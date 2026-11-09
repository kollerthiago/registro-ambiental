-- Modelo simples para os registros ambientais.
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tipos_problema (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS registros (
  id INTEGER PRIMARY KEY,
  tipo_id INTEGER NOT NULL,
  local TEXT NOT NULL CHECK(length(trim(local)) BETWEEN 1 AND 100),
  descricao TEXT NOT NULL CHECK(length(trim(descricao)) BETWEEN 1 AND 400),
  data_registro TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (tipo_id) REFERENCES tipos_problema(id)
);
