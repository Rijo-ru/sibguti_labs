#include <iostream>

using namespace std;

int main()
{
    int *p = (int *) 0xb1000000;
    int *r = (int *)(p + 10);
    
    std::cout << r << '\n';
    std::cout << sizeof(r) << '\n';

    return 0;
}