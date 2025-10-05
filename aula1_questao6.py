# questao_6

def main():
    # Lê a quantidade de experimentos
    while True:
        try:
            N = int(input("Digite a quantidade de experimentos: "))
            if N <= 0:
                print("Por favor, digite um número positivo.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número inteiro.")

    # Inicializa os contadores
    total_cobaias = 0
    sapos = 0
    ratos = 0
    coelhos = 0

    # Lê os experimentos e atualiza os contadores
    for i in range(N):
        while True:
            try:
                quantia, tipo = input(f"Digite a quantidade e o tipo de cobaia do experimento {i+1} (ex: 10 S): ").split()
                quantia = int(quantia)
                if quantia < 0:
                    print("Por favor, digite uma quantidade não negativa.")
                elif tipo.upper() not in ['S', 'R', 'C']:
                    print("Por favor, digite um tipo de cobaia válido (S, R ou C).")
                else:
                    break
            except ValueError:
                print("Por favor, digite uma quantidade e um tipo de cobaia válidos.")
        
        total_cobaias += quantia
        
        if tipo.upper() == 'S':
            sapos += quantia
        elif tipo.upper() == 'R':
            ratos += quantia
        elif tipo.upper() == 'C':
            coelhos += quantia

    # Calcula os percentuais
    percentual_sapos = (sapos / total_cobaias) * 100
    percentual_ratos = (ratos / total_cobaias) * 100
    percentual_coelhos = (coelhos / total_cobaias) * 100

    # Imprime os resultados
    print(f"Total: {total_cobaias} cobaias")
    print(f"Total de sapos: {sapos}")
    print(f"Total de ratos: {ratos}")
    print(f"Total de coelhos: {coelhos}")
    print(f"Percentual de sapos: {percentual_sapos:.2f} %")
    print(f"Percentual de ratos: {percentual_ratos:.2f} %")
    print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")

if __name__ == "__main__":
    main()
