# Banco de dados — Registro Ambiental

Banco de dados de demonstração para o Módulo 3 do Projeto Integrador de Tecnologia da Informação II.

## Modelo
- `tipos_problema`: id (chave primária) e nome (único).
- `registros`: id (chave primária), tipo_id (chave estrangeira), local, descricao e data_registro.
- Um tipo de problema pode estar ligado a vários registros (relação 1:N).

## Arquivos
- `01_estrutura.sql`: cria as tabelas e restrições.
- `02_operacoes.sql`: apresenta INSERT, SELECT, UPDATE e DELETE com dados de exemplo.
- `testar_banco.py`: executa os SQLs com SQLite e confere as operações.

## Teste
Na pasta raiz do repositório, execute:

```bash
python banco/testar_banco.py
```

O programa utiliza o SQLite disponível no Python e não exige servidor.

**Observação:** a página web original continua usando `localStorage`. Os scripts SQLite demonstram a modelagem e as operações de banco de dados desta etapa; o site ainda não se conecta diretamente ao SQLite. Os endereços dos exemplos são fictícios.
