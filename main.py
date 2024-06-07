# 메인 실행 파일
from foods_database import *


if __name__ == "__main__":
    print("==========================================================================")
    print("---------------------------K-Food Halal Checker---------------------------")
    print()
    print("!! Welcome to K-Food Halal Checking Program")
    print("!! This program will help you to check whether the food is halal or not")
    while True:
        print()
        btn = input('- Do you want to check the food? (y/n) : ')
        if btn == 'y':
            food_name = input('Please enter the food name : ')
            food_name = food_name.replace(" ","").lower()   # 입력한 음식이 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            if food_name in halal_dict:
                print('This food is halal')
                print('Enjoy your meal! :)')
            elif food_name in caution_dict:
                print('This food needs caution. Please check the following reasons.')
                
            elif food_name in haram_dict:
                print('This food is haram')
            else:
                print('This food is not in the list')
        elif btn == 'n' :
            print()
            print('Goodbye. See you next time! :)')
            print("==========================================================================")
            break
        else:
            print('Please enter y or n')
            continue




