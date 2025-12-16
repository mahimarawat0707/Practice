#include <iostream>

#include <string>

using namespace std;

class Person {

public:

    string name;

    int age;

};

class Faculty : virtual public Person {

public:

    string department;

};

class Student : virtual public Person {

public:

    string course;

};

class TeachingAssistant : public Faculty, public Student {};

int main() {

    TeachingAssistant ta;

    ta.name = "Alice";            // No ambiguity

    ta.age = 25;

    ta.department = "Computer Science";

    ta.course = "Data Structures";

 

    cout << "Name: " << ta.name << endl;

    cout << "Age: " << ta.age << endl;

    cout << "Department: " << ta.department << endl;

    cout << "Course: " << ta.course << endl;

 

    return 0;

}
