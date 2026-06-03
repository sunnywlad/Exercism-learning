-- Schema: CREATE TABLE "grains" ("task" TEXT, "square" INT, "result" INT);
-- Task: update the grains table and set the result based on the task (and square fields).
WITH RECURSIVE cumulate(square, grains_on_sq, total_cumulate) AS (
  SELECT 1, 1, 1
  UNION ALL
  SELECT square + 1, grains_on_sq * 2, CAST((total_cumulate + grains_on_sq * 2) AS REAL) FROM cumulate
  WHERE square < 64)
UPDATE "grains"
SET result = (
  SELECT CASE
    WHEN "task" = 'single-square' THEN
      (SELECT grains_on_sq FROM cumulate WHERE cumulate.square = grains.square)
    WHEN "task" = 'total' THEN
      (SELECT total_cumulate FROM cumulate WHERE square = 64)
    END);
