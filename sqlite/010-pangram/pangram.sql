-- Schema: CREATE TABLE pangram (sentence TEXT NOT NULL, result BOOLEAN);
-- Task: update pangram table and set result based on sentence.
WITH RECURSIVE
lowered_sent(sent, lw_sent) AS (
  SELECT sentence, LOWER(sentence) FROM pangram
  ),
pangram_detect(sen, lt_code, lt_check) AS (
  SELECT lw_sent, 97, INSTR(lw_sent, CHAR(97)) FROM lowered_sent
  UNION ALL
  SELECT sen, lt_code + 1, INSTR(sen, CHAR(lt_code + 1)) FROM pangram_detect
  WHERE lt_code < 122
  )
UPDATE pangram
SET result =
  CASE
    WHEN (
      SELECT MIN(lt_check) FROM pangram_detect
      WHERE LOWER(pangram.sentence) = pangram_detect.sen) = 0
    THEN 0
    ELSE 1
  END;
