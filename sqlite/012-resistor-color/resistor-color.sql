-- CREATE TABLE "color_code" ("color" TEXT, "result" INT);
-- Task: update the color_code table and set the result based on the color.

WITH RECURSIVE
raw(pasted) AS (
  VALUES(
'black: 0
brown: 1
red: 2
orange: 3
yellow: 4
green: 5
blue: 6
violet: 7
grey: 8
white: 9')),
splitter(line, rest) AS (
  SELECT
    SUBSTR(raw.pasted, 1, (INSTR(raw.pasted, char(10)) - 1)),
    SUBSTR(raw.pasted, (INSTR(raw.pasted, char(10)) + 1))
  FROM raw
  UNION ALL
  SELECT
    SUBSTR(rest, 1, (INSTR(rest || char(10), char(10)) - 1)),
    SUBSTR(rest, (INSTR(rest || char(10), char(10)) + 1))
  FROM splitter
  WHERE rest != ''
  ),
parser(color_name, color_number) AS (
  SELECT
    SUBSTR(line, 1, (INSTR(line, ':') - 1)),
    SUBSTR(line, (INSTR(line, ':') + 2))
  FROM splitter)
UPDATE "color_code"
SET result = (
  SELECT color_number FROM parser
  WHERE parser.color_name = color_code.color
);
