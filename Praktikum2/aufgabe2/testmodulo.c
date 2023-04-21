/* Test Modulo operation */
#include <stdbool.h>

main()
{
int a=10;
int b=5;
int c=a%5;
return c;
}

bool test(int a)
{
return (a%3123)==24;
}

int test2(int a)
{

a += a + a;
a = (a ** 31) >> 1;
a >>= 3;
a += 444;
a -= 222;
a = a%3123;
if(a == 24){
return 1;
}
else{
return 0;
}
}
