import json
import sys

def chat(prompt: str, personality: str) -> str:
    return "This is your answer"

def load_character(character_path: str):
    with open(character_path, "r", encoding="utf-8") as f:
        character = json.load(f)
    return character

def main():

    character_path = sys.argv[1]
    character = load_character(character_path)

    character_name = character["name"]
    character_personality = character["personality"]

    while True:
        prompt = input("You: ")

        if prompt in ["exit", "quit", "leave"]:
            return

        answer = chat(prompt, character_personality)

        print(f"{character_name}: {answer}")

if __name__ == "__main__":
    main()