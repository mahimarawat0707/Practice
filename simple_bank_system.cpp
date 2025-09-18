#include<iostream.h>

#include<iomanip.h>

class bank

{

char name[40];

int ac_no;

char ac_type[20];

double balance;

public:

int assign(void);

void deposite(float b);

void withdraw(float c);

void display(void);

};

int bank::assign(void)

{

float initial;

cout<<" You have to pay 500 TK to open your account \n"

<<" You have to store at least 500 TK to keep your account active\n"

<<"Would you want to open a account????\n"

<<" If Yes press 1 \n"

<<" If No press 0 : ";

int test;

cin>>test;

if(test==1)

{

initial=500;

balance=initial;

cout<<" Enter name ,account number & account type to creat account : \n";

cin>>name>>ac_no>>ac_type;

}

else

;// do nothing

return test;

}

void bank::deposite(float b)

{

balance+=b;

}

void bank::withdraw(float c)

{

balance-=c;

if(balance<500)

{

cout<<" Sorry your balance is not sufficient to withdraw "<<c<<"TK\n"

<<" You have to store at least 500 TK to keep your account active\n";

balance+=c;

}

}

void bank::display(void)

{

cout<<setw(12)<<"Name"<<setw(20)<<"Account type"<<setw(12)<<"Balance"<<endl;

cout<<setw(12)<<name<<setw(17)<<ac_type<<setw(14)<<balance<<endl;

}

int main()

{

bank account;

int t;

t=account.assign();

if(t==1)

{

cout<<" Would you want to deposite: ?"<<endl

<<"If NO press 0(zero)"<<endl

<<"If YES enter deposite ammount :"<<endl;

float dp;

cin>>dp;

account.deposite(dp);

cout<<" Would you want to withdraw : ?"<<endl

<<"If NO press 0(zero)"<<endl

<<"If YES enter withdrawal ammount :"<<endl;

float wd;

cin>>wd;

account.withdraw(wd);

cout<<" see details :"<<endl<<endl;

account.display();

}

else if(t==0)

cout<<" Thank you ,see again\n";

return 0;

}
