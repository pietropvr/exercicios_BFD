#Conversor de temperaturas - Funções:

#Celsius para Fahrenheit:
def converter_celsius_para_fahrenheit(celsius):
    # A variável 'celsius' é o valor que a função recebe
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Celsius para Kelvin:
def converter_celsius_para_kelvin(celsius):
    kelvin = (celsius + 273.15)
    return kelvin

#Fahrenheit para Celsius:
def converter_fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#Fahrenheit para Kelvin:
def converter_fahrenheit_para_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

#Kelvin para Celsius:
def converter_kelvin_para_celsius(kelvin):
    celsius = (kelvin - 273.15)
    return celsius

#Kelvin para Fahrenheit:
def converter_kelvin_para_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

while True:
    print("\n--- Conversor de Temperaturas ---")
    print("Unidades: [C]elsius, [F]ahrenheit, [K]elvin ou [S]air")
    
    # Pegamos a origem e usamos .upper() para aceitar letras minúsculas ou maiúsculas
    origem = input("Escolha a unidade de ORIGEM (C, F, K, S): ").upper()
    
    if origem == 'S':
        print("Encerrando o programa. Até logo!")
        break 
        
    destino = input("Escolha a unidade de DESTINO (C, F, K): ").upper()
    
    # Coletamos o valor e transformamos em número (float)
    valor_digitado = input("Digite o valor da temperatura: ")
    valor = float(valor_digitado)
    
    # --- ROTEAMENTO ---
       # Caminhos saindo de CELSIUS
    if origem == 'C' and destino == 'F':
        resultado = converter_celsius_para_fahrenheit(valor)
        print(f"\nResultado: {valor} °C equivalem a {resultado:.2f} °F")
        
    elif origem == 'C' and destino == 'K':
        resultado = converter_celsius_para_kelvin(valor)
        print(f"\nResultado: {valor} °C equivalem a {resultado:.2f} °K")

    # Caminhos saindo de FAHRENHEIT
    elif origem == 'F' and destino == 'C':
        resultado = converter_fahrenheit_para_celsius(valor)
        print(f"\nResultado: {valor} °F equivalem a {resultado:.2f} °C")
        
    elif origem == 'F' and destino == 'K':
        resultado = converter_fahrenheit_para_kelvin(valor)
        print(f"\nResultado: {valor} °F equivalem a {resultado:.2f} °K")

    # Caminhos saindo de KELVIN
    elif origem == 'K' and destino == 'C':
        resultado = converter_kelvin_para_celsius(valor)
        print(f"\nResultado: {valor} °K equivalem a {resultado:.2f} °C")
       
    elif origem == 'K' and destino == 'F':
        resultado = converter_kelvin_para_fahrenheit(valor)
        print(f"\nResultado: {valor} ° K equivalem a {resultado:.2f} °F")

    # A REDE DE SEGURANÇA (Catch-all)
    else:
        # Se o usuário digitar "C" para "C", ou letras inventadas tipo "Y" para "H", 
        # o programa não quebra. Ele cai aqui!
        print("Opção inválida! Por favor, escolha C, F ou K em unidades diferentes.")
