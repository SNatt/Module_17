import sys

user_sequence = input('Введите целые числа через пробел и нажмите ENTER: ')
user_number = int(input('Введите любое целое число: '))

# *** Процедура бинарного поиска ***

def binary_search(list, item):
    idx_low = 0
    idx_high = len(list) - 1
    while idx_low <= idx_high:
        idx_mid = (idx_low + idx_high) // 2
        guess = list[idx_mid]
        if guess == item:
            return idx_mid
        if guess > item:
            idx_high = idx_mid - 1
        else:
            idx_low = idx_mid + 1
    return None

# *** Процедура поиска наименьшего элемента массива ***

def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# *** Процедура сортировки выбором ***

def selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


my_str = user_sequence.replace(' ', '')
if my_str.isdecimal() is not True:         # Проверка.В введённой строке должны содержаться только цифры
    sys.exit('\nВ последовательности содержатся не только цифры!\nПерезапустите программу и повторите ввод.')

list_user_sequence = user_sequence.split()
if len(list_user_sequence) < 2:  # Проверка на минимальное количество элементов в последовательности
    print('\nВаша последовательность содержит только одно значение!')
    sys.exit('Перезапустите программу и повторите ввод.')

# *** Преобразование списка в числовой формат и сортировка

list_user_sequence = [int(item) for item in list_user_sequence]
list_user_sequence = selection_sort(list_user_sequence)
print('\nОтсортированный список:\n', list_user_sequence)

# *** Поиск позиции элемента в списке и вывод результатов ***

idx_item = binary_search(list_user_sequence, user_number)
if idx_item == 0:
    print('\nВаш элемент находится на позиции: 1.\nСледующий больший элемент находится на позиции: 2')
elif idx_item == len(list_user_sequence) - 1:
    print('\nВаш элемент максимальный в списке и занимает позицию', len(list_user_sequence))
    print('Предыдущий меньший элемент занимает позицию:', len(list_user_sequence) - 1)
elif idx_item == None:
    print('\nВашего элемента нет в списке')
else:
    print('\nВаш элемент находится в списке.')
    print('Позиция меньшего числа в списке:', idx_item)
    print('Позиция большего числа в списке:', idx_item + 2)
