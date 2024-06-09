# 음식 분류
# 순니파의 할랄 정보를 담은 데이터베이스


halal_list = [
    "kimchi", "bibimbap", "japchae", "gyeranjjim", "gyeranmari", "kongguksu", 
    "hobakjuk", "samgyetang", "kkakdugi", "miyeokguk", "sigeumchinamul", 
    "japgokbap", "dubu", "hobakjeon", "dotorimuk", "baechukimchi", 
    "mulnaengmyeon", "nokdujeon", "pajeon", "tteokguk", "milmyeon", 
    "kalguksu", "dubujorim", "jeonbokjuk", "beoseotjeongol", "ssalbap", 
    "kim", "miyeokmuchim", "yeot", "patbingsu", "tteok", "yakgwa"
]

caution_list = [
    "bulgogi", "tteokbokki", "sundubujjigae", "dakgalbi", "jajangmyeon", 
    "kimbap", "seolleongtang", "galbi", "haemulpajeon", "mandu", "jjamppong", 
    "haejangguk", "bossam", "yangnyeom chicken", "jangjorim"
]

haram_list = [
    "samgyeopsal", "doenjangjjigae", "soondae", "gopchang", "budaejjigae", 
    "sotteoksotteok", "odeng", "sundae"
]



# # 음식 분류 딕셔너리
# # dict comprehension 활용
# halal_dict = {food: "a" for food in halal_list}
# # print(halal_dict)
# caution_dict = {food: "b" for food in caution_list}
# haram_dict = {food: "c" for food in haram_list}


# foods_dict 생성
# dict comprehension 활용
foods_dict = {food: 'a' for food in halal_list}
foods_dict.update({food: 'b' for food in caution_list})
foods_dict.update({food: 'c' for food in haram_list})
# print(foods_dict)


# 주의할 식재료 목록
# 하람 식재료의 목록은 변경되지 않을 것임
# 다만 종파 별 식재료 목록이 다를 수 있으므로 추후에 추가할 수 있음 TODO : 종파 별 분류
ingredients = (
    "Pork", "Pig intestines", "Pork ham", "Pork Bacon", "Lard(pork fat)", "Gelatin", "Alcohol", "Seafood","Non-halal slaughtered meat", "Non-halal cheese"
    )

# 주의할 이유 및 하람 이유 딕셔너리
caution_reasons = {
    "bulgogi": (8,),
    "tteokbokki": (7, 8, 9,),
    "sundubujjigae": (7,),
    "dakgalbi": (8,),
    "jajangmyeon": (1, 4,),
    "kimbap": (2, 7, 8,),
    "seolleongtang": (8,),
    "galbi": (8,),
    "haemulpajeon": (7,),
    "mandu": (0, 8,),
    "jjamppong": (1,),
    "haejangguk": (8,),
    "bossam": (1,),
    "yangnyeom chicken": (8,),
    "jangjorim": (8,),
}

haram_reasons = {
    "samgyeopsal": (0,),
    "doenjangjjigae": (0,),
    "soondae": (0, 1,),
    "gopchang": (0, 1, 8,),
    "budaejjigae": (0, 2, 3,),
    "sotteoksotteok": (0, 2, 3,),
    "odeng": (0, 7,),
    "sundae": (0, 1,)
}


# 브랜드와 대표 메뉴 및 할랄 여부를 변환한 딕셔너리
# 할랄 1 True 하람 0 False
# 브랜드 명은 공식 브랜드 명으로 저장해놓고 싶었지만, 사용자가 입력하여 구분 할 때에 대소문자 구분 없이 비교할 수 있도록 해야 하여 전부 소문자로 교체
brands_dict = {
    "kyochonchicken": {"Soy Garlic Chicken": 1, "Honey Combo Chicken": 1},
    "bhcchicken": {"Prinkle Chicken": 1, "Gold King Chicken": 1},
    "bbqchicken": {"Golden Olive Chicken": 1, "Jamaica Grilled Chicken": 1},
    "bonjuk": {"Abalone Porridge": 1, "Beef Porridge": 1},
    "bibigo": {"Bibimbap": 1, "Galbitang": 1},
    "hanchonseolleongtang": {"Seolleongtang": 1, "Doganitang": 1},
    "hansotdosirak": {"Bulgogi Dosirak": 1, "Spicy Pork Dosirak": 0},
    "nolboobudaejjigae": {"Budaejjigae": 1, "Kimchijjigae": 1},
    "bongchujjimdak": {"Jjimdak": 1, "Soy Sauce Jjimdak": 1},
    "saemaeulsikdang": {"7-Minute Pork Kimchi Jjigae": 0, "Unlimited Beef": 1},
    "hongikdonkatsu": {"King Donkatsu": 0, "Cheese Donkatsu": 0},
    "sinsunseolnongtang": {"Seolnongtang": 1, "Woojoktang": 1},
    "han'sdeli": {"Chicken Doria": 1, "Hamburg Steak": 0},
    "lotteria": {"Bulgogi Burger": 1, "Shrimp Burger": 1},
    "ashley": {"BBQ Ribs": 0, "Pasta": 1},
    "yopgitteokbokki": {"Tteokbokki": 1, "Cheese Tteokbokki": 1},
    "jawstteokbokki": {"Tteokbokki": 1, "Sundae": 1},
    "vips": {"Steak": 0, "Salad Bar": 1},
    "hanampighouse": {"Samgyeopsal": 0, "Hangjeongsal": 0},
    "wonhalmonibossam": {"Bossam": 0, "Jokbal": 0}
}






