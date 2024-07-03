#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

void generateMultiplication(int* score) { // 곱하기
    int num1 = rand() % 900 + 100;
    int num2 = rand() % 900 + 100;
    int answer = num1 * num2;
    int userAnswer;

    printf("%d * %d = ", num1, num2);
    scanf("%d", &userAnswer);

    if (userAnswer == answer) {
        printf("정답!\n");
        (*score)++;
    } else {
        printf("땡 ㅋㅋ 정답은 %d.\n", answer);
    }
}

void generateAddition(int* score) { // 더하기
    int num1 = rand() % 900 + 100;
    int num2 = rand() % 900 + 100;
    int answer = num1 + num2;
    int userAnswer;

    printf("%d + %d = ", num1, num2);
    scanf("%d", &userAnswer);

    if (userAnswer == answer) {
        printf("정답!\n");
        (*score)++;
    } else {
        printf("땡 ㅋㅋ 정답은 %d.\n", answer);
    }
}

void generateDivision(int* score) { // 나누기
    int num1, num2, answer, userAnswer;

    // divide by zero 조건
    do {
        num1 = rand() % 900 + 100;
        num2 = rand() % 900 + 1;   // 1~999 사이의 숫자 (0 제외)
    } while (num1 % num2 != 0);

    answer = num1 / num2;

    printf("%d / %d = ", num1, num2);
    scanf("%d", &userAnswer);

    if (userAnswer == answer) {
        printf("정답!\n");
        (*score)++;
    } else {
        printf("땡 ㅋㅋ 정답은 %d.\n", answer);
    }
}

void generateSubtraction(int* score) { // 빼기
    int num1 = rand() % 900 + 100;
    int num2 = rand() % 900 + 100;
    int answer = num1 - num2;
    int userAnswer;

    printf("%d - %d = ", num1, num2);
    scanf("%d", &userAnswer);

    if (userAnswer == answer) {
        printf("정답!\n");
        (*score)++;
    } else {
        printf("땡 ㅋㅋ 정답은 %d.\n", answer);
    }
}

void generateOverflowUnderflow(int* score) {
    unsigned int num1, num2, answer;
    int userAnswer;
    char op;

    if (rand() % 2 == 0) {
        // Multiplication overflow
        num1 = rand() % 900 + 100;
        num2 = UINT_MAX / num1 + 1; // 오버플로우를 일으키는 숫자
        op = '*';
        answer = num1 * num2;
    } else {
        // Subtraction underflow
        num1 = rand() % 900 + 100;
        num2 = num1 + (UINT_MAX - num1) + 1; // 언더플로우를 일으키는 숫자
        op = '-';
        answer = num1 - num2;
    }

    printf("%u %c %u = ", num1, op, num2);
    scanf("%d", &userAnswer);

    if (op == '-' && userAnswer == (int)answer) {
        printf("정답! (Underflow)\n");
        *score += 5;
    } else if (op == '*' && userAnswer == (int)answer) {
        printf("정답! (Overflow)\n");
        *score += 5;
    } else {
        printf("땡 ㅋㅋ 정답은 %u.\n", answer);
    }
}

void printGrade(int score) {
    int grade;
    if (score >= 25) {
        grade = 1;
    } else if (score >= 20) {
        grade = 2;
    } else if (score >= 15) {
        grade = 3;
    } else if (score >= 10) {
        grade = 4;
    } else {
        grade = 5;
    }

    printf("점수는 %d점. 등급은 %d입니다.\n", score, grade);
}

int main() {
    int level, score = 0;
    srand(time(NULL));

    printf("레벨을 선택하세요 (1-5): ");
    scanf("%d", &level);

    if (level < 1 || level > 5) {
        printf("레벨을 잘못 입력했습니다 .\n");
        return 1;
    }

    for (int i = 0; i < 5; i++) {
        if (level < 5) {
            int operation = rand() % 4;
            switch (operation) {
                case 0:
                    generateMultiplication(&score);
                    break;
                case 1:
                    generateAddition(&score);
                    break;
                case 2:
                    generateDivision(&score);
                    break;
                case 3:
                    generateSubtraction(&score);
                    break;
            }
        } else {
            generateOverflowUnderflow(&score);
        }
    }

    printGrade(score);

    return 0;
}
