#include <iostream>
using namespace std;

int main() {
    int num, reversed = 0, original, digit;
    cout << "Enter a number: ";
    cin >> num;
    original = num;

    while(num > 0) {
        digit = num % 10;
        reversed = reversed * 10 + digit;
        num /= 10;
    }

    if(original == reversed)
        cout << "It’s a palindrome";
    else
        cout << "Nope, not a palindrome";

    return 0;
}
