# criar um programa que mede o ponto da carne de acordo com a temperatura da mesma

""" selada = 48
mal_passada = 54
ao_ponto = 60
bem_passada = 65
queimada = 71 """

temperatura_da_carne = int(input('qual a temepratura da carne?'))
if temperatura_da_carne <= 48:
    print('crua')
elif temperatura_da_carne in range(49, 53):
    print('selada')
elif temperatura_da_carne in range(54, 59):
    print('mal passada')
elif temperatura_da_carne in range(60, 64):
    print('ao ponto')
elif temperatura_da_carne in range(65, 70):
    print('mal passada')
elif temperatura_da_carne >= 71:
    print('queimada')