class Fish {
    void sound() {
        System.out.println("Fish makes a sound");
    }
}

class Goldfish extends Fish {
    void sound() {
        super.sound();
        System.out.println("Goldfish blubs");
    }
}

class Main {
    public static void main(String[] args) {
        Goldfish g = new Goldfish();
        g.sound();
    }
}
