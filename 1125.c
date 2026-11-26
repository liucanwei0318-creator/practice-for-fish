#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int fib_seq(int a )
{
	if (a == 1|| a == 2)
	{
		return 1;
	}
	return fib_seq(a - 1) + fib_seq(a - 2);
}
int main()
{
	int i = 0;
	scanf("%d", &i);
	printf("%d", fib_seq(i));
	return 0;
}