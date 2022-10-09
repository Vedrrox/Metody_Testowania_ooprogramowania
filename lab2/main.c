#include <stdio.h>
#include <string.h>
#include <ctype.h>

	int my_printf(char *format_string, char *param) {
    
    for (int i = 0; i < strlen(format_string); i++){
          if (isalpha(format_string[i])) {
            if (islower(format_string[i]))
                format_string[i] = (char) toupper(format_string[i]);
            else
                format_string[i] = (char) tolower(format_string[i]);
        }
    }
    
        

    for (int i = 0; i < strlen(format_string); i++) {

            if ((format_string[i] == '#') && (format_string[i + 1] == 'k')) {
                i++;
                printf("%s", param);
            } else
                putchar(format_string[i]);
        }
        
        puts("");
        return 0;
		
    }

    int main(int argc, char *argv[]) {
        char buf[1024], buf2[1024];
        while (gets(buf)) {
            gets(buf2);
            my_printf(buf, buf2);
        }
        return 0;
	}
    
