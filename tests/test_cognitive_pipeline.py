from services.core.cognitive_pipeline import build_cognitive_pipeline


pipeline = build_cognitive_pipeline(
    "Alex"
)

for key, value in pipeline.items():

    print()

    print("=" * 50)

    print(key.upper())

    print("=" * 50)

    print(value)