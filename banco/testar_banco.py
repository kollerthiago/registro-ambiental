"""Roda os SQLs do Módulo 3 sem precisar instalar um servidor."""
from pathlib import Path
import sqlite3

pasta = Path(__file__).resolve().parent
with sqlite3.connect(":memory:") as banco:
    banco.executescript((pasta / "01_estrutura.sql").read_text(encoding="utf-8"))

    # Registro anterior usado para verificar que o exemplo preserva outros dados.
    banco.execute("INSERT INTO tipos_problema (id, nome) VALUES (1, 'Outro')")
    banco.execute("""
        INSERT INTO registros (tipo_id, local, descricao)
        VALUES (1, 'Local anterior', 'Descrição anterior')
    """)

    banco.executescript((pasta / "02_operacoes.sql").read_text(encoding="utf-8"))
    registros = banco.execute("""
        SELECT t.nome, r.local, r.descricao, r.data_registro
        FROM registros AS r
        JOIN tipos_problema AS t ON t.id = r.tipo_id
        ORDER BY r.id
    """).fetchall()
    assert [linha[:3] for linha in registros] == [
        ("Outro", "Local anterior", "Descrição anterior"),
        ("Descarte irregular", "Avenida Exemplo, esquina",
         "Materiais descartados ao lado da calçada"),
    ], "O CRUD deve preservar o registro anterior e deixar só um exemplo"
    assert all(linha[3] for linha in registros), "A data deve ser preenchida"
    assert {nome for (nome,) in banco.execute("SELECT nome FROM tipos_problema")} == {
        "Lixo acumulado", "Descarte irregular", "Entulho na rua", "Outro"
    }, "As categorias devem corresponder ao formulário"

    casos_invalidos = [
        ("Chave estrangeira", 999, "Local", "Descrição", sqlite3.SQLITE_CONSTRAINT_FOREIGNKEY),
        ("Campo obrigatório", 1, None, "Descrição", sqlite3.SQLITE_CONSTRAINT_NOTNULL),
        ("Local vazio", 1, "   ", "Descrição", sqlite3.SQLITE_CONSTRAINT_CHECK),
        ("Local acima de 100 caracteres", 1, "x" * 101, "Descrição", sqlite3.SQLITE_CONSTRAINT_CHECK),
        ("Descrição acima de 400 caracteres", 1, "Local", "x" * 401, sqlite3.SQLITE_CONSTRAINT_CHECK),
    ]
    for nome, tipo_id, local, descricao, erro_esperado in casos_invalidos:
        try:
            banco.execute(
                "INSERT INTO registros (tipo_id, local, descricao) VALUES (?, ?, ?)",
                (tipo_id, local, descricao),
            )
        except sqlite3.IntegrityError as erro:
            assert erro.sqlite_errorcode == erro_esperado, f"Restrição inesperada em {nome}"
            print(f"{nome}: OK")
        else:
            raise AssertionError(f"Restrição ignorada: {nome}")

    print("CREATE TABLE, INSERT, SELECT, UPDATE e DELETE: OK")
    print("Ocorrência fictícia após o teste:")
    print(" | ".join(registros[1][:3]))
