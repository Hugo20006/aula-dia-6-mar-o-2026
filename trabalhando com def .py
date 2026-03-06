numero1= float(input(" Digite o primeiro número: "))
numero2= float(input(" Digite o segundo número: "))
print("Escolha a operação: ")
print("1 - adicao\n", print("2 - Subtração\n"), print("3 - Multiplição\n"), print("4 - Divisao\n", print("5 - Potência")))
operacão = input("Digite o número da operacão desejada: ")
def adicao (a, b):
      return a + b
def subtracao (a, b):
      return a - b
def multiplicacao (a, b):
      return a * b
def divisao (a, b):
      return a / b
def potencia (a, b):
      return a ** b
if operacão == "1":
   print("resultado:", adicao(numero1, numero2))
elif operacão== "2:":
   print("resultado", subtracao(numero1,numero2))
elif operacão == "3":
   print("resultado:", multiplicacao(numero1, numero2))
elif operacão == "4":
   print("resultado:", divisao(numero1, numero2))
elif operacão == "5":
   print("resultado:", potencia(numero1, numero2))
else:
   print("Não achei a operacão desejada")

