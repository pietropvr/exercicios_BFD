# Sistema de Consulta e Análise de Câmbio

Este projeto é uma aplicação em Python desenvolvida para consultar, armazenar e analisar cotações de moedas em tempo real. O sistema foi refatorado para utilizar a **Brasil API** como fonte de dados, garantindo maior estabilidade e aderência às diretrizes do projeto. 

A aplicação conta com uma interface de terminal estilizada, persistência de dados local e recursos avançados implementados como tarefas bônus.

## Funcionalidades Principais

* **Consulta via Brasil API:** Integração direta com a Brasil API para obter as cotações de moedas atualizadas.
* **Armazenamento Local (SQLite):** Todas as consultas realizadas são salvas no banco de dados local (`dados_cambio.db`), construindo um histórico de cotações para consultas futuras.
* **Cálculo de Variações:** Ferramentas de análise para calcular e exibir a variação de taxas entre diferentes datas registradas no histórico.
* **Interface de Linha de Comando (CLI):** Menus interativos e saídas de dados formatadas e coloridas no terminal, proporcionando uma melhor experiência de uso (utilizando a biblioteca `rich`).

## Tarefas Bônus Implementadas

* **Exportação de Relatórios (Jinja2):** Capacidade de exportar o histórico e as análises de câmbio para arquivos formatados (como HTML ou TXT) utilizando o motor de templates Jinja2.
* **Cobertura de Testes Automatizados:** Inclusão de testes de software utilizando a biblioteca `pytest` para garantir a integridade das funções de API e de banco de dados (configurações de cache de teste devidamente isoladas via `.gitignore`).
* **Tratamento de Exceções Avançado:** Sistema robusto para lidar com quedas de conexão, respostas inesperadas da API ou erros de gravação no banco de dados, retornando mensagens claras ao usuário.

## Estrutura de Diretórios e Arquivos

* `main.py`: Ponto de entrada da aplicação, contendo o loop principal e a interface de usuário.
* `api.py`: Módulo dedicado exclusivamente à comunicação com a Brasil API e tratamento do formato JSON retornado.
* `banco.py`: Módulo responsável por inicializar o SQLite, criar as tabelas necessárias e executar as querys de inserção e leitura.
* `requirements.txt`: Arquivo de manifesto listando todas as bibliotecas de terceiros necessárias.
* `.gitignore`: Arquivo de configuração que impede o envio de dados locais (como o `.db`), caches (`__pycache__`, `.pytest_cache`) e ambientes virtuais (`venv`) para o repositório remoto.

## Pré-requisitos

Para executar este projeto, é necessário ter instalado em sua máquina:
* Python 3.8 ou superior.
* Gerenciador de pacotes `pip`.
