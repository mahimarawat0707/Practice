class MethodOverloading {

    void para(){
        System.out.println("No parameters");
    }
    void para(int a) {
        System.out.println("a = " + a);
    }
    // Method with two int parameters
    void para(int a, int b) {
        System.out.println("a = " + a + " b = " +b);
    }

    // Method with two double parameters
    double para(double a) {
        return a;
    }

    public static void main(String[] args) {
        MethodOverloading obj = new MethodOverloading();
        obj.para();
        obj.para(12);
        obj.para(34, 56);
        System.out.println(obj.para(56.67893));
    }
}
