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

        array.append(int(fickleString))
        safe = True

        if array[len(array) - 1 ] > array[0]:
            breed = "increasing"
        if array[len(array) - 1] < array[0]:
            breed = "decreasing"
        print(breed)
        for b in range(len(array)):
            if b > 0:
                if array[b] - array[b - 1] > 3 or array[b] - array[b - 1] < -3:
                    safe = False
                if array[b] > array[b - 1] and breed == "decreasing":
                    safe = False
                if array[b] < array[b - 1] and breed == "increasing":
                    safe = False
                if array[b] == array[b - 1]:
                    safe = False

        if safe:
            safeCount += 1


        #print(fickleString)
        #print(array)
        fickleString = ""
        array = []

    else:
        fickleString += i

print(safeCount)




