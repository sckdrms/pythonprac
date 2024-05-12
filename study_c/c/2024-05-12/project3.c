#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// up and down

int main (void)
{
  srand(time(NULL));
  int num = rand() % 100 + 1; // 1 ~ 100 사이의 숫자
  printf("%d\n", num);
  int answer = 0;
  int chance = 5;

  while (chance > 0)
  {
    printf("chance %d\n", chance--);
    printf("guess num (1~100):\n");
    scanf("%d",&answer);

    if (answer > num)
    {
      printf("down\n");
    }
    else if (answer < num)
    {
      printf("up\n");
    }
    else if (answer = num)
    {
      printf("correct!\n");
      break;
    }
    else
    {
      printf("error\n");
    }

    if (chance == 0)
    {
      printf("you lose\n");
    }
    
  }

  return 0;
}