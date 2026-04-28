import json
import random
import os
from core.config import PROJECT_ROOT


def pull_question(level: int):
    """
    Outputs a question to a level.

    Args:
        level (int): Difficulty (1-12)

    Returns:
        dict: {
        "pytanie": "[question]", # e.g. "Który z wymienionych języków nie jest kompilowany?"
        "opcje": {
            "A": "[answer]", # e.g. "Go"
            "B": "[answer]", # e.g. "C++"
            "C": "[answer]", # e.g. "Python"
            "D": "[answer]"  # e.g. "Rust"
        },
        "poprawna": "[correct_answer]" # e.g. "C"
        }
    """

    # File path
    json_path = PROJECT_ROOT / "assets" / "pytania.json"

    # Loading file's contents
    raw_content = json_path.read_text()
    file_content = json.loads(raw_content)

    current_level_questions = file_content[f"poziom_{level}"]

    # Getting and returning a random question
    random_question = random.choice(current_level_questions)

    final_dict = {
        "pytanie": random_question["pytanie"],
        "opcje": random_question["opcje"],
        "poprawna": random_question["poprawna"],
    }
    return final_dict


def clear_screen():
    """
    Just clears the screen of the user.
    """
    os.system("cls" if os.name == "nt" else "clear")
