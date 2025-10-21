#include <iostream>
using namespace std;

class Person {
public:
    string *name;
    int *age;
    long long *phone_no;

    void allocation(string n, int a, long long p) {
        name = new string(n);
        age = new int(a);
        phone_no = new long long(p);
    }

    void show() {
        cout << "Name: " << *name << endl;
        cout << "Age: " << *age << endl;
        cout << "Phone Number: " << *phone_no << endl;
    }

    void deallocate() {
        delete name;
        delete age;
        delete phone_no;
    }
};

int main() {
    Person obj;
    obj.allocation("Mahima", 18, 9876543210);
    obj.show();
    obj.deallocate();
    return 0;
}
