# 음식 분류
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



# 음식 분류 딕셔너리
# dict comprehension 활용
halal_dict = {food: "a" for food in halal_list}
# print(halal_dict)
caution_dict = {food: "b" for food in caution_list}
haram_dict = {food: "c" for food in haram_list}


# 주의할 식재료 목록
# 하람 식재료의 목록은 변경되지 않을 것임
# 다만 종파 별 식재료 목록이 다를 수 있으므로 추후에 추가할 수 있음 TODO : 종파 별 분류
ingredients = (
    "Pork", "Pig intestines", "Pork ham", "Pork Bacon", "Lard(pork fat)", "Gelatin", "Alcohol", "Seafood","Non-halal slaughtered meat", "Non-halal cheese"
    )

# 주의할 이유 및 하람 이유 딕셔너리
caution_reasons = {
    "bulgogi": (8),
    "tteokbokki": (7, 8, 9),
    "sundubujjigae": (7),
    "dakgalbi": (8),
    "jajangmyeon": (1),
    "kimbap": (7, 8),
    "seolleongtang": (8),
    "galbi": (8),
    "haemulpajeon": (7),
    "mandu": (1, 8),
    "jjamppong": (1),
    "haejangguk": (8),
    "bossam": (1),
    "yangnyeom chicken": (8),
    "jangjorim": (8),
}

haram_reasons = {
    "samgyeopsal": (0),
    "doenjangjjigae": (0),
    "soondae": (0, 1),
    "gopchang": (1, 2, 8),
    "budaejjigae": (0, 2),
    "sotteoksotteok": (0, 3),
    "odeng": (0, 5),
    "sundae": (0, 1)
}


# 브랜드와 대표 메뉴 및 할랄 여부를 변환한 딕셔너리
# 할랄 1 True 하람 0 False
brands = {
    "Kyochon Chicken": {"Soy Garlic Chicken": 1, "Honey Combo Chicken": 1},
    "BHC Chicken": {"Prinkle Chicken": 1, "Gold King Chicken": 1},
    "BBQ Chicken": {"Golden Olive Chicken": 1, "Jamaica Grilled Chicken": 1},
    "Bonjuk": {"Abalone Porridge": 1, "Beef Porridge": 1},
    "Bibigo": {"Bibimbap": 1, "Galbitang": 1},
    "Hanchon Seolleongtang": {"Seolleongtang": 1, "Doganitang": 1},
    "Hansot Dosirak": {"Bulgogi Dosirak": 1, "Spicy Pork Dosirak": 0},
    "Nolboo Budaejjigae": {"Budaejjigae": 1, "Kimchijjigae": 1},
    "Bongchu Jjimdak": {"Jjimdak": 1, "Soy Sauce Jjimdak": 1},
    "Saemaeul Sikdang": {"7-Minute Pork Kimchi Jjigae": 0, "Unlimited Beef": 1},
    "Hongik Donkatsu": {"King Donkatsu": 0, "Cheese Donkatsu": 0},
    "Sinsun Seolnongtang": {"Seolnongtang": 1, "Woojoktang": 1},
    "Han's Deli": {"Chicken Doria": 1, "Hamburg Steak": 0},
    "Lotteria": {"Bulgogi Burger": 1, "Shrimp Burger": 1},
    "Ashley": {"BBQ Ribs": 0, "Pasta": 1},
    "Yopgi Tteokbokki": {"Tteokbokki": 1, "Cheese Tteokbokki": 1},
    "Jaws Tteokbokki": {"Tteokbokki": 1, "Sundae": 1},
    "VIPS": {"Steak": 0, "Salad Bar": 1},
    "Hanam Pig House": {"Samgyeopsal": 0, "Hangjeongsal": 0},
    "Won Halmoni Bossam": {"Bossam": 0, "Jokbal": 0}
}






