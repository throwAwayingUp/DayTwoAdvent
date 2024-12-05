file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()



fickleString = ""
array = []
safeCount = 0
for i in content:
    if i == " ":
        array.append(int(fickleString))
        fickleString = ""
    if i == "\n":
        safe = True

        if array[len(array) - 1 ] > array[0]:
            breed = "increasing"
        if array[len(array) - 1] < array[0]:
            breed = "decreasing"

        for b in range(0, len(array)):
            if b > 0:
                if array[b] - array[b - 1] > 2 or array[b] - array[b - 1] < -2:
                    safe = False
                if array[b] > array[b - 1] and breed == "decreasing":
                    safe = False
                if array[b] < array[b - 1] and breed == "increasing":
                    safe = False

        if safe:
            safeCount += 1
        fickleString = ""
        array = []

    else:
        fickleString += i

print(safeCount)