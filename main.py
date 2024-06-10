# 융합 기초프로그래밍 실습 과제
# 60190365 아랍지역학과 최원민
# https://github.com/almeng-E/mju-basic-programming 
# 최종 수정일 : 2024.06.10

# ChatGPT 사용 내역 : 버튼 디자인, db 생성
# 이외의 코드는 전부 직접 작성함
# -------------------------------------------------------


# 메인 실행 파일
# from foods_database import *
# import 문 작성
import sunni_db
import shia_db


# 함수 정의
def show_reason(food_name):
    # print(f'이 {food_name}은 {reasons} 등의 이유로 주의가 필요합니다.')
    # # 이 {음식}은 {이유 1}, {이유 2}, {이유 3} 등의 이유로 주의가 필요합니다.
    if foods_dict[food_name] == 'b':
        reasons = caution_reasons
    else:
        reasons = haram_reasons
    print(f'{food_name.upper()} contains the following haram ingredients :')
    for i, v in enumerate(reasons[food_name]):
        print(f'{i+1}.  {ingredients[v]}')

def print_back_to_menu():
    print('>> BACK TO MAIN MENU')

def print_invalid_input():
    print('>> Invalid input. Please enter a valid number.')

def print_check_food(food_name):
    if foods_dict[food_name] == 'a':
        print('This food is halal')
        print('Enjoy your meal! :)')
    elif foods_dict[food_name] == 'b':
        print('This food needs caution, it might contain non-halal ingredients as sub ingredient.')
        show_reason(food_name)
    elif foods_dict[food_name] == 'c':
        print('This food is haram, non-halal ingredients are its main ingredients. Please avoid eating this food.')
        show_reason(food_name)

def print_check_brand(brand_name):
    print(f'Here are two best selling menus from {brand_name}.')
    for item, status in brands_dict[brand_name].items():
        status_str = 'Halal' if status == 1 else 'Haram'
        print(f"+ {item} : {status_str}")
    print('For more information on other menus, try our food name checking service.')

def set_sect():
    # 전역 변수 접근
    global foods_dict
    global caution_reasons
    global haram_reasons
    global ingredients
    global brands_dict
    if sunni:
        foods_dict = sunni_db.foods_dict
        caution_reasons = sunni_db.caution_reasons
        haram_reasons = sunni_db.haram_reasons
        ingredients = sunni_db.ingredients
        brands_dict = sunni_db.brands_dict
    else:
        foods_dict = shia_db.foods_dict
        caution_reasons = shia_db.caution_reasons
        haram_reasons = shia_db.haram_reasons
        ingredients = shia_db.ingredients
        brands_dict = shia_db.brands_dict



