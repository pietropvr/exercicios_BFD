def conversor_distancias():
    print("=== CONVERSOR DE DISTÂNCIAS ===")
    print("Unidades disponíveis: km, mi, m")
    
    origem = input("Escolha a unidade de origem: ").lower()
    destino = input("Escolha a unidade de destino: ").lower()
    valor = float(input(f"Digite o valor em {origem}: "))
    
    # Fatores de conversão para metros (unidade base)
    fatores_para_metros = {
        'km': 1000.0,
        'mi': 1609.34,
        'm': 1.0
    }
    
    if origem in fatores_para_metros and destino in fatores_para_metros:
        # Converte a origem para metros, depois divide pelo fator de destino
        valor_em_metros = valor * fatores_para_metros[origem]
        resultado = valor_em_metros / fatores_para_metros[destino]
        print(f"\nResultado: {valor} {origem} = {resultado:.2f} {destino}")
    else:
        print("\nErro: Unidade inválida. Use apenas km, mi ou m.")


conversor_distancias()
