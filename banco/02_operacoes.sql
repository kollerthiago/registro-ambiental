-- Dados fictícios somente para demonstrar as operações do banco.
PRAGMA foreign_keys = ON;
BEGIN;

INSERT OR IGNORE INTO tipos_problema (nome) VALUES
  ('Lixo acumulado'),
  ('Descarte irregular'),
  ('Entulho na rua'),
  ('Outro');

-- INSERT: cadastro de uma ocorrência de exemplo.
INSERT INTO registros (tipo_id, local, descricao) VALUES
  ((SELECT id FROM tipos_problema WHERE nome = 'Descarte irregular'),
   'Avenida Exemplo, esquina', 'Materiais deixados ao lado da via');

-- SELECT: consulta da ocorrência recém-inserida com sua categoria.
SELECT r.id, t.nome AS tipo, r.local, r.descricao, r.data_registro
FROM registros AS r
JOIN tipos_problema AS t ON t.id = r.tipo_id
WHERE r.id = last_insert_rowid();

-- UPDATE: correção da descrição da ocorrência recém-inserida.
UPDATE registros
SET descricao = 'Materiais descartados ao lado da calçada'
WHERE id = last_insert_rowid();

-- INSERT e DELETE: cadastro e exclusão de outra ocorrência de exemplo.
INSERT INTO registros (tipo_id, local, descricao) VALUES
  ((SELECT id FROM tipos_problema WHERE nome = 'Lixo acumulado'),
   'Rua Exemplo, próximo à praça', 'Sacos de lixo na calçada');

DELETE FROM registros
WHERE id = last_insert_rowid();

-- SELECT: situação final após as alterações.
SELECT r.id, t.nome AS tipo, r.local, r.descricao, r.data_registro
FROM registros AS r
JOIN tipos_problema AS t ON t.id = r.tipo_id
ORDER BY r.id;

COMMIT;
