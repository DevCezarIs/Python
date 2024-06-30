def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("esta acontecendo algo antes")
        funcao(*args, **kwargs)
        print("cabou")

    return envelope
    
@meu_decorador
def ola(nome):
    print(f"ola {nome}")

ola("Cezar")


