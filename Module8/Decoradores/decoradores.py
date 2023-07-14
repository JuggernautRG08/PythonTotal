def decorar_saludi(funcion):
    def otra_funcion(palabra):
        print ("Otra funcion")
        funcion(palabra)
        print ("Otra funcion --")
        return otra_funcion
def uppercase(text):
    print(text.upper())
def lowercase(text):
    print(text.lower())


mayuscula_decorada= decorar_saludi(uppercase)

uppercase('asbdasbnmssd')
