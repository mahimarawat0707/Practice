#include <iostream>
using namespace std;

class MyInt {
public:
    int value;

    void setValue(int v) {
        value = v;
    }

    void setZero() {
        value = 0;
    }

    void display() {
        cout << value << endl;
    }

    MyInt operator + (MyInt obj2) {
        MyInt obj3;
        obj3.value = value + obj2.value;
        return obj3;
    }
};

int main() {
    MyInt obj1, obj2, obj3;

    obj1.setValue(2);
    obj2.setValue(3);
    obj3.setZero();

    obj3 = obj1 + obj2;

    obj3.display();

    return 0;
}
