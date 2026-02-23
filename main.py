"""
    Tabuada automática

    Peça um número e mostre a tabuada dele de 1 a 10."""


numero = int(input("Digite um numero de 1 a 10  para ter a tabuada dele: "))
contador = 0


while contador  <= 10: # enquanto o contador for menor ou igual a dez faça...
    resultado = (numero * contador) # criei uma variavel resultado para receber o resultado de numero * contador
    print(numero, "x", contador, "=",  resultado) # print na tela o numero digitado * o contador = resultado
    contador = contador + 1 # no contador cada hora que passa aumenta um 
print("Fim da Tabuada!")


""" 
    Dificuladaes: Usar while, saber a ordem para organizar o contador.
    
"""