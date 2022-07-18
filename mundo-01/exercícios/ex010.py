real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.44
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))