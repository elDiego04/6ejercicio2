class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir(self):
        print(f"El alumno {self.nombre} tiene una nota de {self.nota}")
    
    def resultado(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado")
        else:
            print(f"El alumno {self.nombre} ha suspendido")
alumno1 = Alumno('Juan', 7)
alumno1.imprimir()
alumno1.resultado()