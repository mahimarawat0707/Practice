#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class Library {
public:
    void issueBook() {
        string name, book;
        cout << "Enter your name: ";
        cin.ignore(); 
        getline(cin, name);

        cout << "Enter the name of the book to issue: ";
        getline(cin, book);

        ofstream fout("issued_books.txt", ios::app);
        if (fout) {
            fout << "User: " << name << ", Book: " << book << endl;
            fout.close();
            cout << "\nBook issued successfully!\n";
        } else {
            cout << "Error opening file!\n";
        }
    }

    void showIssuedBooks() {
        ifstream fin("issued_books.txt");
        if (!fin) {
            cout << "\nNo records found!\n";
            return;
        }

        string line;
        cout << "\n--- List of Issued Books ---\n";
        while (getline(fin, line)) {
            cout << line << endl;
        }
        fin.close();
    }
};

int main() {
    Library lib;
    int choice;
    do {
        cout << "\n--- Library Management System ---\n";
        cout << "1. Issue Book\n";
        cout << "2. Show Issued Books\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                lib.issueBook();
                break;
            case 2:
                lib.showIssuedBooks();
                break;
            case 3:
                cout << "Exiting program...\n";
                break;
            default:
                cout << "Invalid choice!\n";
        }
    } while (choice != 3);

    return 0;
}
