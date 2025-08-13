#include <iostream>
#include <string>
using namespace std;

class Employee {
private:
    int E_ID;
    string name;
    float basicSalary;
    float hra, ta, da;
    int leaveTaken;
    float commission;
    float netSalary;

public:
    void input_details() {
        cout << "Enter Employee ID: ";
        cin >> E_ID;

        cout << "Enter name: ";
        cin.ignore(); // to avoid newline issues
        getline(cin, name);

        cout << "Enter basic salary: ";
        cin >> basicSalary;

        cout << "Enter the number of leaves taken: ";
        cin >> leaveTaken;

        cout << "Enter commission: ";
        cin >> commission;

        hra = 800;
        da = 0.25f * basicSalary;
        ta = 0.10f * basicSalary;

        float grossSalary = basicSalary + hra + da + ta + commission;

        int allowedLeave = 2;
        float leaveDeduction = 0;

        if (leaveTaken > allowedLeave) {
            leaveDeduction = (leaveTaken - allowedLeave) * 500;
        }

        netSalary = grossSalary - leaveDeduction;
    }

    void display_details() {
        cout << "\n______________Salary Slip_____________";
        cout << "\n Employee ID : " << E_ID;
        cout << "\n Employee name : " << name;
        cout << "\n Basic Salary : " << basicSalary;
        cout << "\n HRA : " << hra;
        cout << "\n DA : " << da;
        cout << "\n TA : " << ta;
        cout << "\n Commission : " << commission;
        cout << "\n Leave taken : " << leaveTaken;
        cout << "\n Net Salary : " << netSalary;
        cout << "\n_______________________________________\n";
    }
};

int main() {
    Employee e;
    e.input_details();
    e.display_details();
    return 0;
}
