create table employees(
employee_Id serial primary key,
	first_name text not null,
	last_name text not null,
	salary numeric not null
);

insert into employees(first_name,last_name,salary) values ('Marian','Paździoch',10000);
insert into employees(first_name,last_name,salary) values ('Arnold','Boczek',6000);
insert into employees(first_name,last_name,salary) values ('Ferdynand','Kiepski',2000);

select * from employees;

create table products(
product_id serial primary key,
	name text not null,
	price numeric not null,
	description text
);

insert into products (name,price,description) values ('Granatnik RWG-95',2137,'Do strzelania na komendzie ;) ');
insert into products (name,price,description) values ('Bulbulator',1000,'Urządzenie które robi bul bul');
insert into products (name,price,description) values ('Wihajster',100,'Takie coś z takim czymś bez takiego czegoś');

select * from products;