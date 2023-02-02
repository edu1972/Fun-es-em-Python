
#FUNÇÃO MÁXIMO

def maximo(x , y):
    if x > y:
        print(x)
    else:
        print(y)


#FUNÇÃO DE TESTE

def num(var):
    var = (var % 2)==0 #resto da divisão
    print(var)


#FUNÇÃO DEFINE NÚMERO PRIMO

def valor(var):
    var = (var % 2) or (var == 2) #condicional de definição
    if var >= 1:
        print("é primo")
    else:
        print("não é primo")


#FUNÇÃO DEFINE MAIOR PRIMO

def maior_primo(num):
    var = (var % 2) or (var == 2)
    if var >= 1: # é primo
        print(var)
    else:
        print("desenvolva o resto")
        
