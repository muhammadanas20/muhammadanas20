CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE chunks (
  id UUID PRIMARY KEY,
  doc_id UUID NOT NULL,
  tenant_id TEXT NOT NULL,
  body TEXT NOT NULL,
  embedding vector(768) NOT NULL
);

CREATE INDEX chunks_hnsw ON chunks USING hnsw (embedding vector_cosine_ops);
CREATE INDEX chunks_tenant ON chunks (tenant_id);