# 메인 코드
if __name__ == "__main__":
    # 검색기록 빈 리스트 생성
    searched_history = []
    # 종파 기본 값 설정
    sunni = True
    set_sect()
    # 프로그램 시작
    print("==========================================================================")
    print("---------------------------K-Food Halal Checker---------------------------")
    print()
    print("!! Welcome to K-Food Halal Checking Program")
    print("!! This program will help you to check whether the food is halal or not")
    print("!! Default Sect : Sunni")
    # 무한 루프 시작
    while True:
        print('--------------------------------------------------------------------------')
        print()
        print("┌──────────────────────────────────────────────────────────────────────┐")
        print("│ Please choose an option:                                             │")
        print("│                                                                      │")
        print("│  [1]  Check Food                                                     │")
        print("│  [2]  Check Brand                                                    │")
        print("│  [3]  View Search History                                            │")
        print("│  [4]  Clear Search History                                           │")
        print("│                                                                      │")
        print("│  [9]  Choose Sect ( Sunni , Shia )                                   │")
        print("│                                                                      │")
        print("│  [0]  Exit                                                           │")
        print("└──────────────────────────────────────────────────────────────────────┘")
        btn = input('- Enter your choice: ')
        # 탈출 조건
        if btn == '0' :
            print()
            print('Goodbye. See you next time! :)')
            print("==========================================================================")
            break


        elif btn == '1':
            food_name = input('- Please enter the food name : ')
            # 입력한 음식이 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            food_name = food_name.replace(" ","").lower()   
            if food_name not in foods_dict:
                print('This food is not in the list')
                print_back_to_menu()
                continue
            # 검색 기록에 추가
            searched_history.append(("Food", food_name))
            # 할랄 여부 출력
            print_check_food(food_name)
            # 중복되는 코드를 함수로 만들어서 처리하여, 뒷 내용은 주석 처리 함
            # if foods_dict[food_name] == 'a':
            #     print('This food is halal')
            #     print('Enjoy your meal! :)')
            # elif foods_dict[food_name] == 'b':
            #     print('This food needs caution, it might contain non-halal ingredients as sub ingredient.')
            #     show_reason(food_name)
            # elif foods_dict[food_name] == 'c':
            #     print('This food is haram, non-halal ingredients are its main ingredients. Please avoid eating this food.')
            #     show_reason(food_name)


        elif btn == '2':
            brand_name = input('- Please enter the brand name : ')
            # 입력한 브랜드가 띄어쓰기와 대소문자 구분 없이 검색되도록 소문자로 변환
            brand_name_changed = brand_name.replace(" ","").lower()   
            if brand_name_changed not in brands_dict:
                print('This brand is not in the list')
                print_back_to_menu()
                continue
            # 검색 기록에 추가
            searched_history.append(("Brand", brand_name))
            # 브랜드의 대표 메뉴 및 할랄 여부 출력
            print_check_brand(brand_name_changed)
            # 중복되는 코드를 함수로 만들어서 처리하여, 뒷 내용은 주석 처리 함
            # print(f'Here are two best selling menus from {brand_name}.')
            # # print(brands_dict[brand_name_changed])
            # for item, status in brands_dict[brand_name_changed].items():
            #     status_str = 'Halal' if status == 1 else 'Haram'
            #     print(f"+ {item} : {status_str}")
            # print('For more information on other menus, try our food name checking service.')


        elif btn == '3':   
            print('Search History')
            if searched_history == []:
                print('No search history')
                print_back_to_menu()
                continue
            else:
                print('Here is your search history')
                for i in range(len(searched_history)):
                    # print(f'[{i+1}] {searched_history[i][0]} : {searched_history[i][1]}')
                    print(f'[{i+1:<2}] {searched_history[i][0]:<6} : {searched_history[i][1]:<20}')
                # enumerate를 활용한 코드
                # for idx, (type, value) in enumerate(searched_history, start=1):
                #     print(f'[{idx}] {type} : {value}'
            # 검색 기록 선택 기능
            search_num = input('- Enter the number to view the details (Press Enter to MAIN MENU): ')
            # 빈 문자열 입력시 메인 메뉴로 이동
            if search_num == '':
                print_back_to_menu()
                continue
            # 번호 체크
            if search_num.isdigit() and int(search_num) <= len(searched_history):
                search_index = int(search_num) - 1
                search_type, search_value = searched_history[search_index]
                # 검색 단계 진행
                if search_type == "Food":
                    print(f'Food Name: {search_value}')
                    print_check_food(search_value)
                    # 중복되는 코드를 함수로 만들어서 처리하여, 뒷 내용은 주석 처리 함
                    # if search_value in foods_dict:
                    #     if foods_dict[search_value] == 'a':
                    #         print('This food is halal')
                    #         print('Enjoy your meal! :)')
                    #     elif foods_dict[search_value] == 'b':
                    #         print('This food needs caution, it might contain non-halal ingredients as sub ingredient.')
                    #         show_reason(search_value)
                    #     elif foods_dict[search_value] == 'c':
                    #         print('This food is haram, non-halal ingredients are its main ingredients. Please avoid eating this food.')
                    #         show_reason(search_value)

                elif search_type == "Brand":
                    print(f'Brand Name: {search_value}')
                    print_check_brand(search_value)
                    # 중복되는 코드를 함수로 만들어서 처리하여, 뒷 내용은 주석 처리 함
                    # brand_name_changed = search_value.replace(" ","").lower()
                    # if brand_name_changed in brands_dict:
                    #     print(f'Here are two best selling menus from {search_value}.')
                    #     for item, status in brands_dict[brand_name_changed].items():
                    #         status_str = 'Halal' if status == 1 else 'Haram'
                    #         print(f"+ {item} : {status_str}")
                    #     print('For more information on other menus, try our food name checking service.')
            else:
                print_invalid_input()
                print_back_to_menu()
                continue


        elif btn == '4':
            searched_history = []
            print('>> Search history cleared')
            print_back_to_menu()
            continue


        elif btn == '9':
            print('Choose Sect')
            print('1. Sunni')
            print('2. Shia')
            sect = input('- Enter the number to choose the sect: ')
            if sect == '1':
                if sunni:
                    print('>> Sect is already Sunni')
                else : # 변경
                    sunni = True
                    print('>> Sect has been changed to Sunni')                    
                    set_sect()
            elif sect == '2':
                if not sunni:
                    print('>> Sect is already Shia')
                else: # 변경
                    sunni = False
                    print('>> Sect has been changed to Shia')
                    set_sect()
            else:
                print_invalid_input()
            print_back_to_menu()
            continue


        else:
            print_invalid_input()
            continue



