#criar um programa que gera 3 listas de acorda com as nescessidades
# lista1 = funcionarios que tem carros e trabalham a noite 
# lista2 = funcionarios que tem carro e trabalham de dia 
# lista3 = funcionarios que nao tem carro 





funcionarios = [ 'ana', 'marcos', 'alice', 'pedro', 'sophia', 'Bruno', 'Melissa']
turno_dia = ['ana', 'marcos','alice','Melissa'  ]
turno_noite = [ 'pedro', 'sophia',  'Bruno' ]
tem_carro = ['marcos','alice', 'Bruno', 'Melissa' ]

funcionarios= set(funcionarios)
turno_dia = set (turno_dia )
turno_noite = set(turno_noite)
tem_carro = set(tem_carro )

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)
lista3 = set(funcionarios) - (tem_carro)
print(lista3)