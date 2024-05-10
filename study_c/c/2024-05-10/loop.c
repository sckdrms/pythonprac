#include <stdio.h>

int main (void)
{
  // ++ 계산
  // ++i = 식 출력 전 계산, i++ = 식 출력 후 계산
  int i = 1;
  printf("hello world %d\n", i++);
  printf("hello world %d\n", ++i);
  printf("hello world %d\n", i);


  // 반복문 
  // for (선언; 조건; 증감){}
  for (int i = 0; i < 10; i++)
  {
    printf("hello world\n");
  }


  // 반복문 
  // while 선언 (조건) {증감}
  int i1 = 1;
  while (i1 <= 10)
  {
    printf("Hello World %d\n", i1++);
  }

  // 반복분 do while
  // 선언 do {증감} while (조건);
  int i2 = 1;
  do {
    printf("HELLO WORLD %d\n", i2++);
  } while (i2 <= 10);


  // 2중 반복문
  for (int i3 = 1; i3 <= 3; i3++)
  {
    printf("first for: %d\n", i3);
    for (int j = 1; j <= 5; j++)
    {
      printf("second for: %d\n", j);
    }

  }


  // 2중 반복문을 활용한 구구단
  for (int a = 1; a <= 9; a++)
  {
    printf("%dth dan\n", a);
    for (int b = 1; b <= 9; b++)
    {
    printf("%d x %d =%d\n" , a, b , a*b);
    }
  }

  // 별찍기
  for (int d = 1; d <= 5; d++)
  {
    for (int e = 1; e <= d; e++)
    {
      printf("*");
    }
    printf("\n");
  }

  // 반대로 별찍기
  for (int f = 1; f <= 5; f++)
  {
    for (int r = 5; r > f; r--)
    {
      printf(" ");
    }
    for (int g = 1; g <= f; g++)
    {
      printf("*");
    }
    printf("\n");
  }

  return 0;
}