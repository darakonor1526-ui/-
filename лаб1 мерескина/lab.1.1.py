numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
i=numbers.index(None)
numbers[i] = 0
a = sum(numbers)/len(numbers)
numbers[i] = a
print("Измененный список:", numbers)
