#include <stdio.h>

int add(int num1, int num2);
int min(int num1, int num2);
int mul(int num1, int num2);
int div(int num1, int num2);

int main(void)
{
  int num1 = 12;
  int num2 = 4;
  int ret = 0;

  ret = add(num1, num2);
  printf("ret = %d\n", ret);

  ret = min(num1, num2);
  printf("ret = %d\n", ret);

  ret = mul(num1, num2);
  printf("ret = %d\n", ret);

  ret = div(num1, num2);
  printf("ret = %d\n", ret);


  return 0;
}

int add(int num1, int num2)
{
  return num1 + num2;
}

int min(int num1, int num2)
{
  return num1 - num2;
}
int mul(int num1, int num2)
{
  return num1 * num2;
}

int div(int num1, int num2)
{
  return num1 / num2;
}