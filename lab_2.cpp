#include <iostream>
using namespace std;
int main()
{
    int *iptr = (int *)10; // ошибка приведения целого числа для указателя
    *iptr = 11;
    cout<<"По адресу iptr="<<iptr<<" хранится *iptr="<<*iptr<<"\n";
    return 0;
}