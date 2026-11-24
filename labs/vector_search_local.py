import json
from math import sqrt
from pathlib import Path
import sqlite3

from fastembed import TextEmbedding

ROOT = Path(__file__).resolve().parent
MODEL = "sentence-transformers/all-MiniLM-L6-v2"
PRODUCTS = [
    (1, "Running Shoes", "Light trail shoes with a cushioned sole", 89.99, "Footwear"),
    (2, "Hiking Boots", "Leather boots with waterproofing for mountain hikes", 149.99, "Footwear"),
    (3, "Tennis Racket", "300 g carbon-fiber racket for competitive tennis", 199.99, "Sports"),
    (4, "Yoga Mat", "Slip-resistant 6 mm mat made of eco-friendly material for yoga workouts", 29.99, "Fitness"),
    (5, "Basketball", "Standard composite basketball for indoor or outdoor play", 34.99, "Sports"),
    (6, "Climbing Harness", "Adjustable climbing safety harness with attachment loops", 79.99, "Outdoor"),
    (7, "Swimming Goggles", "Racing swim goggles with fog resistance and UV protection", 24.99, "Aquatics"),
    (8, "Cycling Helmet", "Ventilated, streamlined helmet for road cycling", 69.99, "Cycling"),
    (9, "Camping Tent", "Waterproof dome shelter for two campers", 129.99, "Outdoor"),
    (10, "Fitness Tracker", "Wristband that measures heart rate and counts steps", 49.99, "Electronics"),
]
QUERIES = [("gear for exercising at home", None, 3), ("protection for water sports", 100, 5)]


def embed_catalog_and_queries():
    model = TextEmbedding(model_name=MODEL, cache_dir=str(ROOT / ".cache" / "fastembed"))
    texts = [product[2] for product in PRODUCTS] + [query for query, _, _ in QUERIES]
    vectors = [vector.tolist() for vector in model.embed(texts)]
    assert len(vectors) == len(texts)
    assert all(len(vector) == 384 for vector in vectors)
    return vectors[:len(PRODUCTS)], vectors[len(PRODUCTS):]


def cosine_distance(left, right):
    a, b = json.loads(left), json.loads(right)
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    return 1 - dot / sqrt(sum(x * x for x in a) * sum(y * y for y in b))


def main():
    product_vectors, query_vectors = embed_catalog_and_queries()
    with sqlite3.connect(":memory:") as db:
        db.create_function("cosine_distance", 2, cosine_distance, deterministic=True)
        db.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY, name TEXT, description TEXT,
                price REAL, category TEXT, embedding TEXT
            )
        """)
        db.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", [
            (*product, json.dumps(vector))
            for product, vector in zip(PRODUCTS, product_vectors, strict=True)
        ])
        keyword_hits = db.execute("""
            SELECT name FROM products
            WHERE description LIKE '%gear%' OR description LIKE '%exercising%' OR description LIKE '%home%'
        """).fetchall()
        assert keyword_hits == []
        results = []
        for (query, ceiling, limit), vector in zip(QUERIES, query_vectors, strict=True):
            matches = db.execute(
                """
                SELECT name, price, category, cosine_distance(embedding, ?) AS distance
                FROM products
                WHERE ? IS NULL OR price < ?
                ORDER BY distance, id
                LIMIT ?
                """,
                (json.dumps(vector), ceiling, ceiling, limit),
            ).fetchall()
            assert len(matches) == limit
            if ceiling is not None:
                assert all(price < ceiling for _, price, _, _ in matches)
            results.append({
                "query": query, "limit": limit, "price_below_usd": ceiling,
                "matches": [
                    {"name": name, "price_usd": price, "category": category, "distance": round(distance, 5)}
                    for name, price, category, distance in matches
                ],
            })
    assert results[1]["matches"][0]["name"] == "Swimming Goggles"
    report = {
        "engine": "SQLite with cosine distance", "embedding_model": MODEL, "dimensions": 384,
        "catalog": "Ten workshop products with paraphrased descriptions", "product_count": len(PRODUCTS),
        "keyword_match_count": len(keyword_hits), "queries": results,
    }
    path = ROOT / "results" / "vector-search-local.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
