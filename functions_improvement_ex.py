# functions improvement exercise
# times-table tester

import random


def input_number():
    print("Times-table tester")
    print()
    testTable = int(input("Which times-table do you want to be tested on? "))
    return testTable

def calculation(testTable):
    for questions in range(1,6):
        Num1 = testTable
        Num2 = random.randrange(2,13)
        Ans = Num1 * Num2
        UserAnswer = int(input(str(Num1) + ' x ' + str(Num2) + ' = ? '))
        if UserAnswer == Ans:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',Ans)
            print()
    return Ans,Num1,Num2

def timesTableTester():
    testTable = input_number()
    Ans,Num1,Num2 = calculation(testTable)



#main program
timesTableTester()
