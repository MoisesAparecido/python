palavras = ('aprender', 'progamar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'práticar',
            'trabalhar', 'mercado', 'progamador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lowe() in 'aeiou':
            print(letra, end='')
