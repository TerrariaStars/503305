import time
import keyboard
import threading
import os

def zvezda_ris():
    os.system('cls')
    size = int(input('Введите нечетное число не превышающее 29\n'))
    os.system('cls')
    if size % 2 == 0:
        os.system('cls')
        print("Размер должен быть нечетным")
        time.sleep(1)
        return
    if size > 29:
        os.system('cls')
        print("Размер не должен превышать 29")
        time.sleep(1)
        return
    
    zvezda = [["." for _ in range(size)] for _ in range(size)]
    
    middle = size // 2
    
    for i in range(size):
        zvezda[i][i] = "*"
        zvezda[i][size - i - 1] = "*"
        zvezda[middle][i] = "*"
        zvezda[i][middle] = "*"
        
    for i in zvezda:
        print("  ".join(i))
    print('Нажмите ESC для выхода')
    while True:
        key = keyboard.read_key()
        if key == 'esc':
            time.sleep(0.1)
            break
    
def squad_ris():
    os.system('cls')
    size = int(input('Введите число не превышающее 29\n'))
    os.system('cls')
    
    if size > 29:
        os.system('cls')
        print("Размер не должен превышать 29")
        time.sleep(1)
        return
    squad = [["." for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        squad[i][size-1] = "*"
        squad[0][i] = "*"
        squad[i][0] = '*'
        squad[size-1][i] = "*"
        
    for i in squad:
        print("  ".join(i))
        
    print('Нажмите ESC для выхода')
    while True:
        key = keyboard.read_key()
        if key == 'esc':
            time.sleep(0.1)
            break
        
def treugol_ris():
    os.system('cls')
    size = int(input('Введите число не превышающее 29\n'))
    os.system('cls')
    if size % 2 == 0:
        os.system('cls')
        print("Размер должен быть нечетным")
        time.sleep(1)
        return
    if size > 29:
        os.system('cls')
        print("Размер не должен превышать 29")
        time.sleep(1)
        return
    middle = size//2
    
    treugol = [["." for _ in range(size)] for _ in range(size//2+1)]
    treugol[middle][size-1] = '*'
    
    for i in range(middle):
        treugol[i][middle - i] = "*"
        treugol[i][middle + i] = '*'
        treugol[middle][i] = '*'
        treugol[middle][middle+i] = '*' 
        
    for i in treugol:
        print('  '. join(i))
    print('Нажмите ESC для выхода')
    while True:
        key = keyboard.read_key()
        if key == 'esc':
            time.sleep(0.1)
            break
        
def romb_ris():
    
    os.system('cls')
    size = int(input('Введите нечетное число не превышающее 29\n'))
    os.system('cls')
    middle = size//2
    romb = [["." for _ in range(size)] for _ in range(size)]
    romb[middle][size-1] = '*'
    romb[middle][0] = '*'
    
    for i in range(size):
        if i < middle:
            romb[i][middle-i] = '*'
            romb[i][middle+i] = '*'
        elif i > middle:
            romb[i][i - middle] = "*"
            romb[i][size-i+middle-1] = '*'
        
    for i in romb:
        print('  '. join(i))
    print('Нажмите ESC для выхода')
    while True:
        key = keyboard.read_key()
        if key == 'esc':
            time.sleep(0.1)
            break
        
def enter():
    time.sleep(0.5)
    while True:
        os.system('cls')
        print('1. Рисовать звезду\n2. Рисовать квадрат\n3.Рисовать треугольник\n4.Рисовать ромб\nESC.Выход')
        key = keyboard.read_key()  # Ждем нажатия клавиши
        if key == '1':
            zvezda_ris()
        elif key == '2':
            squad_ris()
        elif key == '3':
            treugol_ris()
        elif key == '4':
            romb_ris()
        elif key == 'esc':            
            os.system('cls')
            print('Выход')
            time.sleep(0.5)
            break
        else:
            os.system('cls')
            print("Неверный выбор. Попробуйте снова.")
            time.sleep(0.5)
        time.sleep(0.1)    
enter()
os.system('cls')
