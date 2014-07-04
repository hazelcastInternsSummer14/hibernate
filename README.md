<h1>ABOUT</h1>
This project is prepared to serve as a sample application for Hazelcast, the leading open source in-memory data grid . Here, Hazelcast's use case is Hibernate.

<h2>Prerequisites</h2>
You should have installed Apache Maven(http://maven.apache.org/download.cgi) and MySQL Server(http://dev.mysql.com/downloads/mysql/) on your system.

It would be great if you also have installed Python 2x(https://www.python.org/downloads/) on your system.

<h2>How to Run Sample Application</h2>

1) create database named "hibernate" using the following command after replacing USERNAME and PASSWORD with yours:
```
mysql -u USERNAME -pPASSWORD -e 'create database hibernate;'
```
2) create table named "EMPLOYEE" using the following command after replacing USERNAME and PASSWORD with yours:
```
mysql -u USERNAME -pPASSWORD -D hibernate -e 'create table EMPLOYEE ( id INT NOT NULL auto_increment, first_name VARCHAR(20) default NULL, last_name  VARCHAR(20) default NULL, salary INT default NULL, PRIMARY KEY (id) );'
```
3) clone the repository to your local using:
```
git clone https://github.com/hazelcastInternsSummer14/hibernate4.git
```
4) go to "hibernate4" folder

5) change "hibernate.connection.username" and "hibernate.connection.password" fields in "src/main/resources/hibernate.cfg.xml" file according to your mysql configurations

6) run: 
```
mvn compile
```
7) Create a hazelcast instance by running:
```
mvn exec:java -Dexec.mainClass="Hz"
```
8) After running the following code in different terminal, you can add or delete employees. Start with writing help in the application:
```
mvn exec:java -Dexec.mainClass="ManageEmployee"
```
9) add some employees but do not commit. After creating second hazelcast instance, shutdown first instance. Even now you should be able to commit you changes to database. You can see the employees in the database using:
```
mysql -u USERNAME -pPASSWORD -D hibernate -e 'select * from EMPLOYEE;'
```
10) You can also edit "src/main/resources/hazelcast.xml" file using "src/main/resources/hazelcast_conf.py" script.
