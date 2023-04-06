# Есть 1 текстовый файл с данными в архиве:
# Разделить его на 3 текстовых файла

with open("20_december/Data0.txt", "r", encoding='UTF-8') as file:
    lines = file.readlines()

lines = [line for line in lines if line != "\n"]

for i, line in enumerate(lines):
    with open(f"20_december/file_{i + 1}.txt", "w", encoding='UTF-8') as new_file:
        new_file.write(line)
