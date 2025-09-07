CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT DISTINCT salary
        FROM Employee e1
        WHERE N = (
            SELECT COUNT(DISTINCT salary)
            FROM Employee e2
            WHERE e2.salary >= e1.salary
        )
        LIMIT 1
    );
END;
