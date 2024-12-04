file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()



fickleString = ""
array = []

for i in content:
    if i == "\n":
        array += fickleString