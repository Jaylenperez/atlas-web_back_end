-- Creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE average_score_var FLOAT;

    -- Calculate the average score
    SELECT AVG(score) INTO average_score_var FROM corrections WHERE user_id = user_id;

    -- Update the user's average score
    UPDATE users SET average_score = average_score_var WHERE id = user_id;
END //

DELIMITER ;