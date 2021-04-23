//[C언어/C++] strcpy example. :BlockDMask:
#include<stdio.h>    //C++ <iostream> or <cstdio>
#include<string.h>    //C++ <cstring>
 
typedef struct book
{
char nam[10];
int isbn;
int price;
int year;
struct book* pb;
}BOOK;

// BOOK 구조체 30개를 저장할 수 있는 메모리공간을 할당한 후 BOOK 구조체 포인터로 변환하여 p에 저장

int main(void)
{
    BOOK* p = (BOOK*) malloc ( sizeof(BOOK) * 30);
    printf("%d\n", sizeof(BOOK));
    char a;
    printf("%d\n", sizeof(a));
    int b;
    printf("%d\n", sizeof(b));
    struct book* q;
    printf("%d\n", sizeof(q));
}

