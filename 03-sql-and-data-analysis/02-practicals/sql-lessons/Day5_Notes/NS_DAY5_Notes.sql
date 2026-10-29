select student_id,count(*) as total_records,count(distinct marks)  as distinct_marks
from exams
where subject in ('Chemistry','Physics')
group by student_id
having count(*)=2 and count(distinct marks)=1
;
select student_id,marks , count(1) as total_rows
from exams
where subject in ('Chemistry','Physics')
group by student_id,marks 
having count(1)=2
order by student_id;
-------------------------------------------------
-- create table returns (order_id  varchar(10),return_reason varchar(10));
-- insert into returns select * from returns_backup;

-- Database Joins
------------------------------------------------------------------------------
-- 1. Inner Join
select o.order_id,o.product_id,r.return_reason
from orders o
inner join returns r on o.order_id=r.order_id;

select r.return_reason,sum(sales) as total_sales
from orders o
inner join returns r on o.order_id=r.order_id
group by r.return_reason;

-- 2. Left Join
select o.order_id,o.product_id,r.return_reason, r.order_id as return_order_id
from orders o
left join returns r on o.order_id=r.order_id;

-- 3. Right Join
select o.order_id,o.product_id,r.return_reason, r.order_id as return_order_id
from orders o
right join returns r on o.order_id=r.order_id;

-- 4. Full Outer Join
select o.order_id,o.product_id,r.return_reason, r.order_id as return_order_id
from orders o
full outer join returns r on o.order_id=r.order_id;

-- Table Creation --
-------------------------------------------------------------------------------
-- Employee
create table employee(
    emp_id int,
    emp_name varchar(20),
    dept_id int,
    salary int,
    manager_id int,
    emp_age int
);

-- Data Insertion
insert into employee values(1,'Ankit',100,10000,4,39);
insert into employee values(2,'Mohit',100,15000,5,48);
insert into employee values(3,'Vikas',100,10000,4,37);
insert into employee values(4,'Rohit',100,5000,2,16);
insert into employee values(5,'Mudit',200,12000,6,55);
insert into employee values(6,'Agam',200,12000,2,14);
insert into employee values(7,'Sanjay',200,9000,2,13);
insert into employee values(8,'Ashish',200,5000,2,12);
insert into employee values(9,'Mukesh',300,6000,6,51);
insert into employee values(10,'Rakesh',500,7000,6,50);

-- Departmemt
create table dept(
    dep_id int,
    dep_name varchar(20)
);

-- Data Insertion
insert into dept values(100,'Analytics');
insert into dept values(200,'IT');
insert into dept values(300,'HR');
insert into dept values(400,'Text Analytics');

select * from employee;
select * from dept;

-- 5. Cross Join
select * 
from 
employee,dept;

select * 
from employee 
inner join dept
on 1=1; -- Any always true condition

-- Inner Join
select e.emp_id,e.emp_name,e.dept_id,d.dep_name from 
employee e
inner join dept d on e.dept_id=d.dep_id;

-- Left Join
select e.emp_id,e.emp_name,e.dept_id,d.dep_name from 
employee e
left join dept d on e.dept_id=d.dep_id

-- Right Join
select e.emp_id,e.emp_name,e.dept_id,d.dep_id,d.dep_name from 
employee e
right join dept d on e.dept_id=d.dep_id;

-- Same as Right Join  by just swapping the table
select e.emp_id,e.emp_name,e.dept_id,d.dep_name from 
dept d
left join employee e on e.dept_id=d.dep_id;

-- Full Outer Join
select e.emp_id,e.emp_name,e.dept_id,d.dep_id ,d.dep_name from 
dept d
full outer join employee e on e.dept_id=d.dep_id;

select * from employee;
select * from dept;



-- Table Creation

-- People
create table people
(
manager varchar(20),
region varchar(10)
);

-- Insertion
insert into people
values ('Ankit','West')
,('Deepak','East')
,('Vishal','Central')
,('Sanjay','South');

select * from people;

-- Two Joins in the same query
select o.order_id,o.product_id,r.return_reason,p.manager
from orders o
left join returns r on o.order_id=r.order_id
inner join people p on o.region=p.region;




















