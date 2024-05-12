#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (void)
{
  // if (조건) {} else {}
  int age = 25;
  if(age >= 20)
    printf("adult\n");
  else
    printf("kid\n");

  // else if
  int age1 = 15;
  if(age1 >= 8 && age1 <= 13)
  {
    printf("choding\n");
  }
  else if(age1 >= 14 && age1 <= 16)
  {
    printf("jungding\n");
  }
  else if(age1 >= 17 && age1 <= 19)
  {
    printf("goding\n");
  }
  else
  {
    printf("not student\n");
  }


  // break / continue
  // 1번부터 30번까지 있는 반에서 1번에서 5번까지 조별 발표를 합니다.
  for (int i = 1; i <= 30; i++)
  {
    if (i >= 6)
    {
      printf("go home\n");
      break;
    }
    printf("%d ready to ppt\n", i);
  }


  // 7번을 제외하고 6번부터 10번까지 조별 발표를 하세요.
  for (int i2 = 6; i2 <= 10; i2++)
  {
    if(i2 == 7)
    {
      printf("num %d is sick\n", i2);
      continue;
    }

    printf("%d ready to ppt\n", i2);
  }


  // and &&, or ||
  int a=10;
  int b=11;
  int c=12;
  int d=13;

  if (a == b && c==d)
  {
    printf("same\n");
  }
  else
  {
    printf("different\n");
  }


  // 가위0 바위1 보2
  srand(time(NULL));
  int q = rand() % 3;
  if(q == 0)
  {
    printf("gawe\n");
  }
  else if(q == 1)
  {
    printf("bawe\n");
  }
  else if(q == 2)
  {
    printf("bo\n");
  }


  // switch case
  srand(time(NULL));
  int w = rand() % 3;
  switch (w)
  {
    case 0: printf("gawe\n"); break;
    case 1: printf("bawe\n"); break;
    case 2: printf("bo\n"); break;
    default: printf("idk\n"); break;
  }

  return 0;
}
