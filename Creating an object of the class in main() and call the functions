#include <iostream>

using namespace std;

class Employee {

    int eid;

    char ename[100];

    float basic_salary, hra, da, i_tax, net_salary;

public:

    void accept_details() {

        cout << "\nEnter Employee Id: ";

        cin >> eid;

        cout << "Enter Employee Name: ";

        cin >> ename;

        cout << "Enter Basic Salary: ";

        cin >> basic_salary;

        hra = 800;

        da = 0.25 * basic_salary;

        i_tax = 0.15 * basic_salary;

        net_salary = basic_salary + da + hra - i_tax;

    }

  void display_details() {

        cout << "\n-----------------------------";

        cout << "\nEmployee Id        : " << eid;

        cout << "\nEmployee Name      : " << ename;

        cout << "\nBasic Salary       : " << basic_salary;

        cout << "\nHRA                : " << hra;

        cout << "\nDA                 : " << da;

        cout << "\nIncome Tax         : " << i_tax;

        cout << "\nNet Salary         : " << net_salary;

        cout << "\n-----------------------------";

    }

};

 

int main() {

    Employee e;

    e.accept_details();

    e.display_details();

    return 0;

}
