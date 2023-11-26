-- procedure computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS Users,
        (SELECT Users.id, SUM(score * weight) / SUM(weight) AS weight_avg
        FROM users AS Users
        JOIN corrections as Corr ON Users.id=Corr.user_id
        JOIN projects AS Proj ON Corr.project_id=Proj.id
        GROUP BY Users.id)
    AS WeightAverage
    SET Users.average_score = WeightAverage.weight_avg
    WHERE Users.id=WeightAverage.id;
END
$$
DELIMITER ;
