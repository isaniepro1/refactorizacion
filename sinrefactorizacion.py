class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        import math
        return math.pi * self.radio**2

    def calcular_perimetro(self):  
        import math
        return 2 * math.pi * self.radio

# Lista de figuras
rectangulo = Rectangulo(5, 3)
circulo = Circulo(2)

# Imprimimos las propiedades
print(f"El rectángulo tiene un área de {rectangulo.calcular_area()} y un perímetro de {rectangulo.calcular_perimetro()}")
print(f"El círculo tiene un área de {circulo.calcular_area()} y un perímetro de {circulo.calcular_perimetro()}")