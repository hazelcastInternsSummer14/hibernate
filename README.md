<h1>Hibernate 2nd Level Cache with Hazelcast</h1>
In this repository, you can find a sample implementation of hibernate 2nd level cache with hazelcast. You can also find detailed explanation at http://hazelcast.com/use-cases/hibernate-2nd-level/ 

<h2>Prerequisites</h2>
You should have installed Apache Maven(http://maven.apache.org/download.cgi).

<h2>How to Run Sample Application</h2>

1) clone the repository to your local using:
```
git clone https://github.com/hazelcastInternsSummer14/hibernate4.git
```
2) go to "hibernate4" folder

3) Compile project using:
```
mvn compile
```
4) Create database using:
```
mvn exec:java -Dexec.mainClass="createDB"
```
5) After running the following code, you can add or delete employees. Start with writing help in the application:
```
mvn exec:java -Dexec.mainClass="ManageEmployee"
```