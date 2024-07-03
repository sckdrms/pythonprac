#include <stdio.h>

void noreturn();
int intreturn();

int main(void)
{
  noreturn();
  int ret = intreturn();
  printf("%d\n", ret);
  return 0;
}

void noreturn()
{
  printf("no return function\n");
}

int intreturn()
{
  printf("int return function\n");
  return 10;
}