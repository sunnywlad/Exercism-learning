-- Schema: CREATE TABLE "isbn-verifier" (isbn TEXT NOT NULL, result BOOL);
-- Task: update the isbn-verifier table and set the result based on the isbn.
WITH RECURSIVE
  "isbn-filter"(isbn, raw) AS (
    SELECT
      isbn,
      REPLACE(isbn, '-', '') AS raw
    FROM "isbn-verifier"
    WHERE LENGTH(REPLACE(isbn, '-', '')) = 10
    ),
  "isbn-check"(isbn, raw, position, value) AS (
    SELECT
      isbn,
      raw,
      1,
      UNICODE(SUBSTR(raw, 1, 1)) - UNICODE('0')
    FROM "isbn-filter"
    UNION ALL
    SELECT
      isbn,
      raw,
      position + 1,
      CASE
        WHEN position = 9 THEN
          CASE
            WHEN SUBSTR(raw, 10, 1) = 'X' THEN 10
            ELSE UNICODE(SUBSTR(raw, 10, 1)) - UNICODE('0')
          END
        ELSE UNICODE(SUBSTR(raw, position + 1, 1)) - UNICODE('0')
      END AS value
    FROM "isbn-check"
    WHERE position < 10)
UPDATE "isbn-verifier"
SET result = (
  SELECT CASE
    WHEN (SUM(value * (11 - position)) % 11) = 0 THEN 1
    ELSE 0 END
  FROM "isbn-check"
  WHERE "isbn-check".isbn = "isbn-verifier".isbn);
