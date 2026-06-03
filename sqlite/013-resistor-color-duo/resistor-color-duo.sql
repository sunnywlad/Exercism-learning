-- Schema: CREATE TABLE "color_code" ("color1" TEXT, "color2" TEXT, "result" INT);
-- Task: update the color_code table and set the result based on the two colors.
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
  FROM splitter
  ),
coloring(color1, color2, x1, x2) AS (
  SELECT
    color1,
    color2,
    p1.color_number,
    p2.color_number
  FROM parser AS p1, parser AS p2, color_code
  WHERE p1.color_name = color_code.color1 AND p2.color_name = color_code.color2
)
UPDATE "color_code"
SET result = (
  SELECT x1 * 10 + x2
  FROM coloring
  WHERE color_code.color1 = coloring.color1
    AND color_code.color2 = coloring.color2);
