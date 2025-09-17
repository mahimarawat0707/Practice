#include <iostream>

#include <string>

using namespace std;

class Person {

public:

    string name;

    int age;

};

class Faculty : public Person {

public:

    string department;

};

class Student : public Person {

public:

    string course;

};

class TeachingAssistant : public Faculty, public Student {};

int main() {

    TeachingAssistant ta;

    ta.name = "Alice"; // Ambiguity: which 'name' to use?

    return 0;

}
