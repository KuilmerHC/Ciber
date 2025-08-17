class NeuronaMP:
    def __init__(self, pesos, umbral):
        self.pesos = pesos
        self.umbral = umbral

    def activar(self, entradas):
        suma_ponderada = sum(p * e for p, e in zip(self.pesos, entradas))
        return 1 if suma_ponderada >= self.umbral else 0
    
# Entradas Posibles
entradas = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]   

# Ejemplos de uso:

# AND
neura_and = NeuronaMP([1, 1], 2)
for entrada in entradas:
    salida_and = neura_and.activar(entrada)
    print(f"AND({entrada}) = {salida_and}")

print()

# OR
neura_or = NeuronaMP([1, 1], 1)
for entrada in entradas:
    salida_or = neura_or.activar(entrada)
    print(f"OR({entrada}) = {salida_or}")

print()

# NOT
neura_not = NeuronaMP([-1], 0)
r1 = neura_not.activar([1])     # 0
r0 = neura_not.activar([0])     # 1
print(f"NOT (1) = {r1}")
print(f"NOT (0) = {r0}")

print()

# NOR -> Negar OR

for entrada in entradas:
    salida_or = neura_or.activar(entrada)
    salida_nor = neura_not.activar([salida_or])
    print(f"NOR({entrada}) = {salida_nor}")

print()

# NAND -> Negar AND
for entrada in entradas:
    salida_and = neura_and.activar(entrada)
    salida_nand = neura_not.activar([salida_and])
    print(f"NAND({entrada}) = {salida_nand}")

print()

# XOR multiple neuronas

for entrada in entradas:
    salida_and = neura_and.activar(entrada)
    salida_nand = neura_not.activar([salida_and])
    salida_or = neura_or.activar(entrada)
    xor = neura_and.activar([salida_nand, salida_or])
    
    print(f"XOR({entrada}) = {xor}")
 
print()

# XNOR -> Negar el XOR

for entrada in entradas:
    salida_and = neura_and.activar(entrada)
    salida_nand = neura_not.activar([salida_and])
    salida_or = neura_or.activar(entrada)
    salida_xor = neura_and.activar([salida_nand, salida_or])
    xnor = neura_not.activar([salida_xor])

    print(f"XNOR({entrada}) = {xnor}")
