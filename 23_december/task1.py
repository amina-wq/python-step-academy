#   Есть папка с данными в архиве:
#   Нужно написать скрипт, который «проходит» по всем папкам и удаляет только файлы «for_delete.txt»

import os

for root, directories, files in os.walk("./23_december/for_scan"):
    if os.path.exists(f"{root}/for_delete.txt"):
        os.remove(f"{root}/for_delete.txt")



