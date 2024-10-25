import numpy as np


def print_matrix(matrix):
    print(np.array(matrix))


def add_matrices(matrix1, matrix2):
    return matrix1 + matrix2


def subtract_matrices(matrix1, matrix2):
    return matrix1 - matrix2


def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)


def input_matrix(matrix_number):
    rows = int(input(f"Введите количество строк матрицы {matrix_number}: "))
    cols = int(input(f"Введите количество столбцов матрицы {matrix_number}: "))
    matrix = []

    print(f"Введите элементы матрицы {matrix_number}:")
    for i in range(rows):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)

    return np.array(matrix), rows, cols


def matrix_calculator():
    matrix1, rows1, cols1 = input_matrix(1)
    matrix2, rows2, cols2 = input_matrix(2)

    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Выход")

        choice = input("Ваш выбор: ")

        if choice == '1':
            if matrix1.shape == matrix2.shape:
                result = add_matrices(matrix1, matrix2)
                print("Результат сложения:")
                print_matrix(result)
            else:
                print("Ошибка: размеры матриц не совпадают!")

        elif choice == '2':
            if matrix1.shape == matrix2.shape:
                result = subtract_matrices(matrix1, matrix2)
                print("Результат вычитания:")
                print_matrix(result)
            else:
                print("Ошибка: размеры матриц не совпадают!")

        elif choice == '3':
            if cols1 == rows2:
                result = multiply_matrices(matrix1, matrix2)
                print("Результат умножения:")
                print_matrix(result)
            else:
                print("Ошибка: количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы!")

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор! Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    matrix_calculator()
