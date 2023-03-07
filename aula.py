from datetime import datetime


# python Object-Oriented Programming


""" class Funcionarios:
    nome = input("qual é o seu nome ?")
    sobrenome =input ('Sobrenome?')
    data_nascimento = input('data de nascimento?')


usuario1 = Funcionarios()

print(usuario1.nome,usuario1.sobrenome)
print(usuario1.data_nascimento)  """







""" #classe
class Funcionarios:
    pass

#objeto
usuario1 = Funcionarios()
usuario2 = Funcionarios()

#parametros usuario 1 
usuario1.nome = input("qual é o seu nome ?")
usuario1.sobrenome = input ('Sobrenome?')
usuario1.nascimento = input('data de nascimento?')

#parametros usuario 2
usuario2.nome = input("qual é o seu nome ?")
usuario2.sobrenome = input ('Sobrenome?')
usuario2.nascimento = input('data de nascimento?')

print(usuario1.nome) """








""" #classe
class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = data_nascimento
        

#objeto
usuario1 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))
usuario2 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))
usuario3 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))
usuario4 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))
usuario5 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))


 #parametros usuario 1 
usuario1.nome = input("qual é o seu nome ?")
usuario1.sobrenome = input ('Sobrenome?')
usuario1.nascimento = input('data de nascimento?')

#parametros usuario 2
usuario2.nome = input("qual é o seu nome ?")
usuario2.sobrenome = input ('Sobrenome?')
usuario2.nascimento = input('data de nascimento?') 

print(usuario1.nome)
print(usuario2.nome) """





""" class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nascimento = data_nascimento
    def nome_completo(self):
        return(self.nome +  '' +  self.sobrenome)
        

#objeto
usuario1 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))
usuario2 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('data de nascimento :'))

print(usuario1.nome_completo())
print(Funcionarios.nome_completo(usuario1)) """





""" class Funcionarios:
    def __init__(self,nome,sobrenome,ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = int(ano_nascimento) 

    def nome_completo(self):
        return(self.nome +  ' ' +  self.sobrenome)
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = ano_atual - self.ano_nascimento
        return self.ano_nascimento
   
       
        
        


usuario1 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('ano de nascimento :'))
usuario2 = Funcionarios(input("nome :"), input ('Sobrenome :'), input('ano de nascimento :'))

print(Funcionarios.idade_funcionario(usuario1)) """





