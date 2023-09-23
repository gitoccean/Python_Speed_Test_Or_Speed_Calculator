from  time import *    #1
import random as r  #2
def mistake(partest,usertest):   #10
    error = 0     #11
    for i in range(len(partest)):  #12
        try:    #13
            if partest[i] != usertest[i] : #14
                error = error + 1   #15
        except :  #13
            error = error + 1   #16
    return error   #17



def speed_time (time_s,time_e,userinput):   #20
    time_delay = time_e - time_s     #21
    time_R = round(time_delay,2)      #22
    speed = len(userinput) / time_R    #23
    return round(speed)   #24
if __name__ == "__main__":   #35
         while  True:  #27
             ck = input("Are you ready : yes / no :")  #28
             if ck == "yes":   #29
                  test = ["tk_form is a simple module that helps you to create forms in tkinter easily  and quickly from a base dictionary",
                  " saving certain repetitive tasks in the creation of a form and adding the verification of integer and float  variables.",
                  "In simple words it is similar to having a tkinter variable. Its value is a dictionary."]  #3

                  test1 = r.choice(test)   #4 
                  print("  ******Typing Speed******  ")   #5
                  print(test1)  #6
                  print()   #7
                  print()     #8
                  time_1 = time()   #18
                  testinput = input( "Enter :" )    #9
                  time_2 = time()  #19

                  print("Speed :", speed_time (time_1,time_2,testinput),"w/sec")   #25
                  print("Error :",mistake(test1,testinput))  #26 test
             elif  ck == "no":    #30
                 print(" Thank you ")  #31
                 break   #32
             else :  #33
                 print  ("Wrong input") #34    
    
