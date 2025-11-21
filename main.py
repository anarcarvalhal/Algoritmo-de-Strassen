import random
from utils import pad, imprimir_matriz, checar_resultado, unpad_matrix, ler_matriz_do_usuario
from strassen import metodo_strassen 
from ingenuo import metodo_ingenuo 
# ==============================================================================
#                             FUNÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    while True:
        choice = input("\nEscolha o modo: (1) Digitar matrizes | (2) Gerar aleatoriamente (Teste Rápido): ")
        if choice in ['1', '2']:
            break
        print("Opção inválida.")
        
    if choice == '1':
        while True:
            try:
                N_ORIG = int(input("Digite o tamanho N (ex: 4 ou 6) para as matrizes N x N: "))
                if N_ORIG < 2:
                    print("O tamanho deve ser maior ou igual a 2.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
                
        A_orig = ler_matriz_do_usuario(N_ORIG, "A")
        B_orig = ler_matriz_do_usuario(N_ORIG, "B")
        
    else:
        N_ORIG = random.randint(2, 8)
        A_orig = [[random.randint(1, 10) for _ in range(N_ORIG)] for _ in range(N_ORIG)]
        B_orig = [[random.randint(1, 10) for _ in range(N_ORIG)] for _ in range(N_ORIG)]

    C_naive = metodo_ingenuo(A_orig, B_orig)

    # Padding para Strassen
    A_pad, N_pad = pad(A_orig)
    B_pad, _ = pad(B_orig)
    
    C_strassen_pad = metodo_strassen(A_pad, B_pad)
    C_strassen_final = unpad_matrix(C_strassen_pad, N_ORIG) 

    print(f"\n==================================================")
    print(f"      ALGORITMO DE STRASSEN (N={N_ORIG})")
    print(f"====================================================")

    if N_pad != N_ORIG:
        print(f"Matrizes preenchidas com zero para o tamanho {N_pad}x{N_pad} para o Strassen.")
    
    imprimir_matriz(A_orig, "Matriz A Original")
    imprimir_matriz(B_orig, "Matriz B Original")
    
    print("\n--- RESULTADO NAIVE (O(N³)) ---")
    imprimir_matriz(C_naive)
    
    print("\n--- RESULTADO STRASSEN (O(N²·⁸¹)) ---")
    imprimir_matriz(C_strassen_final)
    
   
    if checar_resultado(C_naive, C_strassen_final):
        print("\nVERIFICAÇÃO FINAL: Resultados Strassen e Naive são idênticos.")
    else:
        print("\nVERIFICAÇÃO FINAL: Foram encontradas diferenças nos resultados. Confira a lógica do Strassen.")

