import csv
import os

search_input = input(
    '\033[94mВведмте номер телефона для поиска по моей базе данных": \033[94m'
)

file_paths = [
    r"Data_Base\database.csv",
    r"Data_Base\number2.csv",
    r"Data_Base\number3.csv",
    r"Data_Base\^_^.csv",
]

phone_column_variations = [
    "phone",
    "PHONE",
    "номер",
    "Номер",
    "Phone",
    "Телефон",
    "phone_number",
]

for file_path in file_paths:
    if os.path.exists(file_path):
        with open(file_path, newline="", encoding="utf-8") as file:
            is_csv = file_path.lower().endswith(".csv")

            if is_csv:
                csv_reader = csv.DictReader(file, delimiter=",")
                # Check for any of the possible variations of the specified columns
                if any(
                        column.lower() in map(str.lower, csv_reader.fieldnames)
                        for column in phone_column_variations
                ):
                    for row in csv_reader:
                        # Check for any of the possible variations of the specified columns' values
                        if any(
                                search_input.lower() in str(row.get(column)).lower()
                                for column in phone_column_variations
                        ):
                            print(
                                f"""\033[94m
DATA 'number3.csv'
Region: {row.get('region', 'N/A')}
Full_Name: {row.get('FNAME', 'N/A')}
Last_Name: {row.get('LNAME', 'N/A')}
Phone: {row.get('phone', 'N/A')}
Address: {row.get('address', 'N/A')}  
Section: {row.get('section', 'N/A')}  
Time_Zone: {row.get('time_zone', 'N/A')}  
Podm: {row.get('podm', 'N/A')}  

DATA 'number2.csv'
Email: {row.get('EMAIL', 'N/A')}
Full_Name: {row.get('FNAME', 'N/A')}
Last_Name: {row.get('LNAME', 'N/A')}
Phone: {row.get('PHONE', 'N/A')}
Instagram_ID: {row.get('INSTAGRAM_ID', 'N/A')}


                            \033[94m"""
                            )
                        from search import get_number, get_yandex_eda_number

                        database_file = ('Data_Base\databank.csv')
                        # noinspection PyRedeclaration
                        database_file = 'Data_Base\database.csv'
                        yandex_eda_db = 'Data_Base\yandex_eda.csv'
                        database_file = 'Data_Base\EYEOFGOD.csv'
                        database_file = 'Data_Base\Sberspasibo2023.txt'
                        search_value = search_input
                        found_in_main_db = get_number(database_file, search_value)

                        if not found_in_main_db:
                            get_yandex_eda_number(yandex_eda_db, search_value)
                            input("Press enter to continue: ")
                            input("\033[94mPress enter to continue\033[94m")
                else:
                    print(
                        f"\033[94mColumns not found in {file_path}: {', '.join(phone_column_variations)}\033[94m"
                    )
            else:
                print(f"\\033[94m{file_path} is not a CSV file\033[94m")
    else:
        print(f"\033[94mFile not found: {file_path}\033[94m")
