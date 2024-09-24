def mul(list A, list B):
    """
    Умножение двух матриц, представленных списками в Python.
    """
    # Получаем размеры матриц
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # Проверяем, что количество столбцов первой матрицы равно количеству строк второй матрицы
    if cols_A != rows_B:
        raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")

    # пустая мтарица
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]


    cdef int i, j, k
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

