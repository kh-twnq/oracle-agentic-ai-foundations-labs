from vector_search_local import PRODUCTS, QUERIES, ROOT, embed_catalog_and_queries

VECTOR_SCALE = 1000


def sql_literal(text):
    return "'" + text.replace("'", "''") + "'"


def vector_literal(values):
    return sql_literal("[" + ",".join(str(round(value * VECTOR_SCALE)) for value in values) + "]")


def main():
    product_vectors, query_vectors = embed_catalog_and_queries()
    products = "\n  UNION ALL\n  ".join(
        f"SELECT {id_}, {sql_literal(name)}, {price}, {vector_literal(vector)} FROM dual"
        for (id_, name, _, price, _), vector in zip(PRODUCTS, product_vectors, strict=True)
    )
    queries = "\n  UNION ALL\n  ".join(
        f"SELECT {index}, {ceiling if ceiling is not None else 'NULL'}, {limit}, "
        f"{vector_literal(vector)} FROM dual"
        for index, ((_, ceiling, limit), vector) in enumerate(zip(QUERIES, query_vectors, strict=True), 1)
    )
    sql = f"""WITH products (id, name, price, embedding_text) AS (
  {products}
), query_inputs (query_no, ceiling, result_limit, embedding_text) AS (
  {queries}
), distances AS (
  SELECT q.query_no, q.result_limit, p.id, p.name, p.price,
         VECTOR_DISTANCE(TO_VECTOR(p.embedding_text, 384, FLOAT32),
                         TO_VECTOR(q.embedding_text, 384, FLOAT32), COSINE) AS distance
  FROM products p CROSS JOIN query_inputs q
  WHERE q.ceiling IS NULL OR p.price < q.ceiling
), ranked AS (
  SELECT distances.*, ROW_NUMBER() OVER (PARTITION BY query_no ORDER BY distance, id) AS match_rank
  FROM distances
)
SELECT query_no, match_rank, name, price, ROUND(distance, 6) AS cosine_distance
FROM ranked
WHERE match_rank <= result_limit
ORDER BY query_no, match_rank;
"""
    path = ROOT / "results" / "vector-search-oracle.sql"
    path.parent.mkdir(exist_ok=True)
    path.write_text(sql, encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
