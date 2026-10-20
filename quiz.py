questions=[
    {
      "question":"Which keyword is used to define a funtion in python?",
      "options":{
          "A":"function",
          "B":"def",
          "C":"define",
          "D":"fun"
      },
      "answer":"B"
    },
    {
        "question":"which data types stores  key-value pairs?",
        "options":{
            "A":"list",
            "B":"tuple",
            "C":"dictionary",
            "D":"set"
        },
        "answer":"C"
    },
    {
        "question":"what is output of print(2+3)?",
        "options":{
            "A":"23",
            "B":"5",
            "C":"6",
            "D":"Error"
        },
        "answer":"B"
    },
    {
        "question":"Which symbol is user for comments in python?",
        "options":{
            "A":"//",
            "B":"<!-- -->",
            "C":"#",
            "D":"**"
        },
        "answer":"C"
    },
    {
        "question":"which function is used to get user input?",
        "options":{
            "A":"print()",
            "B":"len()",
            "C":"input()",
            "D":"type()"
        },
        "answer":"C"
    },
    {
        "question":"which data type stores True or False?",
        "options":{
            "A":"int",
            "B":"str",
            "C":"bool",
            "D":"list"
        },
        "answer":"C"
    },
    {
        "question":"which operator is used exponentation in python?",
        "options":{
            "A":"^",
            "B":"**",
            "C":"//",
            "D":"%"
        },
        "answer":"B"
    },
    {
        "question":"which funtion return a length of a list?",
        "options":{
            "A":"size()",
            "B":"count()",
            "C":"range()",
            "D":"len()"
        },
        "answer":"D"
    },
    {
        "question":"which keyworsd is used  for a loop in python? ",
        "options":{
            "A":"for",
            "B":"repeat",
            "C":"loop",
            "D":"iterate"
        },
        "answer":"A"
    },
    {
        "question":"which methoed adds an item to the end of list?",
        "options":{
            "A":"inser_end()",
            "B":"add()",
            "C":"append()",
            "D":"extend_one()"
        },
        "answer":"C"
    }

]
def s_quiz():
    score=0
    for q in questions:
        print("\n" + q["question"])
        for option ,text in q["options"].items():
            print(option +"-" + text)
        answer=input("Enter your answer(A,B,C,D:):").upper().strip()
        if answer not in["A","B","C","D"]:
            print("invalid option! Please enter A,B,C,D.")
            print("The correct answer is:",q["answer"])
        elif answer ==q["answer"]:
            print("Correct answer......")
            score +=1
        else:
            print("Incorrect answer!!!!!")
            print("The correct answer is:",q["answer"])

    total=len(questions)
    incorrect=total-score
    percentage=(score/total)*100

    print("---Quiz Results---")
    print("Total questions:",total)
    print("Correct answers:",score)
    print("Incorrect answers:",incorrect)
    print("Percentage:",percentage,"%")

    if percentage>=80:
        print("Excellent Performance!")
    elif percentage>=50:
        print("Good! keep practicing!")
    else:
        print("Need more practice!")
    



def menu():
    print("="*20)
    print("QUIZ APPLICATION")
    print("="*20)
    print("1.Start Quiz")
    print("2.View Instructions")
    print("3.Exit")

def show_instructions():
    print("\n ========== Quiz Insructions ==========")
    print("1. Each Questions has four options:A,B,C,D")
    print("2. Select the correct option.")
    print("3. Each correct option get 1 point.")
    print("4. No point fro incorrect answers.")
    print("5. Your final score will be displayed")

while True:
    menu()
    choice=int(input("Enter Your Choice:"))
    if choice==1:
        while True:
            s_quiz()
            replay=input("Do you want to play again?(yes/no)")
            if replay=="yes":
                break
    elif choice==2:
        show_instructions()
    elif choice==3:
        print("Thank You For Using Quiz App....")
        break
    else:
        print("Invaild Choice! Please try again!")


