#include <stdio.h>

int main(){
	int seed;
	signed int i;
	signed int j;
	int rand_num = 0;

	srand(0x83Du);
	for (i=0; i <= 9; ++i)
		seed = rand();
	srand(seed);
	for ( j = 0; j <= 19; ++j){
		rand_num = rand();
		printf("%d",rand_num);
	}
}
