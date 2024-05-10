#include <stdio.h>

int main (void)
{
  // 피라미드 쌓기
  int floor;
  printf("how many floors?: ");
  scanf("%d", &floor);

  for (int a = 0; a < floor; a++)
  {
    for (int b = floor; b > a; b--)
    {
      printf(" ");
    }
    for (int c = 0; c < a * 2 + 1; c++)
    {
      printf("*");
    }
    printf("\n");
  }


  return 0;
}