import random

questions = ("What is the capital of France?","Who wrote the play “Romeo and Juliet”?","Which planet is known as the “Red Planet”?",
"What is the chemical symbol for water?","Who painted the “Mona Lisa”?","Which country is known as the “Land of the Rising Sun”?",
"What is the largest mammal on Earth?","Who was the first woman to fly solo across the Atlantic Ocean?","Which gas do plants absorb during photosynthesis?",
"What is the currency of Japan?")

options = (("A) Berlin", "B) Paris", "C) Rome", "D) Madrid"),("A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"),
("A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"),("A) H2O", "B) CO2", "C) O2", "D) CH4"),("A) Vincent van Gogh", "B) Leonardo da Vinci", "C) Pablo Picasso", "D) Michelangelo"),
("A) China", "B) Japan", "C) South Korea", "D) Thailand"),("A) Elephant", "B) Blue whale", "C) Giraffe", "D) Rhinoceros"),
("A) Amelia Earhart", "B) Marie Curie", "C) Rosa Parks", "D) Florence Nightingale"),("A) Oxygen", "B) Nitrogen", "C) Carbon dioxide", "D) Hydrogen"),
("A) Yen", "B) Euro", "C) Dollar", "D) Pound"))

currect_answers = ("B","A","B","A","B","B","B","A","C","A")
score = 0
i = 0

for question in questions:
    print("-------------------------------------------------------------------")
    print(f"{i+1}. {question}")
    for option in options[i]:
        print(option)
    user_answer = input("Enter Your Option (A/B/C/D): ").upper()
    if user_answer == currect_answers[i]:
        print(f"\n\tCurrect Answer !")
        score+= 1
    else:
        print(f"\nWrong Answer !\n\t\t Right Option Is: {currect_answers[i]}")
    i+= 1


print("-------------------------------------------------------------------")
print("                             Score                                 ")
print("-------------------------------------------------------------------")
print(f"Youre Score Is: {int(score/i*100)}%")
input("Enter To Exit: ")
    