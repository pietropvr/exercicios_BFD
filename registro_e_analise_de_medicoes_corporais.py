import json
import os

# Define o caminho do arquivo de forma segura (funciona no Windows e Mobile)
ARQUIVO_DADOS = os.path.join(os.getcwd(), 'medicoes.json')

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4)

def registrar_medicao():
    print("=== REGISTRO DE MEDIÇÕES ===")
    data = input("Data (DD/MM/AAAA): ")
    peso = float(input("Peso (kg): "))
    cintura = float(input("Cintura (cm): "))
    quadril = float(input("Quadril (cm): "))
    
    dados = carregar_dados()
    dados.append({
        "data": data,
        "peso": peso,
        "cintura": cintura,
        "quadril": quadril
    })
    salvar_dados(dados)
    print("\nMedição registrada com sucesso!")

def analisar_historico():
    dados = carregar_dados()
    if not dados:
        print("Nenhum dado registrado ainda.")
        return
        
    pesos = [item['peso'] for item in dados]
    razoes_cq = [item['cintura'] / item['quadril'] for item in dados]
    
    print("\n=== ANÁLISE DO HISTÓRICO ===")
    print(f"Total de registros: {len(dados)}")
    print(f"Peso Inicial (Primeira medição): {pesos[0]} kg")
    print(f"Peso Atual (Última medição): {pesos[-1]} kg")
    print(f"Menor Peso alcançado: {min(pesos)} kg")
    print(f"Maior Peso registrado: {max(pesos)} kg")
    print(f"Peso Médio: {sum(pesos)/len(pesos):.2f} kg")
    
    rcq_media = sum(razoes_cq) / len(razoes_cq)
    print(f"\nRazão Cintura/Quadril (Média): {rcq_media:.2f}")
    
    evolucao_total = pesos[0] - pesos[-1]
    if evolucao_total > 0:
        print(f"Progresso: Perdeu {evolucao_total:.2f} kg desde o início.")
    elif evolucao_total < 0:
        print(f"Progresso: Ganhou {abs(evolucao_total):.2f} kg desde o início.")

# === MENU PRINCIPAL DE TESTE ===
def menu():
    while True:
        print("\n--- TRACKER CORPORAL ---")
        print("1. Registrar Nova Medição")
        print("2. Ver Análise de Histórico")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            registrar_medicao()
        elif escolha == '2':
            analisar_historico()
        elif escolha == '3':
            break
        else:
            print("Opção inválida.")


menu()
