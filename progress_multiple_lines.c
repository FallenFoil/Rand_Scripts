#include <stdio.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <string.h>

#define gotoxy(x,y) printf("\033[%d;%dH", (y), (x))

int main(){
    gotoxy(1, 2);
    fflush(stdout);
    printf("43%% Checking for updates\n 0%% Installing updates\n 0%% Cleaning up\n");
    gotoxy(1, 2);
    fflush(stdout);
        sleep(3);
    printf("99%% Checking for updates\n40%% Installing updates\n 0%% Cleaning up\n");

    fflush(stdout);
        sleep(3);

    printf("Done, be happy\nAnd enjoy your life\n");

    return 0;
}
