# Projeto Pratico - disciplina de linguagens de programação para engenharia de dados

Este é um projeto que visa realizar o processamento de dados provenientes de arquivos CSV fornecidos pelo Instituto Brasileiro de Geografia e Estatística (IBGE). O objetivo é extrair informações contidas nesses arquivos e armazená-las em um banco de dados SQLite para posterior análise.

## Requisitos

Para executar este script, você precisará ter Python instalado em seu sistema. Além disso, certifique-se de ter as seguintes bibliotecas Python instaladas:

-   `csv`: para leitura de arquivos CSV.
-   `sqlite3`: para interagir com o banco de dados SQLite.
-   `pathlib`: para manipulação de caminhos de arquivos.

## Funcionalidades

-   O script lê arquivos CSV contendo dados do IBGE.
-   Os dados são inseridos em uma tabela no banco de dados SQLite denominada `ENDERECO_IBGE`.
-   Cada arquivo CSV é processado e os dados são inseridos na tabela SQLite.
-   O script cria um banco de dados SQLite (`DESAFIO_2.db`) se não existir.
-   Caso a tabela `ENDERECO_IBGE` já exista, ela é eliminada e recriada para evitar duplicatas.

## Utilização

1.  Certifique-se de ter Python instalado em seu sistema.
2.  Clone este repositório em seu ambiente local.
3.  Execute o script `processamento_dados_ibge.ipynb`.
4.  Aguarde até que o script processe os arquivos CSV e insira os dados no banco de dados SQLite.
5.  Após a execução bem-sucedida, você poderá realizar consultas SQL diretamente no banco de dados ou utilizar o banco de dados em outras aplicações.

## Autor

Este projeto foi desenvolvido por Felipe Soares Ferreira e Winiston Vieira de Freitas.
