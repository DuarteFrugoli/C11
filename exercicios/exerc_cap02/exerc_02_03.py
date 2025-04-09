while True:
    escolha = input('você é homi ou cuié? (H - homi / M - Cuié): ')

    if escolha.upper() == 'H':
        print('parabéns você é homi')
        break
    if escolha.upper() == 'M':
        print('parabéns você é cuié')
        break
    
    print('escolha inválida')