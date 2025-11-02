import json, os, datetime

DATA_DIR = "data/conversations"
os.makedirs(DATA_DIR, exist_ok=True)

def save_conversation(messages):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{DATA_DIR}/convo_{timestamp}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    return file_path

def list_conversations():
    return sorted(os.listdir(DATA_DIR), reverse=True)

def load_conversation(filename):
    with open(f"{DATA_DIR}/{filename}", "r", encoding="utf-8") as f:
        return json.load(f)