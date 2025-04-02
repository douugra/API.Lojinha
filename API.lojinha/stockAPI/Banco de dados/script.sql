create DATABASE stock;
use stock;

create table products (
 id int(10) unsigned not null auto_increment,
    name varchar(50) not null,
    cost decimal(10,2) not null,
    price decimal(10,2) not null,
    primary key (`id`)
    )