drop database if exists ISEER;

/* CREATE DATABASE BY THE NAME IntegritySEER */
create database ISEER;

/* CHOOSE OUR DATABASE */
use ISEER;

Create table Employee(
	EmpID int (5) not null,
	FirstName varchar(20),
	LastName varchar(20),
	Sex char (6),
	DOB Date,
	Email varchar (30),
	Department varchar (25),
	JobTitle varchar(25),
	HireDate Date,
	Supervisor varchar (30),
	EmpType varchar (25),
	Primary Key(EmpID) 
)engine=INNODB;

Create table Department(
	DeptID varchar (5) not null,
	DeptName varchar (25),
	Primary Key (DeptID),
	Unique Key (DeptName)
)engine = INNODB;

Create table Supervisor(
	SupID int(5),
	EmpID int (5),
	Primary Key (SupID,EmpID),
	Foreign Key (EmpID) References Employee (EmpID), 
	Foreign Key (EmpID) References Employee (EmpID) 
)engine = INNODB;


Create table Dept_Manager(
	DeptID varchar (5),
	EmpID int (5),
	ApptDate Date,
	RsgnDate Date,
	Primary Key (DeptID,EmpID),
	Foreign Key (DeptID) References Department (DeptID) On Delete Cascade On Update Cascade,
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade
)engine = INNODB;

