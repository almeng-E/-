# 메인 실행 파일
from foods_database import *


while __name__ == "__main__":
    print("==========================================================================")
    print("---------------------------K-Food Halal Checker---------------------------")
    print()
    print("!! Welcome to K-Food Halal Checking Program")
    print("!! This program will help you to check whether the food is halal or not")
    while True:
        print()
        n = input('- Do you want to check the food? (y/n) : ')
        if n == 'y':
            food_name = input('Please enter the food name : ')
            if food_name in halal_dict:
                print('This food is halal')
            elif food_name in caution_dict:
                print('This food is caution')
            elif food_name in haram_dict:
                print('This food is haram')
            else:
                print('This food is not in the list')
        elif n == 'n' :
            print()
            print('Goodbye. See you next time! :)')
            print("==========================================================================")
            break
        else:
            print('Please enter y or n')
            continue
    break







