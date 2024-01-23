pets = dict()
n = int(input('Сколько животных хотите  добавить:'))
for i in range(n):
    pet = input('Чтобы добавить питомца введите его имя:' )
    view = input('Вид питомца:')
    age = int(input('Возраст питомца:'))
    owner = input('Владелец:')

    pets[pet] = {
        "Вид питомца": view,
        "Возраст питомца": age,
        "Имя владельца": owner
    }
pet_info = pets[pet]

for k in pet_info:
    if pet_info["Возраст питомца"] == 1:
        age_suffix = "год"
    elif pet_info["Возраст питомца"] <= 4:
        age_suffix = "года"
    elif pet_info["Возраст питомца"] <= 20:
        age_suffix = "лет"
    elif pet_info["Возраст питомца"] == 21:
        age_suffix = "год"
    elif pet_info["Возраст питомца"] <= 24:
        age_suffix = "года"
    elif pet_info["Возраст питомца"] <= 30:
        age_suffix = "лет"
    elif pet_info["Возраст питомца"] <= 20:
        age_suffix = "лет"
    elif pet_info["Возраст питомца"] == 31:
        age_suffix = "год"
    elif pet_info["Возраст питомца"] <= 34:
        age_suffix = "года"
    elif pet_info["Возраст питомца"] <= 40:
        age_suffix = "лет"
    elif pet_info["Возраст питомца"] == 41:
        age_suffix = "год"
    elif pet_info["Возраст питомца"] <= 44:
        age_suffix = "года"
    elif pet_info["Возраст питомца"] <= 50:
        age_suffix = "лет"
    else: age_suffix = ""


info_string = f"Это {pet_info['Вид питомца']} по кличке \"{pet}\". Возраст питомца: {pet_info['Возраст питомца']} {age_suffix}. Имя владельца: {pet_info['Имя владельца']}"
print(info_string)
