import math

def area_retangulo(a,b):
    area = a*b
    return area

def hipotenusa(cat_a, cat_b):
    hipo = math.sqrt (cat_a**2+cat_b**2)
    return hipo

print ("Digite 1 pra calcular a área do retângulo")
print ("Digite 2 para a hipotenusa")
opcao = int(input("Sua opção: "))

if opcao == 1:
    a = float(input("Lado A: "))
    b= float (input("Lado B: "))
    resultado = area_retangulo(a,b)
    print (round(resultado,2))

elif opcao == 2:
    cat_a = float(input("Cateto de A: "))
    cat_b = float(input("Cateto de B: "))
    resultado = hipotenusa (cat_a, cat_b)
    print (round(resultado, 2))

