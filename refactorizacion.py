class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcular_area(self):
        raise NotImplementedError("Subclases deben implementar este método")

    def calcular_perimetro(self):
        raise NotImplementedError("Subclases deben implementar este método")

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        import math
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        import math
        return 2 * math.pi * self.radio

# Lista de figuras
figuras = [Rectangulo(5, 3), Circulo(2)]

# Iteramos y calculamos propiedades
for figura in figuras:
    print(f"La figura {figura.nombre} tiene un área de {figura.calcular_area()} y un perímetro de {figura.calcular_perimetro()}")