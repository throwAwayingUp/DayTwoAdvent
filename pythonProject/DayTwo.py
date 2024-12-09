file_path = "C:/Users/BT_2N8_12/PycharmProjects/DayTwoAdvent/pythonProject/input.txt"

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

        virgin = True

        if array[len(array) - 1 ] > array[0]:
            breed = "increasing"
        if array[len(array) - 1] < array[0]:
            breed = "decreasing"
        print(breed)
        for b in range(len(array)):
            if b > 0:
                if array[b] == array[b - 1]:
                    if not virgin:
                        safe = False
                    if virgin:
                         # array[b] = array[b - 1]
                        virgin = False

                if array[b] - array[b - 1] > 3 or array[b] - array[b - 1] < -3:
                    if not virgin:
                        safe = False
                    if virgin:
                        print(array)
                        array[b] = array[b - 1]
                        virgin = False
                if array[b] > array[b - 1] and breed == "decreasing":
                    if not virgin:
                        safe = False
                    if virgin:
                        print(array)
                        array[b] = array[b - 1]
                        virgin = False

                if array[b] < array[b - 1] and breed == "increasing":
                    if not virgin:
                        safe = False
                    if virgin:
                        print(array)
                        array[b] = array[b - 1]
                        virgin = False

        if safe:
            safeCount += 1


        #print(fickleString)
        #print(array)
        fickleString = ""
        array = []

    else:
        fickleString += i

print(safeCount)




