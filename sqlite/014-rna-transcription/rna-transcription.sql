-- Schema: CREATE TABLE "rna-transcription" ("dna" TEXT, "result" TEXT);
-- Task: update the rna-transcription table and set the result based on the dna field.
UPDATE "rna-transcription"
SET result = (
  SELECT
    REPLACE(
    REPLACE(
    REPLACE(
    REPLACE(
    REPLACE(
      dna, 'A', 'U'),
      'T', 'A'),
      'C', 'X'),
      'G', 'C'),
      'X', 'G')
  );
