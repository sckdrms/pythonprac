#include <stdio.h>
int main (void)
{
  // 정수형 변수에 대한 예제

  int age = 12;
  printf("%d\n", age);

  age = 13;
  printf("%d\n", age);


  /**/
  //asd
  
  // 실수형 변수에 대한 예제
  // %.nf 는 소수점 몇번째 자리까지 표시
  // float %f , double %lf
  float f = 46.5f;
  printf("%.2f\n",f);
  double d = 4.428;
  printf("%.1lf\n", d);


  // 상수형 변수에 대한 예제
  // const
  const int year = 2000;
  printf("born year: %d\n", year);
  // YEAR = 2001;


  // printf
  int add = 3 + 7; // 10
  printf("3 + 7 = %d\n", add);
  printf("%d + %d = %d\n", 3, 7, 3 + 7);


  // scanf
  // 키보드 입력을 받아서 저장
  // %s = 값을 입력받음, 출력도 함
  int input;
  printf("input ur num: ");
  scanf("%d", &input); // & = input이라고 정의된 곳에 값을 입력받겠다는 의미
  printf("ur input num is: %d\n", input);

  int one, two, three;
  printf("input 3 nums: ");
  scanf("%d %d %d", &one, &two, &three);
  printf("1st num: %d\n", one);
  printf("2nd num: %d\n", two);
  printf("3rd num: %d\n", three);


  // 뮨자(한 글자), 문자열(한 글자 이상의 여러 글자)
  // char %c
  char c = 'A';
  printf("%c\n", c);

  char str[256];
  scanf("%s", str, sizeof(str));
  printf("u inputted this text: %s\n", str);

    return 0;
}