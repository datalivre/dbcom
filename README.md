# PySpark DBcom 
## Comparador de bases relacionais

Este programa faz comparação quantitativa de tabelas de duas bases relacionais diferentes. Para acessar as bases de dados ele realiza conexões JDBC e puxa a tabela para o ambiente Spark.

### Modo de usar:
Apos editar o arquivo packs/get_string.py, execute `dbcom -t tabela1,tabela2,...,tabelaN`

### Exemplo de saída:

|    | table(s)                             |   sqlserver |   redshift |
|----|--------------------------------------|-------------|------------|
|  0 | assistencia_questionario_pergunta_tb |          87 |         87 |
|  1 | assistencia_questionario_resposta_tb |         255 |        255 |
|  2 | assistencia_questionario_tb          |          31 |         31 |
|  3 | assistencia_servico_tb               |         392 |        392 |
|  4 | itens_nao_inclusos_tb                |         407 |        407 |
|  5 | plano_assistencia_tb                 |          77 |         77 |
|  6 | proposta_assistencia_atual_tb        |     6739161 |          0 |
|  7 | servico_tb                           |          84 |         84 |


### Help:
`dbcom -h`<br/>
usage: dbcom [-h] [-e AMBIENTE] [-d DATABASE] [-c CATEGORY] [-t TABLES]<br/>
<br/>
App comparador quantitativo de tabelas de diferentes bases de dados.
Argumentos default []
<br/>
optional arguments:<br/>
<ul>
  <li>-h, --help   show this help message and exit</li>
  <li>-e AMBIENTE  [dev], hml ou prd</li>
  <li>-d DATABASE  [seguros_db] ou assistencia_db</li>
  <li>-c CATEGORY  [ab] ou abs</li>
  <li>-t TABLES    uma ou mais tabelas separadas por vírgula</li>
</ul>