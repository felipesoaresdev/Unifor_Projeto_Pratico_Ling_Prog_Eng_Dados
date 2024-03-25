# Projeto Pratico - disciplina de linguagens de programação para engenharia de dados

Este é um projeto que visa realizar o processamento de dados provenientes de arquivos CSV fornecidos contendo dados o IBGE. O objetivo é extrair informações contidas nesses arquivos e armazená-las em um banco de dados para posterior análise.

## Pontos de dificuldade
A manipulação direta dos dados CSV sem o uso de bibliotecas como o Pandas se tornou mais desafiadora.
Possiveis riscos de lidar com diferentes tipos de dados, valores ausentes e formatação irregular.
Foi necessário garantir que os dados lidos do CSV estivessem corretos e formatados adequadamente antes da inserção no banco de dados. Caso contrário, erros poderiam ocorrer durante a inserção ou consultas posteriores.
Dependendo do tamanho do arquivo CSV e da quantidade de dados inseridos no banco de dados, a performance da operação de inserção poderia ser completamente afetada. Manipular maiores volumes de dados poderá exigir otimizações adicionais para garantir uma execução eficiente.
A abertura e o fechamento manual da conexão com o banco de dados podem ser propensos a erros, especialmente se esquecido. Isso gerou alguns problemas de bloqueio do banco de dados durante os testes.

## Pontos a favor:
A manipulação direta dos dados CSV e inserção no banco de dados em Python é relativamente simples e direta. Não houve necessidade de aprender novas bibliotecas ou ferramentas complicadas.

Tivemos controle total sobre o processo de manipulação e inserção de dados. Isso permitiu personalizar o fluxo de trabalho de acordo com os requisitos específicos do desafio garantindo a integridade dos dados.

O uso do Python oferece uma variedade enorme de bibliotecas e ferramentas para manipulação de dados, permitindo adaptar o nosso código conforme necessário e integrá-lo 
facilmente a outras partes do desenvolvimento.

## Ferramentas facilitariam a implementação
Pandas: é uma biblioteca Python amplamente utilizada para manipulação e análise de dados. Ele fornece estruturas de dados e ferramentas poderosas para trabalhar com dados tabulares, incluindo a leitura e escrita de arquivos CSV, além de integração fácil com bancos de dados como SQLite, mysql, postegreSQL...

Apache Spark: é uma plataforma de processamento de dados distribuída e escalável. Ele oferece suporte para processamento de dados em grande escala e integração com uma variedade de fontes de dados, incluindo arquivos CSV e bancos de dados SQL.

Apache Airflow: é uma plataforma de fluxo de trabalho de dados que permite agendar, monitorar e gerenciar pipelines de dados de forma programática. Ele pode ser útil para automatizar o processo de ingestão, transformação e carga de dados em um ambiente de produção.

Dask (sugerido pelo chatgpt): é uma biblioteca Python que estende a interface do Pandas e NumPy para trabalhar com dados que não cabem na memória RAM de um único computador. Ele pode ser útil para lidar com grandes volumes de dados de forma eficiente.

SQLAlchemy(sugerido pelo chatgpt): é uma biblioteca Python que fornece uma API de alto nível para interagir com bancos de dados relacionais. Ele simplifica a execução de consultas SQL e a manipulação de dados em bancos de dados SQL.

obs.: A escolha da ferramenta mais adequada depende dos requisitos específicos do projeto e das preferências da equipe de desenvolvimento.

## Requisitos

Para executar este script, você precisará ter Python instalado, Jupyter Notebook ou similares instalados em seu sistema. Além disso, certifique-se de ter as seguintes bibliotecas Python instaladas:

-   `csv`: para leitura de arquivos CSV.
-   `sqlite3`: para interagir com o banco de dados SQLite.
-   `pathlib`: para manipulação de caminhos de arquivos.

Ter baixado todos os CSVs através do link abaixo:

https://drive.google.com/drive/folders/1NWtp0sb_DXDPXnUdNCal1rzoZw6zMjfc

## Funcionalidades

-   O script lê arquivos CSV contendo dados do IBGE.
-   Os dados são inseridos em uma tabela no banco de dados SQLite denominada `ENDERECO_IBGE`.
-   Cada arquivo CSV é processado e os dados são inseridos na tabela do SQLite.
-   O script cria um banco de dados SQLite (`DESAFIO_2.db`) se não existir.
-   Caso a tabela `ENDERECO_IBGE` já exista, ela é eliminada e recriada para evitar duplicatas.

## Utilização

1.  Certifique-se de ter Python instalado em seu sistema.
2.  Clone este repositório em seu ambiente local.
3.  Insira os arquivos baixados na pasta Arquivos.
4.  Execute o script `processamento_dados_ibge.ipynb`.
5.  Aguarde até que o script processe os arquivos CSV e insira os dados no banco de dados SQLite.
6.  Após a execução bem-sucedida, você poderá realizar consultas SQL diretamente no banco de dados ou utilizar o banco de dados em outras aplicações.

## Autor

Este projeto foi desenvolvido por Felipe Soares Ferreira e Winiston Vieira de Freitas.