Create table Works_In(
	EmpID int (5),
	DeptID varchar (5),
	ApptDate Date,
	RsgnDate Date,
	Primary Key (EmpID,DeptID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade,
	Foreign Key (DeptID) References Department (DeptID) On Delete Cascade On Update Cascade
)engine = INNODB;


Create table Evaluation(
	EmpID int (5),
	KPIAssessment varchar (10),
	Compentencies varchar (10),
	Anchors varchar (10),
	Recommendations varchar (100),
	Review varchar (100),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade   

)engine = INNODB;


Create table Perform(
	EmpID int (5),
	Period Date,
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade
)engine  INNODB;	

Create table KPIAssessment(
	EmpID int (5),
	kpi_one varchar (50),
    myeval_1 varchar (50),
    supereval_1 varchar (50),
    mycom_1 varchar (50),
    supercom_1 varchar (50),
    
	kpi_two varchar (50),
    myeval_2 varchar (50),
    supereval_2 varchar (50),
    mycom_2 varchar (50),
    supercom_2 varchar (50),

    kpi_three varchar (50),
    myeval_3 varchar (50),
    supereval_3 varchar (50),
    mycom_3 varchar (50),
    supercom_3 varchar (50),

    kpi_four varchar (50),
    myeval_4 varchar (50),
    supereval_4 varchar (50),
    mycom_4 varchar (50),
    supercom_4 varchar (50),

    kpi_five varchar (50),
    myeval_5 varchar (50),
    supereval_5 varchar (50),
    mycom_5 varchar (50),
    supercom_5 varchar (50),

	kpi_six varchar (50),
    myeval_6 varchar (50),
    supereval_6 varchar (50),
    mycom_6 varchar (50),
    supercom_6 varchar (50),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade   
)engine = INNODB;


Create table Competencies(
	EmpID int (3), 
	JobKnowledge varchar (50),
	CustomerService varchar (50),
	Communication varchar (50),
	Decisions varchar (50),
	Initiative varchar (50),
	Lead varchar (50),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee(EmpID) On Delete Cascade On Update Cascade	 
)engine = INNODB;


Create table Anchors(
	EmpID int (5),
	Punctuality varchar (50),
	Dependability varchar (50),
	Adaptability varchar (50),
	Personality varchar (50),
	Teamwork varchar (50),
	Cooperate varchar (50),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade   
)engine = INNODB;


Create table Recommendations(
	EmpID int (5),
    Assessment1 varchar (50),
	Assessment2 varchar (50),
	Assessment3 varchar (50),
	Assessment4 varchar (50),
	Assessment5 varchar (50),
	Assessment6 varchar (50),
	ProblemSolving varchar(50),
	Punctual varchar(50),
	Personality varchar (50),
	Teamwork varchar (50),
	Promotion varchar (50),
	Training varchar (50),
	NoChange varchar (50),
	Demotion varchar (50),
	Dismissal varchar (50),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade   
)engine = INNODB;	


Create table Review(
	EmpID int (5),
	KPIs varchar (50),
	Competencies varchar (50),
	Anchors varchar (50),
	Strengths varchar (50),
	Improvement varchar(50),
	Training varchar (50),
	EmployeeComments varchar(50),
	FutureGoals varchar (50),
	Confirm varchar (50),
	Primary Key (EmpID),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade   
)engine = INNODB;


Create table ReviewPeriod(
	EmpID int (5),
	Period Date,
	Primary Key (EmpID, Period),
	Foreign Key (EmpID) References Employee (EmpID) On Delete Cascade On Update Cascade
)engine = INNODB;
	
	
	
Create table users(
	Id int (3) AUTO_INCREMENT,
	EmpId int (5),
	Password varchar (20),
	Role varchar (25),
	Primary Key (Id),
	Unique (EmpId)
)engine = INNODB;
	

Insert into Employee values (10001,'Shereen','Brown','F','1975-09-10','shereenbrown@gmail.com','Financial Analysis','Senior Financial Analyst','2012-08-25','Remace Jourdine', 'Permanent');
Insert into Employee values (10002,'Miguel','Crowley','M','1985-01-11','miguelcrowley@gmail.com ','Financial Investigations','Chief Financial Investigator','2015-06-15','Remace Jourdine','Permanent');
Insert into Employee values (10003,'Jensen','Ackles','M','1980-11-11','jensenackles@gmail.com ','Financial Investigations','Financial Investigator','2018-01-06' ,'Remace Jourdine', 'Contract');
Insert into Employee values (10005,'Karen','Dacres','F','1980-11-11','karendacres@gmail.com ', 'Human Resources','Corporate Services Manager','2017-12-12' ,'Remace Jourdine','Permanent');
Insert into Employee values (10004,'Shavan','Bulli','M','1990-08-10','shavanbulli@gmail.com ', 'Human Resources','Data Entry Clerk','2018-08-25' ,'Remace Jourdine', 'Contract');
Insert into Employee values (10006,'Antonio','Grossett','M','1982-01-18','antoniogrossett@gmail.com ', 'Human Resources','Data Systems Analyst ','2015-06-15' ,'Remace Jourdine','Contract');
Insert into Employee values (10007,'Jerome','Bent','M','1980-11-11','jeromebent@gmail.com ','Financial Analysis','Financial Analyst','2018-01-06' ,'Remace Jourdine', 'Contract');
Insert into Employee values (10008,'Delton','Jenisson','M','1980-11-11','deltonjenisson@gmail.com ','Financial Analysis','Financial Analyst','2017-12-12' ,'Remace Jourdine','Permanent');
Insert into Employee values (10009,'Steph','Freckleton','F','1987-10-15','stephfreckleton@gmail.com ', 'Financial Investigations','Financial Investigator','2013-04-13' ,'Remace Jourdine','Permanent');
Insert into Employee values (10010,'Johnathon','James','M','1989-09-11','1keysuccesss@gmail.com', 'Financial Analysis','Financial Analyst','2014-12-12' ,'Remace Jourdine','Contract');
Insert into Employee values (10012,'Remace','Jourdaine','M','1969-02-25','theiseer@gmail.com ',NULL,'Manager','2014-03-07', NULL,'Permanent');

Insert into Department values ('FA001', 'Financial Analysis');
Insert into Department values ('FI001', 'Financial Investigation');
Insert into Department values ('HR001', 'Human Resources');

Insert into Supervisor values(10012,10004);
Insert into Supervisor values(10012,10006);
Insert into Supervisor values(10012,10003);
Insert into Supervisor values(10012,10009);
Insert into Supervisor values(10012,10008);
Insert into Supervisor values(10012,10010);
Insert into Supervisor values(10012,10007);
Insert into Supervisor values(10012,10001);
Insert into Supervisor values(10012,10002);
Insert into Supervisor values(10012,10005);



Insert into Dept_Manager values('FA001', 10012,'2016-07-29', ' ');
Insert into Dept_Manager values('FI001', 10012,'2016-07-29', ' ');
Insert into Dept_Manager values('HR001', 10012,'2016-07-29', ' ');


Insert into Works_In values(10001,'FA001','2018-04-02', ' ');
Insert into Works_In values(10002,'FI001','2016-01-09', ' ');
Insert into Works_In values(10003,'FI001','2009-03-20', ' ');
Insert into Works_In values(10005,'FA001','2010-07-29', ' ');


Alter table users AUTO_INCREMENT = 01;


Insert into users values (' ', 10012, 'boss','Supervisor');
Insert into users values (' ', 10001, 'myproject','Employee');
Insert into users values (' ', 10005, 'prime','Employee');
Insert into users values (' ', 10002, 'one','Employee');
Insert into users values (' ', 10003, 'win','Employee');
Insert into users values (' ', 10004, 'won','Employee');
Insert into users values (' ', 10006, 'real','Employee');
Insert into users values (' ', 10008, 'fake','Employee');
Insert into users values (' ', 10009, 'soft','Employee');
Insert into users values (' ', 10007, 'hard','Employee');
Insert into users values (' ', 10010, 'push','Employee');



/*=======================QUERIES=============================================*/


Select * From Employee;

Select * From Department;

Select * From users;

Select * From Employee 
Join Works_In On Works_In.EmpID = Employee.EmpID
Join Department on Department.DeptID = Works_In.DeptID;



