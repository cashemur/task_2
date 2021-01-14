from random import randint
firstArray = [randint(-1000, 1000) for i in range(1000)]#Создание и заполнение массива на 1000 элементов случайными числами в диапазоне от - 1000 до 1000
print(firstArray)
sum = 0#Обьявление переменной для вычисления суммы всех элементов массива
for i in range(len(firstArray)):#Вычисление суммы всех элементов массива
    sum += firstArray[i]
avg = sum / len(firstArray)#Вычесление среднего арифмитического
print("Average =", avg)
newArray = []#Новый массив для записи в него элементов из массива firstArray
for i in range(len(firstArray)):
    if (avg + avg * 0.2) >= firstArray[i] >= (avg - avg * 0.2):#Поиск значения, которые на 20% отличаются от среднего
        newArray.append(firstArray[i])#Добавление найденых элементов в массив newArray
print(newArray)
