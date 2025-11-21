import math

# ==============================================================================
#              FUNÇÕES ÚTEIS PARA O ALGORITMO DE STRASSEN
# ==============================================================================
#  
def soma_matrizes(A, B):

    linhas = len(A)
    colunas = len(A[0])

    if linhas != len(B) or colunas != len(B[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem somadas.")

    soma = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(A[i][j] + B[i][j])
        soma.append(linha)

    return soma


def subtrai_matrizes(A, B):

    linhas = len(A)
    colunas = len(A[0])

    if linhas != len(B) or colunas != len(B[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões para serem subtraídas.")

    diferenca = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(A[i][j] - B[i][j])
        diferenca.append(linha)

    return diferenca


def dividir_matriz(M):

    n = len(M)
    meio = n // 2

    A11, A12, A21, A22 = [], [], [], []

    for i in range(n):
        linha_esq = M[i][:meio]
        linha_dir = M[i][meio:]

        if i < meio:
            A11.append(linha_esq)
            A12.append(linha_dir)
        else:
            A21.append(linha_esq)
            A22.append(linha_dir)
    return A11, A12, A21, A22



def juntar_matriz(C11, C12, C21, C22):
    C = []
    for i in range(len(C11)):
        C.append(C11[i] + C12[i])
    for i in range(len(C21)):
        C.append(C21[i] + C22[i])
    return C

# ==============================================================================
#                                FUNÇÕES DE SUPORTE
# ==============================================================================

def ler_matriz_do_usuario(tamanho, nome):
    """
    Lê uma matriz de tamanho N x N digitada pelo usuário.
    """
    M = []
    print(f"\n--- Digite a Matriz {nome} ({tamanho}x{tamanho}) ---")
    for i in range(tamanho):
        while True:
            try:
                # Recebe a linha do usuário, separa por espaço e converte para float
                linha_str = input(f"Linha {i+1} (Separe os {tamanho} números por espaço): ").strip().split()
                linha = [int(x) for x in linha_str]
                
                if len(linha) != tamanho:
                    print(f"Erro: Você deve digitar exatamente {tamanho} números.")
                    continue
                M.append(linha)
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números.")
    return M

def checar_resultado(C1, C2):
    
    n = len(C1)
    for i in range(n):
        for j in range(n):
            # Usando uma tolerância pequena para lidar com erros de ponto flutuante
            if abs(C1[i][j] - C2[i][j]) > 1e-9: 
                print(f"ERRO DE CORREÇÃO em C[{i}][{j}]: Strassen = {C2[i][j]:.4f} | Ingênuo = {C1[i][j]:.4f}")
                return False
    return True


def get_padded_size(n):
    """Calcula o próximo tamanho que é potência de 2."""
    if n > 0 and (n & (n - 1) == 0): # Verifica se já é potência de 2
        return n
    return 2**math.ceil(math.log2(n))


def pad(M):
    n_orig = len(M)
    n_pad = get_padded_size(n_orig)
    
    if n_orig == n_pad:
        return M, n_pad
    
    # Cria uma nova matriz preenchida com zeros
    M_padded = [[0 for _ in range(n_pad)] for _ in range(n_pad)]
    
    # Copia os valores originais
    for i in range(n_orig):
        for j in range(n_orig):
            M_padded[i][j] = M[i][j]
            
    return M_padded, n_pad

def unpad_matrix(M_padded, n_orig):
    """
    Remove o padding de uma matriz preenchida, retornando-a ao tamanho original.
    """
    return [linha[:n_orig] for linha in M_padded[:n_orig]]


def imprimir_matriz(M, name=None): # Adiciona 'name' como argumento opcional
    if name:
        print(f"\n--- {name} ({len(M)}x{len(M[0])}) ---")
    # Imprime a matriz
    for linha in M:
        print("  ".join(f"{x:10d}" for x in linha)) 

