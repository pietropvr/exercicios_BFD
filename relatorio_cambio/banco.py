import sqlite3
import os
from datetime import datetime

def conectar():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.join(diretorio_atual, "dados_cambio.db")
    return sqlite3.connect(caminho_db)


def criar_tabelas():
    with conectar() as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS cotacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            moeda TEXT,
            compra REAL,
            venda REAL,
            data_hora TEXT
        )
        """)
        con.execute("""
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            texto_template TEXT
        )
        """)

def salvar_cotacao(moeda, compra, venda):
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with conectar() as con:
        con.execute(
            "INSERT INTO cotacoes (moeda, compra, venda, data_hora) VALUES (?, ?, ?, ?)",
            (moeda, float(compra), float(venda), data_atual)
        )

def buscar_historico(moeda=None):
    with conectar() as con:
        cursor = con.cursor()
        if moeda:
            cursor.execute("SELECT * FROM cotacoes WHERE moeda = ?", (moeda,))
        else:
            cursor.execute("SELECT * FROM cotacoes")
        
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

def buscar_historico_dias(moeda, dias):
    with conectar() as con:
        cursor = con.cursor()
        cursor.execute("""
        SELECT data_hora, compra FROM cotacoes 
        WHERE moeda = ? ORDER BY id DESC LIMIT ?
        """, (moeda, dias))
        
        resultados = cursor.fetchall()
        cursor.close()
        return resultados

def salvar_template(nome, texto):
    with conectar() as con:
        con.execute(
            "INSERT INTO templates (nome, texto_template) VALUES (?, ?)", 
            (nome, texto)
        )
