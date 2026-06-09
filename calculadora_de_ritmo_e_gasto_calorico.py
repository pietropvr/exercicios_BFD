def calculadora_pace_e_calorias():
    print("=== CALCULADORA DE CORRIDA E CALORIAS ===")
    
    # 1. Cálculo de Pace e Velocidade
    distancia_km = float(input("Distância percorrida (km): "))
    tempo_min = float(input("Tempo total (minutos): "))
    
    pace_decimal = tempo_min / distancia_km
    minutos = int(pace_decimal)
    segundos = int((pace_decimal - minutos) * 60)
    
    velocidade_kmh = distancia_km / (tempo_min / 60)
    
    print(f"\nSeu Pace médio: {minutos}:{segundos:02d} min/km")
    print(f"Sua Velocidade média: {velocidade_kmh:.2f} km/h")
    
    # 2. Cálculo de Calorias
    print("\n--- Gasto Calórico ---")
    peso_kg = float(input("Seu peso (kg): "))
    print("Atividades: 1-Caminhada, 2-Corrida, 3-Ciclismo")
    opcao_ativ = input("Escolha a atividade (1/2/3): ")
    
    mets = {'1': 3.5, '2': 9.8, '3': 7.5}
    
    if opcao_ativ in mets:
        met_escolhido = mets[opcao_ativ]
        # Aplicação da fórmula
        calorias = met_escolhido * peso_kg * (tempo_min / 60)
        print(f"Gasto calórico estimado: {calorias:.0f} kcal")
    else:
        print("Atividade inválida.")


calculadora_pace_e_calorias()
