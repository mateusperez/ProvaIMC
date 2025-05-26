nome = str (input('Digite o nome do paciente: '))
peso = float(input('Digite o peso do paciente: '))
altura = float(input('Digite a altura do paciente: '))

imc = peso / (altura*altura)
if imc < 18.5:
    categoria = 'abaixo do peso'
elif imc < 24.9:
    categoria = 'peso normal'
elif imc < 29.9:
    categoria = 'sobrepeso'
elif imc < 34.9:
    categoria = 'obesidade grau I'
elif imc < 39.9:
    categoria = 'obesidade grau II'
else:
    categoria = 'obesidade grau III'

print(nome,' tem o imc igual a', imc,' que está classificado como ', categoria)