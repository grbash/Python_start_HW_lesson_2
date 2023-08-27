#  Допущение для всех задач: Пользователь вводит адекватные значение 
# (если в условии задачи написано "возводит число A в натуральную степень B", то мы допускаем, 
# что число B на вход мы получим натуральное, а вот А может быть любое, иначе придется использовать слишком много проверок)

# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

sumOfHeads = 0
sumOfTails = 0
for i in range(int(input("Enter number of coins: "))):
    if int(input(f"Enter coin {i + 1} state: ")) == 1:
        sumOfHeads += 1
    else:
        sumOfTails += 1
if sumOfTails < sumOfHeads:
    print(f"You need to turn {sumOfTails} coin(s)")
else:
    print(f"You need to turn {sumOfHeads} coin(s)")