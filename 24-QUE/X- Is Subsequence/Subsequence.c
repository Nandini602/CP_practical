#include <stdio.h>
#include <stdbool.h>
#include <string.h>

bool isSubsequence(char* s, char* t) {
    int n = strlen(s);
    int m = strlen(t);
    int i = 0;
    int j = 0;
    
    while (i < n && j < m) {
        if (s[i] != t[j]) {
            j++;
        } else {
            i++;
            j++;
        }
        
        if (i == n) {
            return true;
        }
    }
    
    return false;
}

int main() {
    char s[100];
    char t[100];
    
    printf("Enter string s: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0'; // Remove newline character
    
    printf("Enter string t: ");
    fgets(t, sizeof(t), stdin);
    t[strcspn(t, "\n")] = '\0'; // Remove newline character
    
    bool result = isSubsequence(s, t);
    printf("%s\n", result ? "true" : "false");
    
    return 0;
}

