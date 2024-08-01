print('Calculo de IMC')
print('-' * 14)

def imc(dados):
    resultado = dados[1]/(dados[0] ** 2)
    return resultado

dados = list(map(float, input('Altura e Peso: ').split()))
total = imc(dados)

print('-' * 14)
print(f'IMC: {total:.2f}')
print('-' * 14)
print('Classificação de IMC')
print('-' * 14)

if total < 18.5:
    print('Abaixo do peso normal')
    print('-' * 14)
elif 18.5 < total < 24.9:
    print('Peso normal')
    print('-' * 14)
elif 25.0 < total < 29.9:
    print('Excesso de peso')
    print('-' * 14)
elif 30.0 < total < 34.9:
    print('Obesidade classe I')
    print('-' * 14)
elif 35.0 < total < 39.9:
    print('Obesidade classe II')
    print('-' * 14)
else:
    print('Obesidade clase III')
    print('-' * 14)
