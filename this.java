class Student {
    int uid;

    Student(int uid) {
        this.uid = uid;
    }

    void display() {
        System.out.println("UID: " + uid);
    }
}

class Main {
    public static void main(String[] args) {
        Student s1 = new Student(111);
        s1.display();
    }
}
