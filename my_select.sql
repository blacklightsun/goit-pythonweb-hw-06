-- Create a denormalized table combining scores with student, subject, group, and teacher information

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join groups g on st.group_id = g.id
    left join teachers t on sub.teacher_id = t.id
)
select
    *
from denorm_table;




-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name
        -- ,
        -- sub.name as subject_name,
        -- g.name as group_name,
        -- t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    -- left join subjects sub on scores.subject_id = sub.id
    -- left join groups g on st.group_id = g.id
    -- left join teachers t on sub.teacher_id = t.id
)
select
    denorm_table.student_name,
    avg(denorm_table.score) as avg_score
from denorm_table
GROUP BY denorm_table.student_name
order by avg_score desc
limit 5;


select 
    st.name as student_name,
    avg(scores.score) as avg_score
from scores
    left join students st on scores.student_id = st.id
GROUP BY student_name
order by avg_score desc
limit 5;





-- Знайти студента із найвищим середнім балом з певного предмета.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name
        -- ,
        -- g.name as group_name,
        -- t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    -- left join groups g on st.group_id = g.id
    -- left join teachers t on sub.teacher_id = t.id
)
SELECT
    denorm_table.student_name,
    avg(denorm_table.score) as avg_score
FROM denorm_table
    WHERE denorm_table.subject_name = 'Art'
    GROUP BY denorm_table.student_name
    ORDER BY avg_score DESC
    LIMIT 1;


-- v.2
select 
    st.name as student_name,
    avg(scores.score) as avg_score
from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
WHERE sub.name = 'Art'

GROUP BY student_name
ORDER BY avg_score DESC
LIMIT 1;





-- Знайти середній бал у групах з певного предмета.

with denorm_table as (
    select 
        scores.*,
        -- st.name as student_name,
        sub.name as subject_name,
        g.name as group_name
        -- ,
        -- t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join groups g on st.group_id = g.id
    -- left join teachers t on sub.teacher_id = t.id
)
SELECT
    denorm_table.group_name,
    avg(denorm_table.score) as avg_score
FROM denorm_table
    WHERE denorm_table.subject_name = 'Science'
    GROUP BY denorm_table.group_name
    ORDER BY avg_score DESC;


-- v.2
SELECT
    g.name as group_name,
    avg(scores.score) as avg_score
FROM scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join groups g on st.group_id = g.id
WHERE sub.name = 'Science'
GROUP BY g.name
ORDER BY avg_score DESC;






-- Знайти середній бал на потоці (по всій таблиці оцінок).

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join groups g on st.group_id = g.id
    left join teachers t on sub.teacher_id = t.id
)
SELECT
    denorm_table.group_name,
    avg(denorm_table.score) as avg_score
FROM denorm_table
    -- WHERE denorm_table.subject_name = 'Science'
    GROUP BY denorm_table.group_name
    ORDER BY avg_score DESC;


-- Another solution without CTE

SELECT
    g.name as group_name,
    avg(scores.score) as avg_score
from scores
    left join students st on scores.student_id = st.id
    left join groups g on st.group_id = g.id
GROUP BY group_name
ORDER BY avg_score DESC
;





-- Знайти які курси читає певний викладач.

SELECT
    subjects.name AS subject_name
FROM subjects
    left JOIN teachers t ON subjects.teacher_id = t.id
where t.name = 'Kristi Ford'
;




-- Знайти список студентів у певній групі.

SELECT
    students.name as student_name
FROM students
    left JOIN groups g ON students.group_id = g.id
where g.name = 'Group A'
;




-- Знайти оцінки студентів у окремій групі з певного предмета.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join groups g on st.group_id = g.id
    left join teachers t on sub.teacher_id = t.id
)
select
    denorm_table.student_name,
    denorm_table.score
from denorm_table
where denorm_table.subject_name = 'Mathematics' and denorm_table.group_name = 'Group B'
order by denorm_table.score desc;


-- v.2
SELECT
    st.name AS student_name,
    scores.score AS score
FROM scores
    left join subjects on scores.subject_id = subjects.id
    left join students st on scores.student_id = st.id
    left join groups g on st.group_id = g.id
WHERE subjects.name = 'Mathematics' AND g.name = 'Group B'
ORDER BY scores.score DESC
;





-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
        left join students st on scores.student_id = st.id
        left join subjects sub on scores.subject_id = sub.id
        left join groups g on st.group_id = g.id
        left join teachers t on sub.teacher_id = t.id
)
select
    -- denorm_table.teacher_name,
    avg(denorm_table.score) as average_score
from denorm_table
where denorm_table.teacher_name = 'Kristi Ford'
group by denorm_table.teacher_name
order by average_score desc;


-- v.2
SELECT
    avg(scores.score) as average_score
FROM scores
    left JOIN subjects ON scores.subject_id = subjects.id
    left JOIN teachers ON subjects.teacher_id = teachers.id
WHERE teachers.name = 'Kristi Ford'
;






-- Знайти список курсів, які відвідує певний студент.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
        left join students st on scores.student_id = st.id
        left join subjects sub on scores.subject_id = sub.id
        left join groups g on st.group_id = g.id
        left join teachers t on sub.teacher_id = t.id
)
select
    DISTINCT denorm_table.subject_name
from denorm_table
where denorm_table.student_name = 'Nathan Johnson';


-- v.2
SELECT
    DISTINCT sub.name as subject_name
FROM scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
WHERE st.name = 'Nathan Johnson';







-- Список курсів, які певному студенту читає певний викладач.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
        left join students st on scores.student_id = st.id
        left join subjects sub on scores.subject_id = sub.id
        left join groups g on st.group_id = g.id
        left join teachers t on sub.teacher_id = t.id
)
select
    DISTINCT denorm_table.subject_name
from denorm_table
where denorm_table.student_name = 'Nathan Johnson' and denorm_table.teacher_name = 'Kristi Ford';


-- v.2
SELECT
    DISTINCT sub.name as subject_name
FROM scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join teachers t on sub.teacher_id = t.id
WHERE st.name = 'Nathan Johnson' and t.name = 'Kristi Ford';







-- Середній бал, який певний викладач ставить певному студентові.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name,
        t.name as teacher_name
    from scores
        left join students st on scores.student_id = st.id
        left join subjects sub on scores.subject_id = sub.id
        left join groups g on st.group_id = g.id
        left join teachers t on sub.teacher_id = t.id
)
select
    avg(denorm_table.score) as average_score
from denorm_table
where denorm_table.teacher_name = 'Kristi Ford' and denorm_table.student_name = 'Nathan Johnson';


-- v.2
SELECT
    avg(scores.score) as average_score
FROM scores
    left join students st on scores.student_id = st.id
    left join subjects sub on scores.subject_id = sub.id
    left join teachers t on sub.teacher_id = t.id
WHERE t.name = 'Kristi Ford' and st.name = 'Nathan Johnson';







-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

with denorm_table as (
    select 
        scores.*,
        st.name as student_name,
        sub.name as subject_name,
        g.name as group_name
    from scores
        left join students st on scores.student_id = st.id
        left join subjects sub on scores.subject_id = sub.id
        left join groups g on st.group_id = g.id
    where sub.name = 'Art' and g.name = 'Group B'
)
select
    denorm_table.student_name,
    denorm_table.score
from denorm_table
    where denorm_table.created = (select max(created) from denorm_table)
-- order by denorm_table.created desc;


