import math
from datetime import date
import openpyxl as x
from mail import sendmail


class Candidate :
    def __init__(self,name , age, gender,mail) :
        self.name=name
        self.age=age
        self.gender=gender.lower()
        self.mail=mail
        self.doj=date.today()

    def bmi(self,height,weight) :
        temp= float(weight)/(math.pow(float(height),2))
        self.bmi=temp
        if(temp<=18.5) :
            self.fat="underweight"
        elif temp>18.5 and temp<25 :
            self.fat= "fit"
        elif  temp>=25 and temp<30 :
            self.fat="overweight"
        else :
            self.fat="obese"


    def write_detail(self) :
        work=x.load_workbook('gymdetails.xlsx')
        sheet=work['Sheet1']
        data=[self.name,self.age,self.gender,self.mail,self.bmi,self.fat,self.doj]
        sheet.append(data)
        work.save('gymdetails.xlsx')
        message=f"""HELLO {self.name.upper()}!
YOU HAVE BEEN REGISTERED SUCCESSFULLY"""
        sendmail(self.mail,message)













