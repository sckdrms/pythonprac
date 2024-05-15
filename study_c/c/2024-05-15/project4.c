// 5단계까지 있고 점점 어려운 문제 출제 (랜덤)
// 맞추면 통과, 틀리면 실패

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int getnum(int level);
void showquestion(int level, int num1, int num2);
void succes();
void fail();


int main(void)
{
  srand(time(NULL));
  int count = 0;
  for(int i = 1; i <= 5; i++)
  {
    int num1 = getnum(i);
    int num2 = getnum(i);
    // printf("%d ? %d\n", num1, num2);
    showquestion(i, num1, num2);

    int answer = -1;
    scanf("%d", &answer);
    if (answer == -1)
    {
      printf("exit\n");
      exit(0);
    }
    else if (answer == num1 * num2)
    {
      // 성공
      succes();
      count++;
    }
    else
    {
      // 실패
      fail();
      printf("You lose\n");
      exit(0);
    }
  }

  printf("You get %d score\n", count);

  return 0;
}

int getnum(int level)
{
  return rand() % (level * 7) + 1;
}

void showquestion(int level, int num1, int num2)
{
  printf("=======level: %d\n=======", level);
  printf("%d x %d = ?\n", num1, num2);
  printf("=========================\n");
  printf("enter answer: / (exit >> -1)\n");
}

void succes()
{
  printf("Good\n");
}

void fail()
{
  printf("Fail\n");
}