
def get_dv(chave):

    peso_dv = [4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9,
               8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    dv_calculado = 11 - (sum([int(char) * peso_dv[i]
                              for i, char in enumerate(chave[0:43])]) % 11)

    if dv_calculado == 10 or dv_calculado == 11:

        return '0'

    else:
        return str(dv_calculado)
