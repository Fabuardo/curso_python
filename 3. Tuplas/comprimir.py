
lista = [1,2,3,4,5,6,7,8,9]
tupla = (10,20,30,40,50,60,70,80)
lista2 = [100,200,300,400,500,600,700,800]

resultado = zip(tupla, lista, lista2) # -> se comprime datos 
resultado = tuple(resultado)
print(resultado)