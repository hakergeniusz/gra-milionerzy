import json
import random
import os
from core.config import PROJECT_ROOT, REWARDS


def pull_question(level: int) -> dict:
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


def clear_screen() -> None:
    """
    Just clears the screen of the user.
    """
    os.system("cls" if os.name == "nt" else "clear")

def give_guaranteed_money(level: int) -> str:
    """
    Returns the guaranteed amount of money in the game.
    
    Args:
        level (int): Current level of the game
    
    Returns:
        str: A string with the guaranteed amount of money for the level.
    """
    if level >= 7:
        return REWARDS[7]
    elif level < 7 and level >= 2:
        return REWARDS[2]
    else:
        return "0 zł"

def remove_two_incorrect_answers(options: dict, correct: str) -> dict:
    """
    Removes two incorrect answers from `options`.
    
    Args:
        options (dict): All answers in a dict.
        correct (str): Letter of the correct answer.
        
    Returns: 
        dict: correct answer and random incorrect answer.
    """
    wrong_keys = [k for k in options if k != correct]
    chosen_wrong = random.choice(wrong_keys)
    
    filtered = {k: options[k] for k in options if k in {correct, chosen_wrong}}
    return filtered