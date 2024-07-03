#include <stdio.h>

void numf(int num1, int num2);

int main(void)
{
  numf(3, 5);
  return 0;
}

void numf(int num1, int num2)
{
  printf("num1 = %d, num2 = %d\n", num1, num2);
}