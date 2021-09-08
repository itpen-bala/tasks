#include <stdio.h>

char * input_text() {
    const int SIZE = 50;    
    char word[SIZE];
    char *p = word;

    puts("Enter the word: ");
    gets(word);

    return p;
}

int main(void) {

    char *word = input_text();

    int word_len = sizeof(word) / sizeof(word[0]);    
    for(int i = 0; i < word_len; i++) {
        if(word[i] == '\0') {
            break;
        }
        printf("%c", word[i]);
    }
    return 0;
}
   
