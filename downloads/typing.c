#include <stdio.h>
#include <string.h>
#include <time.h>

int main() {

    while(1) {
        char header[] = "Enter some text: ";
        int i = 0;
        for(i = 0; i < strlen(header); i++) {
            printf("%c", header[i]);
            usleep(30000);
        }

        char text[100];
        fgets(text, 100, stdin);

        int a = 0;
        for(a = 0; a < strlen(text); a++) {
            printf("%c", text[a]);
            usleep(30000);
        }
    }

    return 0;
}
