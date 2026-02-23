interface Studying {
    void study();
}

interface Playing {
    void play();
}

class Student implements Studying, Playing {
    public void study() {
        System.out.println("Student is studying.");
    }

    public void play() {
        System.out.println("Student is playing.");
    }
}

public class Main {
    public static void main(String[] args) {
        Student s = new Student();
        s.study();
        s.play();
    }
}
