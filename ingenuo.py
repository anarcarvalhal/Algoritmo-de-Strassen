def metodo_ingenuo(A, B):
    
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])

    if colunas_A != linhas_B:
        raise ValueError("Para realizar a multiplicação, o número de colunas de A deve ser igual ao número de linhas de B.")
    
    # Cria uma matriz C com as dimensões do produto preenchida com zeros
    C = []
    for _ in range(linhas_A):
        linha = []
        for _ in range(colunas_B):
            linha.append(0)
        C.append(linha)

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]

    return C