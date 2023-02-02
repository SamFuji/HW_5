# import random

# player1 = input("Enter the first player name: ")
# player2 = input("Enter the second player name: ")


# field = [' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ']

# invisible_map = [0, 2, 4, 5, 7, 9, 10, 12, 14]

# win_rec = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# def print_field():
#     print(field[0], end=" ")
#     print(field[1], end=" ")
#     print(field[2], end=" ")
#     print(field[3], end=" ")
#     print(field[4])
#     print('---------')
#     print(field[5], end=" ")
#     print(field[6], end=" ")
#     print(field[7], end=" ")
#     print(field[8], end=" ")
#     print(field[9])
#     print('---------')
#     print(field[10], end=" ")
#     print(field[11], end=" ")
#     print(field[12], end=" ")
#     print(field[13], end=" ")
#     print(field[14])

# print_field()

# def victory():
#     for i in win_rec:
#         if invisible_map[i[0]] == invisible_map[i[1]] == invisible_map[i[2]] :
#             return True
#     return False



# first_turn = random.choice([player1, player2])

# print()

# print(first_turn + ", your move first")

# print()

# if first_turn == player1:
#     print( player1 + " play with 'X' ")
#     print( player2 + " play with 'O' ")
# else:
#     print( player2 + " play with 'X' ")
#     print( player1 + " play with 'O' ")

# print()

# curent_turn = first_turn

# count = 0

# while True:
#     print("Your move, " + curent_turn)
#     if curent_turn == first_turn:
#         sign = 'X'
#         move = int(input("Choise your cell from 1 to 9: "))
#         print()
#         temp = invisible_map[move-1]
#         if field[temp] in ['X', 'O']:
#             print("Cell is already enter!")
#             continue
#         field[temp] = sign
#         invisible_map[move-1] = sign
#     else:
#         sign = 'O'
#         move = int(input("Choise your cell from 1 to 9: "))
#         print()
#         temp = invisible_map[move-1]
#         if field[temp] in ['X', 'O']:
#             print("Cell is already enter!")
#             continue
#         field[temp] = sign
#         invisible_map[move-1] = sign
#     print_field()

#     if victory():
#         print("Winner:" + curent_turn)
#         break
    
#     curent_turn = player2 if curent_turn == player1 else player1
#     count+=1
#     if count == 9:
#         print("Noone wins")
#         break


# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E

text = 'AAAA22222222222222222222222DDDDDFFFFFFFFFFFFFFFFFFFFFFZZZZZZZZOOOOOO'
count = 0
archive = ''
simbol = text[0]

# Сжатие:
for i in text:
    if i != simbol:
        archive+= f"{count}{simbol}"
        simbol = i
        count = 1
    else:
        count+=1
        if count > 8:       # Сделал проверку на двузнайное число, чтобы пра наличие в тексте сжатия более 9 подряд идущих цифр, а не букв, не получилось двузначное число и не возникло проблем при декодировке
            archive+= f"{count}{simbol}"
            simbol = i
            count = 1
else:
    archive+=f"{count}{simbol}"
print ("Исходный текст: " + text)
print ("Сжатие: " + archive)

# Декодировка 

def decode(archive):
    res = ""
    digit = True
    count = 0
    for char in archive:
        if digit:
            count = int(char)
            digit = False
        else:
            res +=count*char
            digit = True
    return res

print("Декодировка:" + decode(archive))








# temp_list = list(archive)
# print(temp_list)

# def decode():
#     for i in range(0, -1, 2):
#         list.append([i])
# print(list[i])

# decode = list(archive)
# print(decode)
# for i in archive:
#     decode +=f"{archive[i]}*{archive[i+1]}"
# print(decode)


# def chec_decode(archive):
#     for i in archive:
#         if i%2 == 0:
#             return True

# decode = f"{lambda i:   }"