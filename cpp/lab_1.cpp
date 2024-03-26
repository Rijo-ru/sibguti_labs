#include <iostream>
using namespace std;
int main() 
{
    char a[]={"Hello World!"};
    char *c1,*c2, c1_c2;

    c1=&a[1];
    c2=&a[2];
    c1_c2=*c1+*c2;
    cout<<"c1="<<c1<<"\n *c1="<<*c1<<"\n";
    cout<<"c2="<<c2<<"\n *c2="<<*c2<<"\n";
    cout<<"c1_c2="<<c1_c2;
}