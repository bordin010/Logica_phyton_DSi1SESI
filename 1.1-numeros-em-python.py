# AULA COMPLETA: NUMEROS EM PYHTON

"""
Vamos aprender:
1 - Tipos numéricos
2 - Conversões de tipos
3 - Hierarquia numérica
4 - Operações matemáticas
5- Coerção de tipos
6 - verificação de tipos
7 - Entrada de dados
"""
#============================
## PASSO 01 - TIPOS NUMÉRICOS
#============================
# int  -> números inteiros
# float -> números com casas decimais
# complex -> números complexos (usado em matemática/engenharia)

print("--TIPOS NUMÉRICOS--")

# EXEMPLO 01 - NÚMERO INTEIRO

# criamos uma variável chamada numero_inteiro
numero_inteiro = 10

# Mostramos o valor
print("Valor:", numero_inteiro)

# Type() mostra qual é o tipo da variável
print("Tipo:", type(numero_inteiro))

print("----------------------------")

# EXEMPLO 02 - NUMERO DECIMAL

# Criamos uma variável chamada numero_decimal
numero_decimal = 3.14

# Mostramos o valor
print("Valor:", numero_decimal)

print("Tipo:", type(numero_decimal))

print("----------------------------")

# EXEMPLO 03 - NUMEROS COMPLEXOS
# UM NUMERO COMPLEXO POSSUI DUAS PARTES:
# PARTE REAL (NUMERO NORMAL)
# PARTE IMAGINÁRIA (MULTIPLICADA POR J)

# ESTRUTURA GERAL:
# NUMERO = A + BJ

# A = PARTE REAL
# B = PARTE IMAGINARIA
# J = UNIDADE IMAGINARIA

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)

print("Tipo", type(numero_complexo))

# EXEMPLO 03 - ACESSAR CADA PARTE DO NÚMERO

# .real retorna a parte real
print ("Parte Real:", numero_complexo.real)

# .imag retorna a parte imaginária
print ("Parte imaginária:", numero_complexo.imag)

# apenas para separar visualmente a saída no terminal
print("\n\n")

#==============================
## PASSO 02 - CONVERSÃO TIPO
#==============================

## Exemplo Clássico:
## Dados vindos do usuário são texto (string), muitas vezes é necessário converter eles.

print("===== Conversões =====")

# float -> int

valor = int(3.9)

print("int(3.9):", valor)
print("Tipo", type(valor))

# string -> int
valor1= "10"
print(type(valor1))

valor2 = int("10")
print("tipo:", type(valor2))

#int -> float
valor3 = float(10)
print("float(10)", valor3)
print("Tipo:", type(valor3))