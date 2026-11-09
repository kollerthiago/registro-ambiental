"""Roda os SQLs do Módulo 3 sem precisar instalar um servidor."""
from pathlib import Path
import sqlite3

pasta = Path(__file__).resolve().parent
with sqlite3.connect(":memory:") as banco:
    banco.execute("PRAGMA foreign_keys = ON")
    banco.executescript((pasta / "01_estrutura.sql").read_text(encoding="utf-8"))
    banco.executescript((pasta / "02_operacoes.sql").read_text(encoding="utf-8"))

    registros = banco.execute("""
        SELECT r.id, t.nome, r.local, r.descricao
        FROM registros r JOIN tipos_problema t ON t.id = r.tipo_id
        ORDER BY r.id
    """).fetchall()
    assert len(registros) == 1, "INSERT ou DELETE não funcionou"
    assert registros[0][3] == "Materiais descartados ao lado da calçada", "UPDATE não funcionou"

    try:
        banco.execute("INSERT INTO registros(tipo_id, local, descricao) VALUES (999, 'Teste', 'Teste')")
    except sqlite3.IntegrityError:
        print("Restrição de chave estrangeira: OK")
    else:
        raise AssertionError("A chave estrangeira não foi respeitada")

    print("CREATE TABLE, INSERT, SELECT, UPDATE e DELETE: OK")
    print("Registros após o teste:")
    for codigo, tipo, local, descricao in registros:
        print(f"{codigo} | {tipo} | {local} | {descricao}")
