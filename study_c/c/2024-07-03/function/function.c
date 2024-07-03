#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>


// 커스텀 함수 순서
// 1. 선언
// 2. main()
// 3. 함수 정의 



void pri(int num);

int main(void)
{

	int num = 2;
	pri(num);

	num += 3;
	pri(num);

	num *= 4;
	pri(num);

	num /= 5;
	pri(num);

	return 0;

}

//반환형 함수이름(전달값){}
void pri(int num)
{
	printf("num is %d\n", num);
}

int plus(int num1, int num2)
{
	return num1 + num2;
}
