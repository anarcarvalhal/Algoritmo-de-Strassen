from utils import soma_matrizes, subtrai_matrizes, dividir_matriz, juntar_matriz
from ingenuo import metodo_ingenuo

THRESHOLD = 2

def metodo_strassen(A, B):
    
    n = len(A)

    if n != len(A[0]) or n != len(B) or n != len(B[0]):
        raise ValueError("As matrizes devem ser quadradas.")

    if n <= THRESHOLD:
        return metodo_ingenuo(A, B)

    A11, A12, A21, A22 = dividir_matriz(A)
    B11, B12, B21, B22 = dividir_matriz(B)

    P1 = metodo_strassen(soma_matrizes(A11, A22), soma_matrizes(B11, B22))
    P2 = metodo_strassen(soma_matrizes(A21, A22), B11)
    P3 = metodo_strassen(A11, subtrai_matrizes(B12, B22))
    P4 = metodo_strassen(A22, subtrai_matrizes(B21, B11))
    P5 = metodo_strassen(soma_matrizes(A11, A12), B22)
    P6 = metodo_strassen(subtrai_matrizes(A21, A11), soma_matrizes(B11, B12))
    P7 = metodo_strassen(subtrai_matrizes(A12, A22), soma_matrizes(B21, B22))

    C11 = soma_matrizes(subtrai_matrizes(soma_matrizes(P1, P4), P5), P7)
    C12 = soma_matrizes(P3, P5)
    C21 = soma_matrizes(P2, P4)
    C22 = soma_matrizes(subtrai_matrizes(soma_matrizes(P1, P3), P2), P6)

    resultado = juntar_matriz(C11, C12, C21, C22)

    return resultado

    
   