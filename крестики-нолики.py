koordinaty = ["00","01","02","10","11","12","20","21","22"]
#игровое поле
def pole():
 print("   ", 0 ," ","","", 1,"  ", 2," ")
 print("  ","_" * 15)
 j = 0
 for i in range(3):
      print(i,"|", koordinaty[0+j] + " |", koordinaty[1+j] + " |", koordinaty[2+j] + " |" )
      print("  |____|____|____|")
      j += 3
#ходы и замена
def hod(index, igrok):
    z = 0
    if index in koordinaty:
        for i in koordinaty:
            if i == index:
                koordinaty[z] = igrok+" "
                return True
            else:
                z += 1
    else:
        return False
#проверяем победу
def proverka():
    if (koordinaty[0] == koordinaty[1] == koordinaty[2]):
        print(koordinaty[0]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[3] == koordinaty[4] == koordinaty[5]):
        print(koordinaty[3]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[6] == koordinaty[7] == koordinaty[8]):
        print(koordinaty[6]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[0] == koordinaty[3] == koordinaty[6]):
        print(koordinaty[0]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[1] == koordinaty[4] == koordinaty[7]):
        print(koordinaty[1]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[2] == koordinaty[5] == koordinaty[8]):
        print(koordinaty[2]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[0] == koordinaty[4] == koordinaty[8]):
        print(koordinaty[0]+"победил! Поздравляю!! Игра окончена.")
        return True
    elif (koordinaty[2] == koordinaty[4] == koordinaty[6]):
        print(koordinaty[2]+"победил! Поздравляю!! Игра окончена.")
        return True
    else:
        return False
#старт
def start():
    igrok = "X"
    shag = 1
    pole()
    while (shag < 10) and (proverka() == False):
        index = input(igrok + ", Введите координаты поля: ")
        if (hod(index, igrok)):
            if igrok == "X":
                igrok = "O"
            else:
                igrok = "X"
            pole()
            shag += 1
        else:
            print("Введите координаты корректно!!!")
    if shag == 10:
        print("Победила дружба! Игра окончена.")
print()
print()
print("Давайте сыграем в 'Крестики - Нолики'!")
print('Координаты вводим без пробела!(как указано на ячейках)')
print('______________________________________')
print()
start()
