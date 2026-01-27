import java.util.ArrayList;

import java.util.Scanner;

 

class Student {

    private int roll;

    private String name;

    private double marks;

 

    public Student(int roll, String name, double marks) {

        this.roll = roll;

        this.name = name;

        this.marks = marks;

    }

 

    // Getters & Setters (encapsulation)

    public int getRoll() { return roll; }

    public String getName() { return name; }

    public double getMarks() { return marks; }

 

    public void display() {

        System.out.printf("Roll: %d, Name: %s, Marks: %.2f%n", roll, name, marks);

    }

}

 

public class StudentRecord {

    private ArrayList<Student> students = new ArrayList<>();

    private Scanner sc = new Scanner(System.in);

 

    public void addStudent() {

        System.out.print("Enter roll: ");

        int r = Integer.parseInt(sc.nextLine());

        System.out.print("Enter name: ");

        String n = sc.nextLine();

        System.out.print("Enter marks: ");

        double m = Double.parseDouble(sc.nextLine());

        students.add(new Student(r, n, m));

        System.out.println("Student added.");

    }

 

    public void displayAll() {

        if (students.isEmpty()) {

            System.out.println("No records.");

            return;

        }

        for (Student s : students) s.display();

    }

 

    public void searchByRoll() {

        System.out.print("Enter roll to search: ");

        int r = Integer.parseInt(sc.nextLine());

        for (Student s : students) {

            if (s.getRoll() == r) {

                s.display();

                return;

            }

        }

        System.out.println("Not found.");

    }

 

    public void menu() {

        while (true) {

            System.out.println("\n1.Add 2.Display All 3.Search by Roll 4.Exit");

            String ch = sc.nextLine();

            switch (ch) {

                case "1": addStudent(); break;

                case "2": displayAll(); break;

                case "3": searchByRoll(); break;

                case "4": System.out.println("Bye"); return;

                default: System.out.println("Invalid");

            }

        }

    }

 

    public static void main(String[] args) {

        new StudentRecord().menu();

    }

}
