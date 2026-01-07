#include <iostream>
using namespace std;
class Table {
    int n;
    
    public:
    void data(){
        cout << "Enter a number: ";
        cin >> n;
    }
    
    void ans(){
        for(int i = 1; i <= 10; i++){
            cout << n << " x " << i << " = " << n * i << endl;
        }
    }
};
int main()
{
    Table t;
    t.data();
    t.ans();

    return 0;
}

