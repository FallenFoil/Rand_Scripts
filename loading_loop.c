#include <stdio.h>
#include <unistd.h>

int main(){
    int i = 0;
    while(1){
    if(i == 0){
        printf("\r-");
    }
    else{
        if(i == 1){
           printf("\r\\");
        }
        else{
        if(i == 2){
                printf("\r|");
        }
        else{
            if(i == 3){
                printf("\r/");
            i = -1;
            }
        }
        }
    }

    i++;
    fflush(stdout);
    sleep(1);
    }

    return 0;
}
