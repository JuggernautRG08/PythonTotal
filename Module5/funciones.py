def chequear_tres_cifras(numero):
    return numero in range(100,1000)
resultado = chequear_tres_cifras(58)
print (resultado)

precio_cafe=[('Capuchinno',2.1),('Cafe',3.50),('Expresso',1.5)]
# for elemento in precio_cafe:
#     print (elemento)

def calcula_cafe_mas_caro(lista_precios):
    preciomayor=0
    cafemascaro=''
    for cafe,precio in lista_precios:
        if precio > preciomayor:
            preciomayor = precio
            cafemascaro = cafe
            print('Entro')
        else:
            pass

        return(cafemascaro,preciomayor)

print(calcula_cafe_mas_caro(precio_cafe))
