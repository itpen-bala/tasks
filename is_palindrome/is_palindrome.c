#include <stdio.h>
#include <string.h>

char * input_text() {
    const int SIZE = 50;    
    char raw_word[SIZE];

    printf("Enter the word: \n");
    scanf("%s", raw_word);

    int len = 0;
    while(raw_word[len] != '\0')
        len++;
    len++;
    char word[len];
    memcpy(word, raw_word, len);
    char *p = word;
    return p;
}

int main(void) {

    char *word = input_text();
    printf("Got text\n");
    int len = 0;
    while(word[len] != '\0')
        len++;
    printf("%d", len);

    int left = 0;
    int middle = len / 2;
    int right = len - 1;
    while(word[left++] == word[right--]) {
        if(left = middle - 1 ) {
            ;
        }
    }
    

    return 0;
}
   
