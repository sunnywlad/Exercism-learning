-- Schema:
-- CREATE TABLE "bottle-song" (
--         start_bottles INTEGER NOT NULL,
--         take_down     INTEGER NOT NULL,
--         result        TEXT
-- );
-- Task: update bottle-song table and set the result based on the
-- start_bottles and take_down.
UPDATE "bottle-song"
SET result = (
  WITH RECURSIVE
    lookup(num, word) AS (VALUES (0, 'no'), (1, 'one'), (2, 'two'), (3, 'three'),
                        (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven'),
                        (8, 'eight'), (9, 'nine'), (10, 'ten')),
    verse_number AS (
      SELECT start_bottles AS count
      UNION ALL
      SELECT count - 1
      FROM verse_number WHERE count > start_bottles - take_down + 1
    )
  SELECT group_concat(
    (SELECT UPPER(SUBSTR(word, 1, 1)) || SUBSTR(word, 2) FROM lookup WHERE num = count) ||
    ' green ' ||
    CASE WHEN count = 1 THEN 'bottle' ELSE 'bottles' END ||
    ' hanging on the wall,' || char(10) ||
    (SELECT UPPER(SUBSTR(word, 1, 1)) || SUBSTR(word, 2) FROM lookup WHERE num = count) ||
    ' green ' ||
    CASE WHEN count = 1 THEN 'bottle' ELSE 'bottles' END ||
    ' hanging on the wall,' || char(10) ||
    'And if one green bottle should accidentally fall,'|| char(10) ||
    'There''ll be ' ||
    (SELECT word FROM lookup WHERE num = count - 1) ||
    ' green ' ||
    CASE WHEN count - 1 = 1 THEN 'bottle' ELSE 'bottles' END ||
    ' hanging on the wall.',
  char(10) || char(10))
  FROM verse_number
);
