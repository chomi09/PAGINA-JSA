class Producto:
    def __init__(self, nombre, tipo, peso):
        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
    def mostrar (self):
        print(f'{self.nombre} {self.tipo} {self.peso}kg S/.{self.precio}')
        
class Cafe (Producto):
    def __init__(self, nombre, tipo, peso, variedad, rendimiento, humedad):
        super().__init__(nombre, tipo, peso)
        self.precio = 0
        self.variedad = variedad
        self.rendimiento = rendimiento
        self.humedad = humedad
    def seleccionar (self):
        
        print('El cafe fue seleccionado')
        while True:
            try:
                self.precio = float(input('Ingrese el precio por kilo: S/ '))
                break
            except ValueError:
                print('Ingrese un número válido')
        if self.variedad == 'catuai':
            self.precio = self.precio + 2
        elif self.variedad == 'catimor':
            self.precio = self.precio + 1
        elif self.variedad =='tupi':
            self.precio = self.precio + 0.5
            
        if self.rendimiento <= 60:
            self.precio = self.precio + 0.1
        elif 60 >= self.rendimiento <= 80:
            self.precio = self.precio + 0.2
        else:
            self.precio = self.precio + 0.3
            
        if self.humedad == 12:
            self.precio += 0
        elif self.humedad == 14:
            self.precio -= 0.2
        elif self.humedad == 16:
            self.precio -= 0.3
            
        total = self.precio * self.peso    
        print(f'El precio total es: {self.precio}')   
            
cafe1 = Cafe('Pepito', 'ORGANICO', 100, 'catimor', 72, 13)
#cafe1.mostrar()
cafe1.seleccionar()
cafe2 = Cafe('Dani', 'CONVENCIONAL',  85, 'catuai', 56, 12)
#cafe2.mostrar()
cafe2.seleccionar()