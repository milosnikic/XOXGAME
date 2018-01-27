'''
** Simulacija popularne igrice 'iks-oks'
**
**          o | x | o
**          o | o | x
**          o | x | x
**
**  Pobednik je takmicar koji uspe da spoji tri karaktera u nizu
**  bilo da je u redu, koloni ili po dijagonali. Potrebno je uneti indexe
**  pozicija na koje zelimo staviti element.
**          ***POZICIJE KRECU OD 1 do 3***
** NPR. x,y = input('Unesite poziciju na koju zelite da stavite X: ')
**      Unesite poziciju na koju zelite da stavite X: 1 1
**
**
**
**  Programski jezik koji je koriscen je Python
**
**  Program je testiran u Linux OS.
'''
import os
'''
Dimenzije matrice 3x3
'''
w, h = 3, 3
MATRICA = [[-1 for x in range(w)] for y in range(h)]

def print_matrix():
    global MATRICA
    for i in range(len(MATRICA)):
        for j in range(len(MATRICA[i])):
            if MATRICA[i][j] == -1 and j != len(MATRICA[i])-1:
                print(u'\u229E' + ' | ',end='')
            elif MATRICA[i][j] == -1 and j == len(MATRICA[i])-1:
                print(u'\u229E'+ ' ',end='')
            elif MATRICA[i][j] != -1 and j != len(MATRICA[i])-1:
                print(MATRICA[i][j] + ' | ',end='')
            elif MATRICA[i][j] != -1 and j == len(MATRICA[i])-1:
                print('' + MATRICA[i][j],end='')
        print()
def unos(param):
    try:
        l = input('Unesite poziciju na koju zelite da stavite '+ param +': ').split()
        i, j = [int(x)-1 for x in l]
        while MATRICA[i][j] != -1:
            print('Dato polje nije prazno.')
            print_matrix()
            l = input('Unesite poziciju na koju zelite da stavite '+ param + ':').split()
            i, j = [int(x)-1 for x in l]
    except KeyboardInterrupt:
        os.system('clear')
        print_matrix()
        unos(param)
    return i, j

def fill():
    k = 0
    global MATRICA
    while k < 9:
        print_matrix()
        if k % 2 == 0:
            i, j = unos('X')
            MATRICA[i][j] = 'X'
        else:
            i, j = unos('O')
            MATRICA[i][j] = 'O'
        win = is_over()
        if win != False:
            break
        k += 1
    print_matrix()
    if k == 9:
        print('Rezultat je neresen.')
    else:
        print('Pobednik je ' + win + ' takmicar.')

def is_over():
    row = check_rows()
    col = check_columns()
    diag = check_diags()
    if row != False:
        return row
    if col != False:
        return col
    if diag != False:
        return diag
    return False

def check_rows():
    for i in range(len(MATRICA)):
        if MATRICA[i][0]=='X' and MATRICA[i][1]=='X' and MATRICA[i][2]=='X':
            return MATRICA[i][0]
        if MATRICA[i][0]=='O' and MATRICA[i][1]=='O' and MATRICA[i][2]=='O':
            return MATRICA[i][0]
    return False

def check_columns():
    for i in range(len(MATRICA)):
        if MATRICA[0][i]=='X' and MATRICA[1][i]=='X' and MATRICA[2][i]=='X':
            return MATRICA[0][i]
        if MATRICA[0][i]=='O' and MATRICA[1][i]=='O' and MATRICA[2][i]=='O':
            return MATRICA[0][i]
    return False

def check_diags():
    x , o = 0, 0
    for i in range(len(MATRICA)):
        if MATRICA[i][i] == 'X':
            x += 1
        if MATRICA[i][i] == 'O':
            o += 1
    if x == 3 or o == 3:
        return MATRICA[i][i]

    x , o = 0, 0
    for i in range(len(MATRICA)):
        for j in range(len(MATRICA[i])):
            if i + j == 2 and MATRICA[i][j] == 'X':
                x += 1
            if i + j == 2 and MATRICA[i][j] == 'O':
                o += 1
    if x == 3 or o == 3:
        return MATRICA[1][1]
    return False

if __name__ == '__main__':
    fill()
    # print_matrix()
