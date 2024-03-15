#include <stdio.h>

void decomp(int n){
    int div = 2;
    printf("Num\tDiv\n");
    while (n>1){
        if(n%div == 0){
            printf("%d\t%d\n", n, div);
            n = n/div;
        } 
        else div++;
    }

}

int main(){
    int n;
    scanf("%d", &n);
    decomp(n);
    return 0;
}