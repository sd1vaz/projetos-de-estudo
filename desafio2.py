#criar um programa que calcula a quantidade de tinta nescessaria para pintar uma pareede. o usuario devera fornecer as seguintes informaçoes: Rendimento, altura e largura.
#o programa deve mostrar na tela a mensagem de "voce nescessita de x de tinta "







rendimento = int(input('informe o rendimento da tinta em m²:'))
altura = int(input('qual a altura da parede?'))
largura = int(input('qual a largura da parede?'))

def tinta_nescessaria ():
    litrostinta = int(altura * largura / rendimento)
    print (f'voce precisa de {litrostinta} litros de tinta')

tinta_nescessaria()