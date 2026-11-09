-- Dados fictícios somente para demonstrar as operações do banco.
PRAGMA foreign_keys = ON;

INSERT OR IGNORE INTO tipos_problema (nome) VALUES
  ('Lixo acumulado'),
  ('Descarte irregular'),
  ('Entulho na rua');

-- INSERT: cadastro de duas ocorrências de exemplo.
INSERT INTO registros (tipo_id, local, descricao) VALUES
  ((SELECT id FROM tipos_problema WHERE nome = 'Lixo acumulado'),
   'Rua Exemplo, próximo à praça', 'Sacos de lixo na calçada'),
  ((SELECT id FROM tipos_problema WHERE nome = 'Descarte irregular'),
   'Avenida Exemplo, esquina', 'Materiais deixados ao lado da via');

-- SELECT: consulta dos registros com a categoria correspondente.
SELECT r.id, t.nome AS tipo, r.local, r.descricao
FROM registros AS r
JOIN tipos_problema AS t ON t.id = r.tipo_id
ORDER BY r.id;

-- UPDATE: correção de uma descrição.
UPDATE registros
SET descricao = 'Materiais descartados ao lado da calçada'
WHERE id = (SELECT MAX(id) FROM registros);

-- DELETE: exclusão do primeiro registro de exemplo.
DELETE FROM registros
WHERE id = (SELECT MIN(id) FROM registros);

-- SELECT: situação final após as alterações.
SELECT r.id, t.nome AS tipo, r.local, r.descricao
FROM registros AS r
JOIN tipos_problema AS t ON t.id = r.tipo_id
ORDER BY r.id;
