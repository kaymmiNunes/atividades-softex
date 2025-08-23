n1 = float(input("\nDigite o primeiro número: "))
n2 = float(input("\nDigite o segundo número número: "))
op = int(input("\nDigite 1 para soma\
           Digite 2 para subtração\
           Digite 3 para divisão\
           Digite 4 para multiplicação\
           \nOperação: "))

def somar(n1,  n2):
   return n1 + n2

def subtrair(n1,  n2):
   return n1 - n2

def dividir(n1,  n2):
   return n1 / n2

def multiplicar(n1,  n2):
   return n1 * n2

if op == 1:
    print(f"O resultado da soma é {somar(n1, n2)}")

if op == 2:
    print(f"O resultado da subtração é {subtrair(n1, n2)}")

if op == 3:
    print(f"O resultado da divisão é {dividir(n1, n2)}")

if op == 4:
    print(f"O resultado da multiplicação é {multiplicar(n1, n2)}")
