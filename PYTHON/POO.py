class Cafe:
    def __init__(self, variedad, precio):
        self.variedad = variedad
        self.precio = precio

    def mostrar_info(self):
        print(f"Café {self.variedad} - S/ {self.precio}")

# Crear objetos
cafe1 = Cafe("Arabica", 15)
cafe2 = Cafe("Geisha", 30)

# Usar métodos
cafe1.mostrar_info()
cafe2.mostrar_info()

print("---------------------------------------")
class Alumno:
    def __init__(self, nombre, grado, dni, curso, esta_matriculado ):
        self.nombre = nombre
        self.grado = grado
        self.dni = dni
        self.curso = curso
        self.esta_matriculado = esta_matriculado
    def presentarse(self):
        print(f'Alumno {self.nombre} del {self.grado} con dni: {self.dni} se encuentra matriculado en el curso de {self.curso}')
    def matricular(self):
        if self.esta_matriculado == True:
            print(f'El usuario {self.nombre} ya se encuentra matriculado')
        else:
            print(f'El usuario {self.nombre} no se encuentra matriculado')
            print('matriculando.......')
            self.esta_matriculado = True
        
        
    

alumno1 = Alumno('juan', 'tercer semestre', '76335832', 'estadistica', False)
alumno2 = Alumno('daniel', 'cuarto semestre', '78685432', 'calculo', True)

#alumno1.presentarse()
#alumno2.presentarse()
alumno2.matricular()

class Persona:
    def __init__(self, nombre, zona, cultivo):
        self.nombre = nombre
        self.zona = zona
        self.cultivo = cultivo
    def productor(self):
        print('El productor {self.nombre} de la {self.zona} con el cultivo {self.}')





