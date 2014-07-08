<h1>Hibernate with Hazelcast as Second Level Cache</h1>


<h2>Prerequisites</h2>
You should have installed Apache Maven(http://maven.apache.org/download.cgi).

It would be great if you also have installed Python 2x(https://www.python.org/downloads/) on your system.

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