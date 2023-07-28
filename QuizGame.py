

questions=("Güneş sisteminde kaç gezegen vardır ? ",
           "Periyodık tabloda kaç element vardır ?",
           "Kurşunun periyodik tablodaki kısaltımı nedir ?",
           "Ortalama en uzun yaşayan canlı nedir ? ")

options=(("A)4","B)7","C)8","D)10"),
         ("A)116","B)118","C)117","D)120"),
         ("A)Ku" ,"B)Pb","C)Kl" ,"D)P"),
         ("A)Grönland Balinası","B)Deniz Anasi","C)Fil","D)Zurafa"))

answers=("C","B","B","A")
gueses=[]

score=0

question_num=0

for question in questions:
    print("------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Choose your answer ! Enter (A, B, C, D) ").upper()
    gueses.append(guess)

    if guess==answers[question_num]:
        score+=1
        print("CORRECT !")
    else:
        print(f"INCORRECT")
        print(f"The correct answer is {answers[question_num]}")    
    question_num+=1    


print("------------------------------------")
print("            RESULTS                 ")  
print("------------------------------------")



print("Your Answers: ",end="")
for yanswers in gueses:
    print(yanswers,end=" ")
print()


print("Correct Answers: ",end="")
for answers in answers:
    print(answers,end=" ")
print()


    
    

print(f"Your score is : {score} ")    
        





