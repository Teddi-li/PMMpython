import json

settings = {"theme": "dark",
            "language": "en",
            "volume": 70}

with open("settings.json", "w", encoding="utf-8") as f:
    json.dump(settings, f, ensure_ascii=False, indent=2)

with open("settings.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("Loaded:", loaded)
