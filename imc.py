#Calculadora de IMC:

#Solicita peso e altura, entrega IMC (numérico)
peso_str = input("Peso (kg): ")
altura_str = input("Altura (m): ")

#Converte string para número com vírgula:
peso = float(peso_str)
altura = float(altura_str)

print(f"Peso digitado: {peso}")
print(f"Altura digitada: {altura}")

#Fórmula: peso / (altura ** 2)
imc = peso / (altura**2)
print(f"IMC calculado: {imc:.2f}")