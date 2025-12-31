#include <iostream>
#include <string>
using namespace std;

class student{
  string name;
  int marks;

public:
  student(string n, int n){
  name = n;
  marks = m;
  }

  student(const student &s){
    cout << "Copy constructor called" << endl;
    name = s.name;
    marks = s.name;
  }

  void showDetails() {
    cout << "Name: <<", Marks: " <<marks << endl;
  }
};

int main() {
  stusent s1("Mahima", 100);
  student s2 = s1;

  cout << "Details of s1: ";
  s1.showDetails();

  cout << "Details of s1: ";
  s2.showDetails();

  return 0;
}
