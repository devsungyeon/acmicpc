#include <stdio.h>

int main() {
	int score;
	scanf("%d", &score);
	int grade;
	grade = (int)(score/10);
	char gradec;
	switch (grade)
	{
	case 10:
		gradec = 'A';
		break;
	case 9:
		gradec = 'A';
		break;
	case 8:
		gradec = 'B';
		break;
	case 7:
		gradec = 'C';
		break;
	case 6:
		gradec = 'D';
		break;
	default:
		gradec = 'F';
		break;
	}
	printf("%c", gradec);
	return 0;
}
