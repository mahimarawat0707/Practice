#include <iostream>
#include <map>
using namespace std;

int main() {
    map<string, string> phoneBook;
    int n;
    string name, number;

    cout << "How many contacts you want to add? ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "\nEnter name: ";
        cin >> name;
        cout << "Enter phone number: ";
        cin >> number;
        phoneBook[name] = number;
    }

    cout << "\n--- Telephone Directory ---\n";
    for (auto p : phoneBook) {
        cout << p.first << " : " << p.second << endl;
    }

    string searchName;
    cout << "\nEnter name to search: ";
    cin >> searchName;

    if (phoneBook.find(searchName) != phoneBook.end())
        cout << "Phone number of " << searchName << " is " << phoneBook[searchName] << endl;
    else
        cout << "Name not found!" << endl;

    return 0;
}
