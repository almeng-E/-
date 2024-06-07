# 메인 실행 파일
from foods_database import *



def show_reason(food_name):
    # print(f'이 {food_name}은 {reasons} 등의 이유로 주의가 필요합니다.')
    # # 이 {음식}은 {이유 1}, {이유 2}, {이유 3} 등의 이유로 주의가 필요합니다.
    if foods_dict[food_name] == 'b':
        reasons = caution_reasons
    else:
        reasons = haram_reasons
    print(f'{food_name.upper()} contains the following haram ingredients :')
    for i, idx in enumerate(reasons[food_name]):
        print(f'{i+1}.  {ingredients[idx]}')
    print('--------------------------------------------------------------------------')




if __name__ == "__main__":
    print("==========================================================================")
    print("---------------------------K-Food Halal Checker---------------------------")
    print()
    print("!! Welcome to K-Food Halal Checking Program")
    print("!! This program will help you to check whether the food is halal or not")
    
    while True:
        print()
        print("┌──────────────────────────────────────────────────────────────────────┐")
        print("│ Please choose an option:                                             │")
        print("│                                                                      │")
        print("│  [1]  Check Food                                                     │")
        print("│  [2]  Check Brand                                                    │")
        print("│  [0]  Exit                                                           │")
        print("└──────────────────────────────────────────────────────────────────────┘")
        btn = input('- Enter your choice: ')
        if btn == '0' :
            print()
            print('Goodbye. See you next time! :)')
            print("==========================================================================")
            break

        elif btn == '1':
            food_name = input('Please enter the food name : ')
            food_name = food_name.replace(" ","").lower()   # 입력한 음식이 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            if food_name not in foods_dict:
                print('This food is not in the list')
                print('BACK TO MAIN MENU')
                continue
            if foods_dict[food_name] == 'a':
                print('This food is halal')
                print('Enjoy your meal! :)')
            elif foods_dict[food_name] == 'b':
                print('This food needs caution, it might contain non-halal ingredients as sub ingredient.')
                show_reason(food_name)
            elif foods_dict[food_name] == 'c':
                print('This food is haram, non-halal ingredients are its main ingredients. Please avoid eating this food.')
                show_reason(food_name)

        elif btn == '2':
            brand_name = input('Please enter the brand name : ')
            brand_name_changed = brand_name.replace(" ","").lower()   # 입력한 브랜드가 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            if brand_name_changed not in brands_dict:
                print('This brand is not in the list')
                print('BACK TO MAIN MENU')
                continue
            print(f'Here are two best selling menues from {brand_name}.')
            print('For more information on other menues, try our food name checking service.')
            print(brands_dict[brand_name_changed])
            print('--------------------------------------------------------------------------')

        else:
            print('Please enter [0], [1], or [2] only.')
            continue




