#include <iostream>
using namespace std;
// First base class
class Father {
public:
    void work() {
        cout << "Father goes to office" << endl;
    }
};
// Second base class
class Mother {
public:
    void cook() {
        cout << "Mother cooks food" << endl;
    }
};
// Derived class
class Child : public Father, public Mother {
public:
    void play() {
        cout << "Child plays games" << endl;
    }
};
int main() {
    Child c;
    c.work();   // From Father
    c.cook();   // From Mother
    c.play();   // Own function
    return 0;
}
