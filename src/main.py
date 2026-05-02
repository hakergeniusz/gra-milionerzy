import random
import time

from core.config import REWARDS
from core.functions import clear_screen, give_guaranteed_money, pull_question, remove_two_incorrect_answers

# Welcome the user
clear_screen()
print("Witaj w grze Milionerzy!")
print("Celem tej gry jest odpowiedzenie na 12 pytań. ")
print("Z każdym pytaniem zwiększa się pula nagród!")
print(
    "0 zł → 1000 zł → 2000 zł (G) → 5000 zł → 10000 zł → 15000 zł → 25000 zł → 50000 zł (G) → 75000 zł → 125000 zł → 250000 zł → 500000 zł → 1000000 zł"
)
print(
    "Natomiast jeśli się pomylisz, otrzymujesz pieniądze z progu gwarantowanego (G), do którego doszedłeś."
)
print("Możesz w dowolnym momencie napisać `koło ratunkowe` i skorzystać z koła ratunkowego, które usuwa dwie błędne odpowiedzi,")
print(
    "ale ta funkcja jest limitowana dwa razy na grę. Również, możesz napisać `zakończ` i aktualna suma pieniędzy zostanie wypłacona."
)
print("Zaczynamy!")
input()

poziom = 1
left_lifeline_uses = 2
# The game loop
while poziom <= 12:
    clear_screen()

    question_data = pull_question(poziom)
    correct_answer = question_data["poprawna"]
    while True:
        clear_screen()
        print(f"Pytanie nr {poziom}")
        print(f"Grasz o {REWARDS[poziom]}!")
        print(f"Pytanie: {question_data['pytanie']}")
        if len(question_data["opcje"]) == 2:
            print(f"Pozostało użyć koła ratunkowego: {left_lifeline_uses}")
        for klucz, tresc in question_data["opcje"].items():
            print(f"{klucz}: {tresc}")

        user_answer = input("Twoja odpowiedź: ").strip().lower()
        user_answer_upper = user_answer.upper()

        if user_answer_upper == correct_answer:
            print("Gratulacje, poprawna odpowiedź!")
            poziom += 1
            input()
            break
        elif user_answer == "zakończ" and poziom == 1:
            print(
                "Decydujesz się zakończyć grę, bez odpowiadania na jakiekolwiek pytanie."
            )
            print("Zabierasz ze sobą 0 zł.")
            exit()
        elif user_answer == "zakończ":
            print(
                f"Decydujesz się zakończyć grę. Zabierasz ze sobą {REWARDS[poziom - 1]}!"
            )
            print(f"Poprawną odpowiedzią było {correct_answer}.")
            exit()
        elif user_answer == "koło ratunkowe" and left_lifeline_uses > 0 and len(question_data['opcje']) == 4:
            left_lifeline_uses -= 1
            question_data['opcje'] = remove_two_incorrect_answers(question_data['opcje'], question_data['poprawna'])
        elif user_answer_upper in ("A", "B", "C", "D"):
            print(
                f"Niestety, zła odpowiedź. Poprawną odpowiedzią było {correct_answer}."
            )
            if poziom > 2:
                guaranteed_reward = give_guaranteed_money(poziom - 1)
                print(
                    f"Doszedłeś do progu gwarantowanego, więc odchodzisz z {guaranteed_reward}!"
                )
            else:
                print(
                    "Nie doszedłeś jeszcze do progu gwarantowanego, więc dostajesz nic."
                )
            input()
            exit()
        elif user_answer == "koło ratunkowe" and len(question_data['opcje']) == 2:
            print("Użyłeś już koła ratunkowego na to pytanie!")
            input()
        elif user_answer == "koło ratunkowe" and left_lifeline_uses == 0:
            print("Nie masz już użyć koła ratunkowego!")
            input()
        else:
            print("Musisz odpowiedzieć literką (A/B/C/D)!")
            input()

random_offset = random.uniform(-0.5, 0.5)
time.sleep(2 + random_offset)

print("Gratulacje! Odpowiedziałeś poprawnie na wszystkie 12 pytań.")
print(
    "Natomiast ze względu na budżet projektu, nie jesteśmy w stanie wypłacić 1000000zł."
)
