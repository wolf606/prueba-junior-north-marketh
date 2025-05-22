def numero_mas_frecuente(lista):
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return lista[0]

    min_num = 0
    max_frecuencia = 0
    frecuencia = {}
    for num in lista:
        frecuencia[num] = frecuencia.get(num, 0) + 1
        if frecuencia[num] > max_frecuencia:
            max_frecuencia = frecuencia[num]
            min_num = num

    for num, freq in frecuencia.items():
        if freq == max_frecuencia and num < min_num:
            min_num = num
    return min_num

assert numero_mas_frecuente([1, 3, 1, 3, 2, 1]) == 1
assert numero_mas_frecuente([4, 4, 5, 5]) == 4
assert numero_mas_frecuente([5, 5, 4, 4]) == 4
assert numero_mas_frecuente([5, 6, 5, 4, 5, 4, 6, 4]) == 4
assert numero_mas_frecuente([1, 2]) == 1
assert numero_mas_frecuente([2, 1]) == 1
assert numero_mas_frecuente([3, 2, 1]) == 1
print("Todos los tests pasaron")