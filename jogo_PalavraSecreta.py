palavra = 'Inovação'
letras_acertadas = ''
repeticoes = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    repeticoes += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue
    
    if letra_digitada in palavra:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            
        else:
            palavra_formada += '*'
        
    print(palavra_formada)

    if palavra_formada == palavra:
        print('PARABÉNS!! VOCÊ GANHOU')
        print('A palavra era ', palavra)
        print('Tentativas: ', repeticoes)
        letras_acertadas = ''
        repeticoes = 0