#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

void generateProblem(int* score, char op) {
    int num1, num2, answer, userAnswer;

    // 숫자 생성 및 연산 문제
    switch (op) {
        case '*':
            num1 = rand() % 900 + 100;
            num2 = rand() % 900 + 100;
            answer = num1 * num2;
            break;
        case '+':
            num1 = rand() % 900 + 100;
            num2 = rand() % 900 + 100;
            answer = num1 + num2;
            break;
        case '/':
            do {
                num1 = rand() % 900 + 100;
                num2 = rand() % 900 + 1;
            } while (num1 % num2 != 0);
            answer = num1 / num2;
            break;
        case '-':
            num1 = rand() % 900 + 100;
            num2 = rand() % 900 + 100;
            answer = num1 - num2;
            break;
    }

    // 문제 출력 및 사용자 입력
    printf("%d %c %d = ", num1, op, num2);
    scanf("%d", &userAnswer);

    // 정답 확인
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
        // 곱셈 오버플로우
        num1 = rand() % 900 + 100;
        num2 = UINT_MAX / num1 + 1;
        op = '*';
        answer = num1 * num2;
    } else {
        // 뺄셈 언더플로우
        num1 = rand() % 900 + 100;
        num2 = num1 + (UINT_MAX - num1) + 1;
        op = '-';
        answer = num1 - num2;
    }

    printf("%u %c %u = ", num1, op, num2);
    scanf("%d", &userAnswer);

    if (userAnswer == (int)answer) {
        printf("정답! (%s)\n", (op == '*') ? "Overflow" : "Underflow");
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
                    generateProblem(&score, '*');
                    break;
                case 1:
                    generateProblem(&score, '+');
                    break;
                case 2:
                    generateProblem(&score, '/');
                    break;
                case 3:
                    generateProblem(&score, '-');
                    break;
            }
        } else {
            generateOverflowUnderflow(&score);
        }
    }

    printGrade(score);

    return 0;
}
