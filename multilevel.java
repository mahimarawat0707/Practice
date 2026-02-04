class A {
    void parent() {
        System.out.println("This is parent class");
    }
}

class B extends A {
    void child() {
        System.out.println("This is child class");
    }
}

class C extends B {
    void child() {
        System.out.println("This is subclass class");
    }
}

public class Main {
    public static void main(String[] args) {
        B b = new B();
        b.parent();
        b.child();
       
        C c = new C();
        c.parent();
        c.child();
    }
}
