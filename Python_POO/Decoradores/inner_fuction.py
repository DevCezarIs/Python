def calculadora(operação):
    
    def somar(a,b):
        return a+b
     
    def sub(a,b):
        return a-b

    match operação:
        case "+":
            return(somar)
        
        case "-":
            return(sub)

hehe = calculadora("+")(5 , 6)
print(hehe)
