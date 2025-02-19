import os


def get_number(database_file, search_value):
    found = False
    with open(database_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(";")
        if len(data) >= 8:
            phone = data[7]
            if search_value in phone:
                data[1]
                last_name = data[2]
                first_name = data[3]
                middle_name = data[4]
                birthday = data[5]
                gender = data[6]
                email = data[8]
                role = data[9]
                class_name = data[13]
                address = data[19]
                country = data[16]
                citizenship = data[15]
                region = data[17]
                municipal_education = data[18]
                institution_name = data[20]

                print(
                    f"""\033[94m
Base: school.mos.ru
User ID: {data[0]}
Register Date : {data[1]}
Last Name: {data[2]}
Name: {data[3]}
Surname: {data[4]}
Birthday: {data[5]}
Gender: {data[6]}
Phone: {data[7]}
Email: {data[8]}
Role: {data[9]}
Class: {data[13]}
Address: {data[19]}
Country: {data[16]}
Citizenship: {data[15]}
Region: {data[17]}
Municipality: {data[18]}
                Name of institution: {data[20]}

                """
                )
                found = True

    if not found:
        print(f"\033[94mNothing found in database sorry :(.\033[94m")


def get_yandex_eda_number(database_file, search_value):
    found = False
    with open(database_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(";")
        if len(data) >= 5:
            phone = data[0]
            if search_value in phone:
                first_name = data[1]
                full_name = data[2]
                email = data[3]
                address_info = data[4].split(",")

                address_city = address_info[0]
                address_street = address_info[1]
                address_house = address_info[2]
                address_entrance = address_info[3]

                print(
                    f"""\033[94m
 Data: Яндекс.Еда
 Номер: {phone}
 Имя: {first_name}
 Полное имя: {full_name}
 Email: {email}
 Город: {address_city}
 Адресс: {address_street}
 Дом: {address_house}
 Entrance: {address_entrance}
                """
                )
                found = True

    if not found:
        print(f"\033[94mНичего не найдено.... :(.\033[94m")
        print("\033[94mEnter To restart\033[94m")
        input(enter)

def get_number(database_file, search_value):
    found = False
    with open(database_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(";")
        if len(data) >= 5:
            phone = data[0]
            if search_value not in phone:
                continue
            first_name = data[1]
            full_name = data[2]
            email = data[3]
            address_info = data[4].split(",")

            address_city = address_info[0]
            address_street = address_info[1]
            address_house = address_info[2]
            address_entrance = address_info[3]

            user_id = data[0]
            registration_date = data[1]
            last_name = data[2]
            first_name = data[3]
            middle_name = data[4]
            birthday = data[5]
            gender = data[6]
            email = data[8]
            role = data[9]
            class_name = data[13]
            address = data[19]
            country = data[16]
            citizenship = data[15]
            region = data[17]
            municipal_education = data[18]
            institution_name = data[20]

            print(
                 f"""\033[94m
Data:EYEOFGOD
Last Name: {data[2]}
Name: {data[3]}
Surname: {data[4]}
Birthday: {data[5]}
Gender: {data[6]}
Phone: {data[7]}
Email: {data[10]}
Address: {data[19]}
Country: {data[16]}
Citizenship: {data[15]}
Region: {data[17]}
Municipality: {data[18]}
Name of institution: {data[20]}
        """
            )


def get_number(database_file, search_value):
    global phone, data
    found = False
    with open(database_file, "r", encoding="utf-8") as file:
          lines = file.readlines()

    for line in lines:
        data = line.strip().split(";")
        if len(data) >= 5:
                phone = data[0]
    if search_value in phone:
        pass
    else:
        first_name = data[1]
        full_name = data[2]
        email = data[3]
        address_info = data[4].split(",")

        address_city = address_info[0]
        address_street = address_info[1]
        address_house = address_info[2]
        address_entrance = address_info[3]

        user_id = data[0]
        registration_date = data[1]
        last_name = data[2]
        first_name = data[3]
        middle_name = data[4]
        birthday = data[5]
        gender = data[6]
        email = data[8]
        role = data[9]
        class_name = data[13]
        address = data[19]
        country = data[16]
        citizenship = data[15]
        region = data[17]
        municipal_education = data[18]
        institution_name = data[20]
    print(
                       f"""\033[94m
Data: databank
Last Name: {data[2]}
Name: {data[3]}
Surname: {data[4]}
Birthday: {data[5]}
Gender: {data[6]}
Phone: {data[7]}
Email: {data[10]}
Address: {data[19]}
Country: {data[16]}
Citizenship: {data[15]}
Region: {data[17]}
Municipality: {data[18]}
Name of institution: {data[20]}
""")
    registration_date = data[1]
    last_name = data[2]
    first_name = data[3]
    middle_name = data[4]
    birthday = data[5]
    gender = data[6]
    email = data[8]
    role = data[9]
    class_name = data[13]
    address = data[19]
    country = data[16]
    citizenship = data[15]
    region = data[17]
    municipal_education = data[18]
    institution_name = data[20]
    print(
                    f"""\033[94m
                    
Data: SberSpasibo
   registration_date = data[1]
last_name = data[2]
first_name = data[3]
middle_name = data[4]
birthday = data[5]
gender = data[6]
email = data[8]
role = data[9]
class_name = data[13]
address = data[19]
country = data[16]
citizenship = data[15]
region = data[17]
municipal_education = data[18]
institution_name = data[20]   
""")

