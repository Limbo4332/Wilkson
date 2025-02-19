import os
import random

# Путь, по которому сохраняются ключи, по дефолту папка загрузки
download_folder = os.path.expanduser("~/Downloads/qwertykeysgenerated")

if not os.path.exists(download_folder):
    os.makedirs(download_folder)

channel = "beshastsquad"
author = "hdoebtwp"



# Количество ключей которые над сгенерировать по дефолту 300
for i in range(300):
    random_number = random.randint(10 ** 15, 10 ** 16 - 1)
    filename = os.path.join(download_folder, f"key_{i + 1}.txt")

    with open(filename, 'w') as file:
        file.write(str(random_number))

print("\nСгенерированные числа сохранены в папке загрузки.")