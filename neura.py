#Lógica Orientada a Objetos y Funciones para entender mejor las operaciones de las neuronas

class NeuronaMP:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def activar(self, entradas):
        suma_ponderada = sum(p * e for p, e in zip(self.pesos, entradas))
        return 1 if suma_ponderada >= self.umbral else 0

# Instancias de neuronas
neura_and = NeuronaMP([1, 1], 2)
neura_or = NeuronaMP([1, 1], 1)
neura_not = NeuronaMP([-1], 0)

# Funciones de Lógica Neuronas
def AND(entrada):
    return neura_and.activar(entrada)

def OR(entrada):
    return neura_or.activar(entrada)

def NOT(entrada):
    return neura_not.activar([entrada])

def NAND(entrada):
    return NOT(AND(entrada))

def NOR(entrada):
    return NOT(OR(entrada))

def XOR(entrada):
    return AND([NAND(entrada), OR(entrada)])

def XNOR(entrada):
    return NOT(XOR(entrada))

# Entradas posibles
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Mostrar resultados por Neurona
for entrada in entradas:
    print(f"AND({entrada}) = {AND(entrada)}")
print()

for entrada in entradas:
    print(f"OR({entrada}) = {OR(entrada)}")
print()

print(f"NOT([1]) = {NOT(1)}")
print(f"NOT([0]) = {NOT(0)}")
print()

for entrada in entradas:
    print(f"NOR({entrada}) = {NOR(entrada)}")
print()

for entrada in entradas:
    print(f"NAND({entrada}) = {NAND(entrada)}")
print()

for entrada in entradas:
    print(f"XOR({entrada}) = {XOR(entrada)}")
print()

for entrada in entradas:
    print(f"XNOR({entrada}) = {XNOR(entrada)}")
print()
