def calculadora():
    while True:
        print("calculadora simples")
        print()
        print("1.soma")
        print("2.subtracao")
        print("3.multiplicacao")
        print("4.divisao")
        print("s. Sair")
        operacao = input("Selecione uma opçaõ ou 's' para sair: ")

        if operacao == 's' or operacao == 'S':
            print("Obrigada por utilizar o calculo simples!")
            break

        if operacao not in ['1','2','3','4']:
            print("Opção inválida! tente novamente!")
            continue

        numero_1 = float(input("Primeiro número: "))
        numero_2 = float(input("SEGUNDO NÚMERO: "))

        if operacao == '1':
            resultado = numero_1 + numero_2
            print("resultado da operação da soma é: ", resultado)
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("resultado da operação da subtração é: ", resultado)
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("resultado da operação da multiplicação é: ", resultado)
        else:
            if numero_2 == 0:
                print("divisões por zero não são possiveis. tente novamente!")
                continue
            else:
                resultado = numero_1 / numero_2
            print("o resultado da operação de divisão é: ", resultado)

calculadora()

