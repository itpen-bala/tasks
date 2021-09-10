#include <stdio.h>
#include <string.h>

char *input_text()
{
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

int str_len(char *str)
{
    int len = 0;
    while(str[len] != '\0')
        len++;
    return len;
}

int is_palindrome(char *word)
{
    int len = str_len(word);

    int left = 0, right = len - 1;
    while(word[left++] == word[right--])
    {
        if(left == len / 2)
            return 1;
    }
    return 0;
}

int main(void)
{

    char *word = input_text();
    int answer = is_palindrome(word);
    printf("Word %s is palindrome: %d\n", word, answer); 
    return 0;
}
   
