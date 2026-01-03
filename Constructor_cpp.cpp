#include <iostream>
using namespace std;

class student {
    int age;
    float marks;
public:
    student() {
        cout << "Enter age: ";
        cin >> age;
        cout << "Enter marks: ";
        cin >> marks;
    }
    void display() {
        cout << "Age = " << age << endl;
        cout << "Marks = " << marks << endl;
    }
};

int main() {
    student obj;
    obj.display();
    return 0;
}
