def calculadora(operação):
      
    def somar(a,b):
          return a+b
      
    def sub(a,b):
          return a-b
      
    def div(a,b):
          return a/b
      
    def mult(a,b):
          return a*b

    match operação:
        case "+":
            return(somar)
          
        case "-":
            return(sub)
          
        case "*":
            return(mult)
          
        case "/":
            return(div)

a = calculadora("+")(5, 6)
print(a)       