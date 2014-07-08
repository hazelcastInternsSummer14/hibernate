import java.util.List;
import java.util.Iterator;
import java.util.Scanner;
import org.hibernate.Session;
import org.hibernate.Transaction;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

/**
 * Created by Esref Ozturk <esrefozturk93@gmail.com> on 26.06.2014.
 */

public class ManageEmployee {
    private static SessionFactory factory;
    private static Session session;
    private static Transaction tx;
    private static Scanner reader;
    private static String command;

    public static void main(String[] args) {
        try{
            factory = new Configuration().configure().buildSessionFactory();
        }catch (Throwable ex) {
            System.err.println("Failed to create sessionFactory object." + ex);
            throw new ExceptionInInitializerError(ex);
        }

        reader = new Scanner(System.in);
        session = factory.openSession();
        tx = session.beginTransaction();

        for(;;){
            System.out.print("command: ");
            command = reader.nextLine();
            if( command.equals("list") ){
                List employees = session.createQuery("FROM Employee").list();
                for (Iterator iterator =
                             employees.iterator(); iterator.hasNext();){
                    Employee employee = (Employee) iterator.next();
                    System.out.print("First Name: " + employee.getFirstName());
                    System.out.print("  Last Name: " + employee.getLastName());
                    System.out.println("  Salary: " + employee.getSalary());
                }
            }
            else if( command.equals("add") ){
                System.out.print("Id: ");
                int id = reader.nextInt();
                reader.nextLine();
                System.out.print("First Name: ");
                String fname = reader.nextLine();
                System.out.print("Last Name: ");
                String lname = reader.nextLine();
                System.out.print("Salary: ");
                int salary = reader.nextInt();
                reader.nextLine();
                Employee employee = new Employee(id,fname, lname, salary);
                int employeeID = (Integer) session.save(employee);
                System.out.println("EmployeeID: "+employeeID);
            }
            else if( command.equals("delete") ){
                System.out.print("EmployeeID: ");
                int employeeId = reader.nextInt();
                reader.nextLine();
                Employee employee = (Employee)session.get(Employee.class, employeeId);
                session.delete(employee);
            }
            else if( command.equals("close") ){
                tx.commit();
                session.close();
            }
            else if( command.equals("open") ){
                session = factory.openSession();
                tx = session.beginTransaction();
            }
            else if( command.equals("help") ){
                System.out.println("help         this menu");
                System.out.println("list         list all employees");
                System.out.println("add          add an employee");
                System.out.println("delete       delete and employee");
                System.out.println("open         open session and begin transaction");
                System.out.println("close        commit transaction and close session");

            }
            else if( command.equals("quit") ) {
                tx.commit();
                session.close();
                factory.close();
                break;
            }
            else{
                System.out.println("command not found. Use help menu");
            }
        }


    }

}