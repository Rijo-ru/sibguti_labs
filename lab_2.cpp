#include <iostream>
using namespace std;
int main()
{setlocale (LC_ALL, "Rus");
    int *iptr = (int *)10; // ошибка приведения типа целого числа для указателя
    *iptr = 11;
    cout<<"По адресу iptr="<<iptr<<" хранится *iptr="<<*iptr<<"\n";
    return 0;
}