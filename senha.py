minha_senha = int(9194)

def verificar_senha(nova_senha):
    if len(nova_senha) >= minha_senha:
        print("valida")
    else:
        print("invalida")