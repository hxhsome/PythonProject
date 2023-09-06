CREATE
DEFINER=`hxh`@`%` PROCEDURE `doinsert`()
begin
 declare
i int;set
i = 0;
while
(i<=200) do
  INSERT INTO `hxhtest1`( `id`) VALUES (i);
  set
i = i+1;
end while;
end;


SELECT
	u.user_uuid uuid,
	u.phone phone,
	u.email,
	u.create_time,
	r.role_name
FROM
	secfort.public.secfort_user u
	left JOIN secfort.secfort_role r ON u.role_id = r.role_id;

INSERT INTO `book` VALUES (1, '计算机操作系统11', '978-7-5606-3350-31111', 'T 工业技术111', '汤小丹', '西安电子科技大学出版社', 54.00, '五号架', '本书共分9章:第1章概述操作系统的定义、功能、特性、发展过程和结构;第2章至第7章介绍进程与线程的基本概念、处理机调度、进程同步与死锁、存储管理、文件系统和设备管理;第8章介绍操作系统的安全性;第9章给出操作系统实验指导。', 10, 8);

update book set price = 23 where id = 1 and name = '123';

delete from book where id = 1 and name = '123';

select * from a where id in (select id from b);

select * from (select * from b);

SELECT
 T.user_account,
 T.user_name
FROM
 ( SELECT user_uuid, user_account, user_name, email FROM secfort_user ) T
 LIMIT 5;