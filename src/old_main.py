from core.test import REWARDS, clear_screen, pull_question

# Welcome the user
clear_screen()
print("Witaj w grze Milionerzy!")
print("Celem tej gry jest odpowiedzenie na 12 pytań. ")
print("Z każdym pytaniem zwiększa się pula nagród!")
print(
    "0 zł → 500 zł → 1000 zł → 2000 zł → 5000 zł → 10000 zł → 20000 zł → 40000 zł → 75000 zł → 125000 zł → 250000 zł → 500000 zł → 1000000 zł"
)
print("Natomiast jeśli się pomylisz, przegrywasz wszystko.")
print(
    "W dowolnym momencie możesz napisać `zakończ` i aktualna suma pieniędzy zostanie wypłacona."
)
print("Zaczynamy!")
input()

poziom = 1

# The game loop
while poziom <= 12:
    clear_screen()
    print(f"Pytanie nr {poziom}")
    question_data = pull_question(poziom)

    question = question_data["pytanie"]
    answer_a = question_data["opcje"]["A"]
    answer_b = question_data["opcje"]["B"]
    answer_c = question_data["opcje"]["C"]
    answer_d = question_data["opcje"]["D"]
    correct_answer = question_data["poprawna"]
    print(f"Grasz o {REWARDS[poziom]}!")
    print(f"Pytanie: {question}")
    print(f"A: {answer_a}")
    print(f"B: {answer_b}")
    print(f"C: {answer_c}")
    print(f"D: {answer_d}")
    user_answer = input("Twoja odpowiedź: ")
    if user_answer.upper().replace(" ", "") == correct_answer:
        print("Gratulacje, poprawna odpowiedź!")
        poziom += 1
        input()
    elif user_answer.lower().replace(" ", "") == "zakończ":
        print(f"Decydujesz się zakończyć grę. Zabierasz ze sobą {REWARDS[poziom - 1]}!")
        print(f"Poprawną odpowiedzią było {correct_answer}.")
        exit()
    elif user_answer.upper().replace(" ", "") in ("A", "B", "C", "D"):
        print(f"Niestety, zła odpowiedź. Poprawną odpowiedzią było {correct_answer}.")
        input()
        exit()
    else:
        print("Musisz odpowiedzieć literką (A/B/C/D)!")
        input()
