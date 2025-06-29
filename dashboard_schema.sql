-- SQL Schema for Dashboard
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    roll_number VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50),
    semester VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    course_code VARCHAR(20),
    course_name VARCHAR(100),
    grade CHAR(1),
    credits INT,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
