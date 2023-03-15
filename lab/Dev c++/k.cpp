#include <cstdlib>
#include <iostream>
using namespace std;
int main()
{ char n;
cout<< "Do you like me? (y/n)";
cin>> n;
if (n == 'y') { cout<< "I like you too."<<endl;}
if (n == 'n') { cout<< "I like you just the same."<<endl; }
system("PAUSE");
return EXIT_SUCCESS;}
