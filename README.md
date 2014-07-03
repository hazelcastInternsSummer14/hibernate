<h1>ABOUT</h1>
This project is prepared to serve as a sample application for Hazelcast, the leading open source in-memory data grid . Here, Hazelcast's use case is Hibernate.

<h2>Prerequisites</h2>
You should have installed Apache Maven(http://maven.apache.org/download.cgi) and MySQL Server(http://dev.mysql.com/downloads/mysql/) on your system.

<h2>How to Run Sample Application</h2>

1) create database named "hibernate" using:
```
mysql -u USERNAME -pPASSWORD -e 'create database hibernate;'
```
2) create table name "EMPLOYEE" using:
```
mysql -u USERNAME -pPASSWORD -D hibernate -e 'create table EMPLOYEE ( id INT NOT NULL auto_increment, first_name VARCHAR(20) default NULL, last_name  VARCHAR(20) default NULL, salary INT default NULL, PRIMARY KEY (id) );'
```
3) clone the repository to your local using:
```
git clone https://github.com/hazelcastInternsSummer14/hibernate4.git
```
4) go to hibernate4 folder

5) run the code: 
```
mvn compile
```
 