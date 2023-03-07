#calculadora de imc 
#calculo de massa corporal = peso / (altura * altura)







peso = float(input('qual é o seu peso?'))
altura = float(input('qual é a sua altura em cm?'))
imc = peso / (altura/100)**2
print(imc)
if imc < 18.5:
    print('magreza')
elif imc >= 18.5 and imc < 24.9:
    print("normal")
elif imc >= 25.0 and imc < 29.9:
    print("acima do peso")
elif imc >= 30.0 and imc <39.9:
    print("obesidade")
else:
    print('OBESIDADE GRAVE') 