#Módulo 4 - Repetição

# 2. Transforme em código o fluxograma a seguir

def contagem_fluxograma():
    # Leitura do valor N
    try:
        n = int(input("Leia n: Digite um valor inteiro para N: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    # Inicializa 'cont' com 0
    cont = 0

    # Estrutura de Repetição (While)
    # O loop continua enquanto 'n < cont' for FALSO (o 'Não' do fluxograma).
    # Ou seja, o loop executa ENQUANTO n >= cont.
    while n >= cont:
        # cont = cont + 1
        cont = cont + 1

        # Imprime cont
        print(cont)
        
        # O loop então volta para a checagem 'n >= cont'
    
    # Após o loop (quando n < cont for VERDADEIRO, o 'Sim' do fluxograma)
    print("Fim")


