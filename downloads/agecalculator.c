#include <stdio.h>

int main() {

    int running = 1;
    while (running == 1){

        int person1Age;
        int person2Age;
        int futurePerson1Age;

        printf("AGE CALCULATOR \n");
        printf("You'll fill in this prompt: \n\n\"Person 1 is _ years old. Person 2 is _ years old. When person 1 is _, I want to know how old person 2 will be.\" \n\n");

        printf("Insert person 1 current age: \n");
        scanf("%d", &person1Age);

        printf("Insert person 2 current age: \n");
        scanf("%d", &person2Age);

        printf("When person 1 is __, I want to know how old person 2 will be. \n");
        printf("Fill in the blank. \n");
        scanf("%d", &futurePerson1Age);

        int futurePerson2Age = person2Age + (futurePerson1Age - person1Age);

        printf("When person 1 is %d, person 2 will be %d. \n\n", futurePerson1Age, futurePerson2Age);

    }

    return 0;
}
