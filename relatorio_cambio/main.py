import sys
import os
import api
import banco
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from jinja2 import Template

console = Console()

def exibir_menu():
    console.print("\n[bold blue]=== Relatório de Câmbio ===[/bold blue]")
    console.print("1. Consultar cotação atual")
    console.print("2. Gerar relatório de variação")
    console.print("3. Template customizado (Salvar no Banco)")
    console.print("4. Listar histórico")
    console.print("5. Comparar moedas")
    console.print("[yellow]--- Tarefas Bônus ---[/yellow]")
    console.print("6. Usar template via arquivo (.txt)")
    console.print("7. Conversor Múltiplo (Bônus)")
    console.print("8. Alerta de Mercado (Bônus)")
    console.print("0. Sair")
    return input("Escolha uma opção: ")

def opcao_1_consultar():
    moeda = input("Sigla da moeda (ex: USD, EUR): ").upper()
    dados = api.consultar_moeda(moeda)
    
    if dados:
        banco.salvar_cotacao(moeda, dados['compra'], dados['venda'])
        template = Template("**{{ m }}**\nCompra: R$ {{ c }}\nVenda: R$ {{ v }}")
        texto = template.render(m=moeda, c=dados['compra'], v=dados['venda'])
        console.print(Panel(texto, title="Cotação Atual", style="green"))
    else:
        console.print("[red]Moeda não encontrada ou erro na API.[/red]")

def opcao_2_relatorio():
    moeda = input("Sigla da moeda (ex: USD): ").upper()
    dias = int(input("Número de registros para analisar: "))
    
    registros = banco.buscar_historico_dias(moeda, dias)
    if len(registros) < 2:
        console.print("[yellow]Histórico insuficiente. Faça mais consultas na Opção 1.[/yellow]")
        return
        
    registros.reverse() 
    dados_jinja = []
    valor_anterior = None
    
    for data, valor in registros:
        variacao = 0.0
        if valor_anterior is not None:
            variacao = ((valor - valor_anterior) / valor_anterior) * 100
        dados_jinja.append({"data": data, "valor": valor, "var": variacao})
        valor_anterior = valor
        
    template = Template("""
{% for linha in dados %}
{{ linha.data }} | R$ {{ "%.2f"|format(linha.valor) }} |  Variação: {{ "%.2f"|format(linha.var) }}%
{% endfor %}
    """)
    texto = template.render(dados=dados_jinja)
    console.print(Panel(texto, title=f"Variação - {moeda}", style="blue"))

def opcao_3_template():
    texto_usuario = input("Digite seu template Jinja2 (ex: Hoje: {{ compra }}): ")
    val_compra = input("Valor para 'compra': ")
    template = Template(texto_usuario)
    resultado = template.render(compra=val_compra)
    
    banco.salvar_template("template_banco", texto_usuario)
    console.print(Panel(resultado, title="Resultado", style="magenta"))

def opcao_4_historico():
    filtro = input("Filtrar por moeda (Enter para todas): ").upper()
    historico = banco.buscar_historico(filtro if filtro else None)
    tabela = Table(title="Histórico Salvo")
    tabela.add_column("ID")
    tabela.add_column("Moeda")
    tabela.add_column("Compra")
    tabela.add_column("Data/Hora")
    
    for linha in historico:
        tabela.add_row(str(linha[0]), linha[1], f"R$ {linha[2]:.2f}", linha[4])
    console.print(tabela)

def opcao_5_comparar():
    m1 = input("Primeira moeda (ex: USD): ").upper()
    m2 = input("Segunda moeda (ex: EUR): ").upper()
    
    d1 = api.consultar_moeda(m1)
    d2 = api.consultar_moeda(m2)
    
    if d1 and d2:
        template = Template(
            " Comparativo Direto:\n1 {{ moeda1 }} custa R$ {{ valor1 }}\n1 {{ moeda2 }} custa R$ {{ valor2 }}"
        )
        texto = template.render(moeda1=m1, valor1=d1['compra'], moeda2=m2, valor2=d2['compra'])
        console.print(Panel(texto, style="cyan"))
    else:
        console.print("[red]Erro ao buscar cotações.[/red]")

def opcao_6_template_txt():
    nome_arquivo = input("Nome do arquivo (ex: layout.txt): ")
    if not os.path.exists(nome_arquivo):
        with open(nome_arquivo, "w", encoding="utf-8") as f:
            f.write("Template do Arquivo!\nMoeda: {{ m }} | Valor: R$ {{ v }}")
        console.print(f"[yellow]Arquivo de exemplo criado. Tente rodar novamente.[/yellow]")
        return
        
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        texto = f.read()
        
    moeda = input("Qual a moeda? (ex: USD): ")
    valor = input("Qual o valor? ")
    
    template = Template(texto)
    console.print(Panel(template.render(m=moeda, v=valor), title="Template via TXT", style="green"))

def opcao_7_conversor():
    reais = float(input("Quantos Reais (R$) você tem? "))
    moedas = ["USD", "EUR", "GBP"]
    
    dados_jinja = []
    for m in moedas:
        cotacao = api.consultar_moeda(m)
        if cotacao:
            convertido = reais / cotacao['compra']
            dados_jinja.append({"moeda": m, "valor": convertido})
            
    template = Template("""
**Com R$ {{ grana }}, você compra:**
{% for item in dados %}
- {{ item.moeda }}: {{ "%.2f"|format(item.valor) }}
{% endfor %}
    """)
    console.print(Panel(template.render(grana=reais, dados=dados_jinja), style="magenta"))

def opcao_8_alerta():
    moeda = input("Moeda para monitorar (ex: USD): ").upper()
    alvo = float(input("Avisar se o preço cair abaixo de qual valor? (ex: 5.00): "))
    
    cotacao = api.consultar_moeda(moeda)
    if cotacao:
        if cotacao['compra'] < alvo:
            template = Template("ALERTA DE COMPRA! \nO {{ m }} caiu para R$ {{ c }}!")
            texto = template.render(m=moeda, c=cotacao['compra'])
            console.print(Panel(texto, style="bold white on red"))
        else:
            console.print(f"[blue]Tudo normal. O valor atual é R$ {cotacao['compra']:.2f}.[/blue]")

if __name__ == "__main__":
    banco.criar_tabelas()
    while True:
        escolha = exibir_menu()
        if escolha == '1': opcao_1_consultar()
        elif escolha == '2': opcao_2_relatorio()
        elif escolha == '3': opcao_3_template()
        elif escolha == '4': opcao_4_historico()
        elif escolha == '5': opcao_5_comparar()
        elif escolha == '6': opcao_6_template_txt()
        elif escolha == '7': opcao_7_conversor()
        elif escolha == '8': opcao_8_alerta()
        elif escolha == '0': sys.exit()
