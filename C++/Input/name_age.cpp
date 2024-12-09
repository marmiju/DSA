#include <iostream>
using namespace std;

int main()
{
    int age;
    string name;

    cout << "Enter your name: "; // will be show String as a input label
    cin >> name;                 // User will enter the name and it will be stored in name variable

    cout << "Enter your age: ";
    cin >> age; // User will enter the age and it will be stored in age variable

    cout << "hello" << name << "! You are" << age << "years Old" << endl;
}