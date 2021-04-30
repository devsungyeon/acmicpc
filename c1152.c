#include <stdio.h>
#include <string.h>
#define MAX 1000001

int main() {
	char str[MAX];
    scanf("%[^\n]", str);
    
    int count = 0;
    int i;
    int isSpace = 1;
    
    for (i = 0 ; str[i] ; i++) {
        if(str[i] == ' ') isSpace = 1;
        else if(isSpace) {
            isSpace = 0 ;
            count++;
        }
    }    
    
    printf("%d", count);
    
	return 0;
}
