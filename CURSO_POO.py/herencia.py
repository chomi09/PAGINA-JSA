class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print('Hola, estoy hablando')

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        return f'mi habilidad es: {self.habilidad}'
        
class Empleado_artista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print( f'Hola soy: {self.nombre}, tengo {self.edad} años y {super().mostrar_habilidad()}, trabajo en la {self.empresa}')

# class Empleado(Persona):
#     def __init__ (self, nombre, edad, nacionalidad, trabajo, salario):
#         super().__init__(nombre, edad, nacionalidad)
#         self.trabajo = trabajo
#         self.salario = salario
#     def hablar(self):
#         print('NO')
        
# class Estudiante(Persona):
#     def __init__ (self, nombre, edad, nacionalidad, NOTAS, uni):
#         super().__init__(nombre, edad, nacionalidad)
#         self.trabajo = NOTAS
#         self.salario = uni   

#roberto = Empleado_artista('roberto', 15, 'peruana', 'programador', 1000, 'Sunat')
roberto = Artista('cantante')

#roberto.presentarse()

herencia = issubclass(Empleado_artista, Persona)
print(herencia)

instancia = isinstance(roberto, Artista)
print(instancia)