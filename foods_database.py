# 음식 분류
halal_list = [
    "kimchi", "bibimbap", "japchae", "gyeran-jjim", "gyeran-mari", "kongguksu", 
    "hobakjuk", "samgyetang", "kkakdugi", "miyeok-guk", "sigeumchi-namul", 
    "japgokbap", "dubu", "hobakjeon", "dotorimuk", "baechu-kimchi", 
    "mul-naengmyeon", "nokdu-jeon", "pajeon", "tteokguk", "milmyeon", 
    "kalguksu", "dubu-jorim", "jeonbok-juk", "beoseot-jeongol", "ssalbap", 
    "kim", "miyeok-muchim", "yeot", "patbingsu", "tteok", "yakgwa"
]

caution_list = [
    "bulgogi", "tteokbokki", "sundubu-jjigae", "dakgalbi", "jajangmyeon", 
    "kimbap", "seolleongtang", "galbi", "haemul-pajeon", "mandu", "jjamppong", 
    "haejangguk", "bossam", "yangnyeom chicken", "jangjorim"
]


haram_list = [
    "samgyeopsal", "doenjang-jjigae", "soondae", "gopchang", "budae-jjigae", 
    "sotteok-sotteok", "odeng", "sundae"
]
# 만약 추가 할 음식이 있다면, list에 append 하면 됨
# 이후 dict comprehension을 활용하여 dict를 만들어주면 됨

# 음식 분류 딕셔너리
# dict comprehension 활용
halal_dict = {food: "a" for food in halal_list}
# print(halal_dict)
caution_dict = {food: "b" for food in caution_list}
haram_dict = {food: "c" for food in haram_list}



# 주의할 식재료 목록
ingredients = (
    "Pork", "Pig intestines", "Pork ham", "Pork Bacon", "Lard(pork fat)", "Gelatin", "Alcohol", "Seafood","Non-halal slaughtered meat", "Non-halal cheese"
    )

# 주의할 이유 및 하람 이유 딕셔너리
caution_reasons = {
    "bulgogi": (8),
    "tteokbokki": (7, 8, 9),
    "sundubu-jjigae": (7),
    "dakgalbi": (8),
    "jajangmyeon": (1),
    "kimbap": (7, 8),
    "seolleongtang": (8),
    "galbi": (8),
    "haemul-pajeon": (7),
    "mandu": (1, 8),
    "jjamppong": (1),
    "haejangguk": (8),
    "bossam": (1),
    "yangnyeom chicken": (8),
    "jangjorim": (8),
}

haram_reasons = {
    "samgyeopsal": (0),
    "doenjang-jjigae": (0),
    "soondae": (0, 1),
    "gopchang": (1, 2, 8),
    "budae-jjigae": (0, 2),
    "sotteok-sotteok": (0, 3),
    "odeng": (0, 5),
    "sundae": (0, 1)
}







