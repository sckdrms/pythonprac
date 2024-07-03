#include <stdio.h>

int apple(int apple, int eat);
// void yparam(int parameter);


int main(void)
{
  int ret = apple(5, 2);
  printf("ret = %d\n", ret);
  printf("%d - %d = %d\n", 10, 4, apple(10,4));
  
  return 0;
}

int apple(int apple, int eat)
{
  printf("yreturn\n");
  return apple - eat;
}