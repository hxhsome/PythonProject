select name as DATABASE_NAME, serverproperty(N'collation') AS VALUE, 'create database database1'  CREATE_DATABASE  from sys.databases;
go
select name as DATABASE_NAME from sys.databases;
go

update book set id = 1,name = '张三' where id = (select id from book);
