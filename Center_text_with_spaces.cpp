#include <iostream>
using namespace std;

int main() {
    int consoleWidth = 80; // assume console width is 80 characters
    string text = "Hello Boss!";

    // Calculate left padding
    int padding = (consoleWidth - text.length()) / 2;

    // Print spaces, then the text
    cout << string(padding, ' ') << text << endl;

    return 0;
}
