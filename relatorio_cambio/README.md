# Sistema de Relatório de Câmbio

Uma aplicação de linha de comando (CLI) desenvolvida em Python para consultar, armazenar e analisar cotações de moedas em tempo real. O sistema utiliza uma API de câmbio para obter os dados, salva o histórico em um banco de dados SQLite local e exibe relatórios formatados utilizando o Jinja2 e a biblioteca Rich.

## Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. **Consultar cotação atual:** Busca o valor atual de uma moeda e salva automaticamente no banco de dados com a data e hora corretas.
2. **Gerar relatório de variação e Exportar:** Analisa as últimas cotações de uma moeda, calcula a variação percentual e exporta um arquivo `.txt`.
3. **Template customizado:** Permite testar templates Jinja2 e salvá-los no banco de dados.
4. **Listar histórico:** Exibe o histórico de consultas salvas, com suporte a filtro por moeda.
5. **Comparar moedas:** Compara o valor de compra de duas moedas diferentes simultaneamente.
6. **Usar template via arquivo (.txt):** Lê um layout de um arquivo de texto externo para formatar a saída.
7. **Conversor Múltiplo:** Converte um valor em Reais (R$) para múltiplas moedas (USD, EUR, GBP) ao mesmo tempo.
8. **Alerta de Mercado:** Monitora uma moeda e emite um alerta visual caso o valor caia abaixo de um limite definido pelo usuário.

## Fuso Horário (Timezone)

O sistema foi configurado para forçar a utilização do fuso horário de Brasília/São Paulo (`America/Sao_Paulo`). Isso garante que os registros salvos no banco de dados tenham a data e hora corretas da consulta no Brasil, mesmo se a aplicação for executada em servidores na nuvem (como o GitHub Codespaces) que utilizam o horário UTC por padrão.

## Pré-requisitos

Devido à utilização da biblioteca nativa `zoneinfo` para a manipulação precisa do fuso horário, é obrigatório o uso de uma versão atualizada do Python:

* **Python 3.9 ou superior**

As seguintes bibliotecas externas também são necessárias (verifique o seu arquivo `requirements.txt`):
* `rich` (Para a interface e cores no terminal)
* `jinja2` (Para a renderização dos templates de texto)
* `requests` (Para as requisições na API, caso utilizado no seu módulo `api.py`)

## Como Executar

1. Clone o repositório para a sua máquina ou ambiente de desenvolvimento.
2. Instale as dependências executando o comando:
   ```bash
   pip install -r requirements.txt
