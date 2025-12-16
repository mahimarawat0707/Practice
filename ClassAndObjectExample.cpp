#include <iostream>
using namespace std;

class Queen {
public:
    void welcome() {
        cout << "Welcome";
    }
};

int main() {
    Queen you;
    you.welcome();
    return 0;
}
