import csv
import sqlite3
from pathlib import Path

# Caminho dos arquivos CSV
caminho = Path(r"[Informe o caminho da pasta onde consta os arquivos CSVs]")
arquivos = caminho.iterdir()


# Função para dropar a tabela no SQLite
def dropar_tabela(cursor):
    cursor.execute("DROP TABLE IF EXISTS ENDERECO_IBGE")


# Função para criar a tabela no SQLite
def criar_tabela(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS ENDERECO_IBGE(COD_UF TEXT, COD_MUN TEXT, COD_ESPECIE TEXT, LATITUDE REAL, LONGITUDE REAL, NV_GEO_COORD TEXT)"
    )


# Função para inserir os dados do CSV na tabela SQLite
def inserir_dados(cursor, dados):
    cursor.executemany("INSERT INTO ENDERECO_IBGE VALUES (?, ?, ?, ?, ?, ?)", dados)


# Nome do arquivo de banco de dados SQLite
banco_de_dados = "DESAFIO_2.db"

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect(banco_de_dados)
cursor = conexao.cursor()

# Dropar a tabela se ela existir
dropar_tabela(cursor)

# Criar a tabela se ela não existir
criar_tabela(cursor)


# Iterar sobre os arquivos CSV no caminho especificado
for arquivo in arquivos:
    if arquivo.suffix == ".csv":
        print(arquivo)
        # Ler os dados do arquivo CSV
        with open(arquivo, "r", newline="", encoding="utf-8") as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=";")
            # Pular o cabeçalho do arquivo CSV
            next(leitor_csv)
            # Converter os dados em tuplas e inserir na tabela SQLite
            dados_para_inserir = [tuple(row) for row in leitor_csv]
            inserir_dados(cursor, dados_para_inserir)

# Commit das alterações e fechar conexão
conexao.commit()

conexao.close()

print("Dados inseridos com sucesso!")


# Nome do arquivo de banco de dados SQLite
banco_de_dados = "DESAFIO_2.db"

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect(banco_de_dados)
cursor = conexao.cursor()


# QTD na tabela ENDERECO_IBGE
cursor.execute("SELECT count(1) FROM ENDERECO_IBGE")
cursor.fetchall()
