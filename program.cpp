#include <iostream>
using namespace std;

class Sum{
    int a, b;

public:
    void data(){
        cout << "Enter first number: ";
        cin >> a;
        cout << "Enter second number: ";
        cin >> b;
    }

    void sum(){
        cout << "Sum of "<< a << " and " <<b <<" = " << a + b <<endl;
    }
    void mul(){
        cout << "Multiplitaion of "<< a << " and " <<b <<" = " << a * b << endl;
    }
    void diff(){
        cout << "Difference of " << a << " and " <<b <<" = " << a - b << endl;
    }
    void div(){
        cout << "Division of " << a << " and " <<b <<" = " << a / b << endl;
    }
};

int main()
{
    Sum s;
    s.data();
    s.sum();
    s.mul();
    s.diff();
    s.div();
    

    return 0;
}
