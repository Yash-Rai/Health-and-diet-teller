import webbrowser
from math import pow
import  details
import update_detail
from printing import print_details
from diet_plan import diet


def bmi() :
    height=float(input("Enter your height(IN METERS) : "))
    weight=float(input("Enter your weight(IN KG) : "))
    temp = weight / (pow(height, 2))
    print(f"Your BMI is : {temp}")
    return temp

def workout() :
    workout_male={'shoulder' :'https://www.youtube.com/watch?v=Ot_F4R5KcGQ' ,'back' :'https://www.youtube.com/watch?v=Fqg-jPvjlS4' ,'chest' :'https://www.youtube.com/watch?v=5DFAcAvT2mI' , 'abs ' : 'https://www.youtube.com/watch?v=LjqybbGHqRo', 'legs' : 'https://www.youtube.com/watch?v=hLaJNv1bins' ,'biceps':'https://www.youtube.com/watch?v=_YTjy-Gy-hA','triceps':'https://www.youtube.com/watch?v=NwL6ciw1gsc'}
    workout_female={'shoulder' :'https://www.youtube.com/watch?v=ZLFfQovA1H8' ,'back' :'https://www.youtube.com/watch?v=2nDt5D1g2GU' ,'chest' :'https://www.youtube.com/watch?v=9K2NVgR14BI' , 'abs ' : 'https://www.youtube.com/watch?v=aNpABe7FcII' , 'legs' :'https://www.youtube.com/watch?v=Wgjp0CWcGwM','biceps' :'https://www.youtube.com/watch?v=P38dvlRXYq8','triceps' : 'https://www.youtube.com/watch?v=_LqX4o2vftI'}

    print("------PLEASE ENTER VALID CHOICE --------")
    choice1=input("Enter your sex(m for male and f for female) : ").lower()
    choice2=input("""-> SHOULDER 
    -> BACK 
    -> CHEST
    -> ABS
    -> LEGS
    -> BICEPS
    -> TRICEPS
    Muscles you wanna work on : """).lower()

    if choice1 =='m' :
            webbrowser.open_new(workout_male.get(choice2))

    elif choice1 == 'f' :
            webbrowser.open_new(workout_female.get(choice2))

    else :
            print("------INVALID CHOICE --------")


def enter_details() :
    name=input("Enter your name : ").lower()
    age=input("Enter your age : ").lower()
    gender=input("Enter your gender(M or F) : ").lower()
    mail=input("Enter your MAILID : ").lower()
    height=input("Enter your height : ")
    weight=input("Enter your weight : ")
    candidate=details.Candidate(name,age,gender,mail)
    candidate.bmi(height,weight)
    candidate.write_detail()

def update() :
    name=input("Enter your name : ").lower()
    update_detail.update_bmi(name)


cont='yes'
while(cont!="no") :
        option = {'1': bmi, '2': enter_details, '3': workout, '4': update , '5' : print_details,'6' : diet}
        print("-----WELCOME------")
        choice=input(""" 
        (1) Get your BMI 
        (2) Register to GYM
        (3) Get your workout schedule
        (4) Update detail
        (5) Get your details
        (6) Get your Diet plan
         Enter Your Choice : """)
        option.get(choice)()
        temp_cont=(input("if u wanna do something more enter yes : ")).lower()
        if  temp_cont=="yes" :
            cont="yes"
        else :
            cont="no"

else :
    print("YOU ARE WELCOME AGAIN ")




