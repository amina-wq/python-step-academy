--PostgreSQL dialect
CREATE TABLE Person (
    person_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    middle_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(15),
    e_mail VARCHAR(100),
    address_id INT
);

CREATE TABLE Address (
    address_id SERIAL PRIMARY KEY,
    country VARCHAR(50),
    state VARCHAR(50),
    city VARCHAR(50),
    street VARCHAR(100),
    postal_code VARCHAR(10)
);

CREATE TABLE Student (
    student_id SERIAL PRIMARY KEY,
    person_id INT,
    group_number VARCHAR(10),
    average_mark FLOAT,
    scholarship DECIMAL(10, 2),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);

CREATE TABLE Teacher (
    teacher_id SERIAL PRIMARY KEY,
    person_id INT,
    grade VARCHAR(10),
    salary DECIMAL(10, 2),
    FOREIGN KEY (person_id) REFERENCES Person(person_id)
);
