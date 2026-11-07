import json
import os

from config.config import Config


def load_json(filename: str):
    path = os.path.join(Config.TEST_DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_customers():
    return load_json("test_data.json")["customers"]


def get_deals():
    return load_json("test_data.json")["deals"]


def get_invalid_credentials():
    return load_json("test_data.json")["invalid_credentials"]
