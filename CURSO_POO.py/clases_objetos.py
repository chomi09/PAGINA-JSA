class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    def llamar (self):
        print(f'estas llamando desde el modelo {self.modelo}')

    def cortar (self):
        print (f'cortaste la llamada desde un {self.marca}')
    
celular1 = Celular('sansung', 'S23', '48MP')
# celular2 = Celular()
# celular3 = Celular()

print(celular1.marca)



celular1.llamar()