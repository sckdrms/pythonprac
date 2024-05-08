#include <stdio.h>

int main (void)
{
  // 경찰관이 범죄자의 정보를 입수함
  // 이름, 나이, 키, 범죄명이 무엇인가?

  // 자료형에 따라서 입력받고 출력받는 방식을 복기하자.


  char name[256];
  printf("name?");
  scanf("%s", name, sizeof(name));

  int age;
  printf("age?");
  scanf("%d", &age);

  float weight;
  printf("weight?");
  scanf("%f", &weight);

  int height;
  printf("height?");
  scanf("%d", &height);

  int bad[256];
  printf("name of bad?");
  scanf("%s", bad, sizeof(bad));

  printf("you are %s, %d, %.2f, %d, %s", name, age, weight, height, bad);

  return 0;
}