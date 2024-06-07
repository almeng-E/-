# 메인 실행 파일
from foods_database import *



def show_reason(food_name):
    # print(f'이 {food_name}은 {reasons} 등의 이유로 주의가 필요합니다.')
    # # 이 {음식}은 {이유 1}, {이유 2}, {이유 3} 등의 이유로 주의가 필요합니다.
    if foods_dict[food_name] == 'b':
        reasons = caution_reasons
    else:
        reasons = haram_reasons

    for i, idx in enumerate(reasons[food_name]):
        print(f'{i+1} : ingredient ~ {ingredients[idx]}')



if __name__ == "__main__":
    print("==========================================================================")
    print("---------------------------K-Food Halal Checker---------------------------")
    print()
    print("!! Welcome to K-Food Halal Checking Program")
    print("!! This program will help you to check whether the food is halal or not")
    while True:
        print()
        btn = input('- Do you want to check the food? (y/n) : ')
        if btn == 'n' :
            print()
            print('Goodbye. See you next time! :)')
            print("==========================================================================")
            break

        elif btn == 'y':
            food_name = input('Please enter the food name : ')
            food_name = food_name.replace(" ","").lower()   # 입력한 음식이 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            if foods_dict[food_name] == 'a':
                print('This food is halal')
                print('Enjoy your meal! :)')
            elif foods_dict[food_name] == 'b':
                print('This food needs caution, it might contain non-halal ingredients as sub ingredient.')
                print('Please check the following reasons.')
                show_reason(food_name)
            elif foods_dict[food_name] == 'c':
                print('This food is haram, non-halal ingredients are the main ingredients. Please avoid eating this food.')
                print('Please check the following reasons.')
                show_reason(food_name)
            else:
                print('This food is not in the list')
        else:
            print('Please enter y or n')
            continue




