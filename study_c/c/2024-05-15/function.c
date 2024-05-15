
#include <stdio.h>

  // 선언 > 선언은 main 위에서 함
void p(int num);
void function_without_return();
int function_with_return();
void function_without_params();
void function_with_params(int parrams1, int parrams2, int parrams3);
int apple(int total, int ate);
int add(int a, int plus);
int sub(int a, int plus);
int mul(int a, int plus);
int div(int a, int plus);

int main (void)
{
  // function
  // 계산기
  int num = 2;
  // printf("num is %d\n", num);
  p(num);

  // 2 + 3 = ?
  num = num + 3; // num += 3;
  printf("num is %d\n", num);

  // 5 - 1 = ?
  num -= 1; // num = num -1;
  printf("num is %d\n", num);

  // 4 * 3 = ?
  num *= 3;
  printf("num is %d\n", num);

  // 12 / 6 = ?
  num /= 6;
  printf("num is %d\n", num);


  function_without_return();
  int ret = function_with_return();
  p(ret);

  function_without_params();
  function_with_params(1, 2, 3);

  int ret1 = apple(5, 2);
  // p(ret1);
  printf("%d - %d = %d\n", 10, 4, apple(10,4));



  int a = 2;
  a = add(a, 3);
  p(a);

  a = sub(a, 1);
  p(a);
  
  a = mul(a, 3);
  p(a);

  a = div(a, 6);
  p(a);



  return 0;
}


// 함수의 형태
// 반환영 함수이름(전달값)
// 반환형 ex) void int float char
void p(int num)
{
  printf("num is %d\n", num);
}



// 함수 종류
// 반환값이 없는 함수 void
void function_without_return()
{
  printf("void function\n");
}

// 반환값이 있는 함수 return
int function_with_return()
{
  printf("return function\n");
  return 10;
}

// 전달값(파라미터)가 없는 함수
void function_without_params()
{
  printf("non_params void function\n");
}

// 잔달값(파라미터)가 있는 함수
void function_with_params(int parrams1, int parrams2, int parrams3)
{
  printf("%d, %d, %d\n", parrams1, parrams2, parrams3);
}

// 전달값도 받고 반환값이 있는 함수
int apple(int total, int ate)
{
  printf("total: %d, ate: %d\n", total, ate);
  return total - ate;
}




// 계산기 함수
int add(int a, int plus)
{
  return a + plus;
}

int sub(int a, int plus)
{
  return a - plus;
}

int mul(int a, int plus)
{
  return a * plus;
}

int div(int a, int plus)
{
  return a / plus;
}
