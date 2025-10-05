
def encontra_maior():
    print("--- Encontra o Maior Valor ---")
    
    # Leitura de N (quantidade de números a serem lidos)
    try:
        n = int(input("Leia N: Digite quantos números você irá informar: "))
        
        # Garante que N seja positivo para o loop começar
        if n <= 0:
            print("N deve ser um número inteiro positivo.")
            return

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido para N.")
        return

    # Inicializa 'maior' com 0
    maior = 0

    # Estrutura de Repetição (Loop While)
    # O loop continua enquanto n > 0 (o 'Sim' da condição n > 0).
    while n > 0:
        # 1. Leia x
        try:
            x = float(input(f"Leia X: Digite o {n}º número: "))
        except ValueError:
            print("Erro: Por favor, digite um número válido. Reinicie.")
            return

        # 2. Estrutura Condicional: Verifica se x é maior que 'maior'
        # Se x > maior (Sim)
        if x > maior:
            # maior = x
            maior = x
            
        # O fluxograma tem uma seta que passa pelo 'Não' e continua para o próximo passo.
        
        # 3. Decrementa N (n = n - 1)
        n = n - 1
        # O código retorna automaticamente para a checagem 'n > 0'
        
    # Após o loop (quando n > 0 for FALSO, o 'Não' do fluxograma)
    
    # Imprime maior
    print("\n------------------------------")
    print(f"O maior valor digitado foi: {maior}")

# Chama a função principal para executar o algoritmo
encontra_maior()