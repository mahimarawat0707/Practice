#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Patient {
    int id;
    string name;
    int age;
    string disease;
};

class Hospital {
private:
    vector<Patient> patients;
    int nextId = 1;

public:
    void addPatient() {
        Patient p;
        p.id = nextId++;
        cout << "Enter patient name: ";
        cin >> p.name;
        cout << "Enter patient age: ";
        cin >> p.age;
        cout << "Enter patient disease: ";
        cin >> p.disease;

        patients.push_back(p);
        cout << "\n✅ Patient added successfully with ID: " << p.id << "\n";
    }

    void viewPatients() {
        if (patients.empty()) {
            cout << "\n⚠ No patients found!" << endl;
            return;
        }

        cout << "\n--- Patient List ---\n";
        for (auto &p : patients) {
            cout << "ID: " << p.id
                 << " | Name: " << p.name
                 << " | Age: " << p.age
                 << " | Disease: " << p.disease << endl;
        }
    }

    void searchPatient() {
        int searchId;
        cout << "Enter Patient ID to search: ";
        cin >> searchId;

        for (auto &p : patients) {
            if (p.id == searchId) {
                cout << "\n✅ Patient Found!" << endl;
                cout << "ID: " << p.id
                     << " | Name: " << p.name
                     << " | Age: " << p.age
                     << " | Disease: " << p.disease << endl;
                return;
            }
        }

        cout << "\n❌ Patient not found!" << endl;
    }

    void deletePatient() {
        int deleteId;
        cout << "Enter Patient ID to delete: ";
        cin >> deleteId;

        for (int i = 0; i < patients.size(); i++) {
            if (patients[i].id == deleteId) {
                patients.erase(patients.begin() + i);
                cout << "\n✅ Patient deleted successfully!" << endl;
                return;
            }
        }
        cout << "\n❌ Patient not found!" << endl;
    }
};

int main() {
    Hospital hm;
    int choice;

    do {
        cout << "\n===== HOSPITAL MANAGEMENT SYSTEM =====\n";
        cout << "1. Add Patient" << endl;
        cout << "2. View Patients" << endl;
        cout << "3. Search Patient" << endl;
        cout << "4. Delete Patient" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: hm.addPatient(); break;
            case 2: hm.viewPatients(); break;
            case 3: hm.searchPatient(); break;
            case 4: hm.deletePatient(); break;
            case 5: cout << "\n👋 Exiting program..." << endl; break;
            default: cout << "\n⚠ Invalid choice! Try again." << endl;
        }

    } while (choice != 5);

    return 0;
}
