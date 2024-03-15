#include <stdio.h>
 
int main() {
 
    double tempo, velocidade;
    scanf("%lf", &tempo);
    scanf("%lf", &velocidade);
    //double dist = (velocidade*tempo)/12;
    
    printf("%.3lf\n", (velocidade*tempo)/12);
    return 0;
}