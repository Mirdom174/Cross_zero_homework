Field = [[' ', 0, 1, 2],
         [0, '-', '-', '-'],
         [1, '-', '-', '-'],
         [2, '-', '-', '-']]


def print_field(some_field):
    for row in some_field:
        for element in row:
            print(f"{element}", end="  ")
        print()


def check_input(a):
    if a.isdigit():
        a = int(a)
        if a < 0 or a > 2:
            print('Вы ошиблись! Строки пронумерованы слева, столбцы сверху от 0 до 2.')
            print_field(Field)
            return False
    else:
        print('Вы ошиблись! Строки пронумерованы слева, столбцы сверху от 0 до 2.')
        print_field(Field)
        return False
    return True


def check_double_input(a, b):
    if Field[int(a) + 1][int(b) + 1] == '-':
        return True
    else:
        print('Здесь нельзя поставить!')
        print_field(Field)
        return False


def cross_motion():
    cross_motion_line = input('Ходят крестики! Введите строку, где хотите поставить крестик.')
    if check_input(cross_motion_line):
        cross_motion_column = input('Введите столбец, где хотите поставить крестик.')
        if check_input(cross_motion_column):
            if check_double_input(cross_motion_line, cross_motion_column):
                Field[int(cross_motion_line) + 1][int(cross_motion_column) + 1] = 'X'
            else:
                cross_motion()
        else:
            cross_motion()
    else:
        cross_motion()


def zero_motion():
    zero_motion_line = input('Ходят нолики! Введите строку, где хотите поставить нолик.')
    if check_input(zero_motion_line):
        zero_motion_column = input('Введите столбец, где хотите поставить нолик.')
        if check_input(zero_motion_column):
            if check_double_input(zero_motion_line, zero_motion_column):
                Field[int(zero_motion_line) + 1][int(zero_motion_column) + 1] = '0'
            else:
                zero_motion()
        else:
            zero_motion()
    else:
        zero_motion()


def row_chek(check_field):
    for row in check_field:
        count = 0
        Past_el = '-'
        for element in row:
            if element == Past_el:
                count += 1
            if count == 2:
                if element == 'X':
                    print_field(Field)
                    print('Крестики выиграли!')
                    return True
                elif element == '0':
                    print_field(Field)
                    print('Нолики выиграли!')
                    return True
            Past_el = element


def check_win():
    if row_chek(Field):
        return True
    elif row_chek(rotate_matrix(Field)):
        return True
    elif (
            Field[1][1] == Field[2][2] and Field[2][2] == Field[3][3] or
            Field[1][3] == Field[2][2] and Field[2][2] == Field[3][1]
    ):
        if Field[2][2] == 'X':
            print_field(Field)
            print('Крестики выиграли!')
            return True
        elif Field[2][2] == '0':
            print_field(Field)
            print('Нолики выиграли!')
            return True


def rotate_matrix(matrix):
    rotated_matrix = [[matrix[j][i] for j in range(4)] for i in range(4)]
    return rotated_matrix


def draw():
    for row in Field:
        for element in row:
            if element == '-':
                return False
    return True
def game():
    for step in range(5):
        print_field(Field)
        cross_motion()
        if check_win():
            break
        if draw():
            print_field(Field)
            print('Ничья!')
            break
        print_field(Field)
        zero_motion()
        if check_win():
            break

game()
