#include <stdio.h>
#include <string.h>
#include <ctype.h>

void swap_case(char *param){
    for (int i = 0; i <strlen(param) ; i++)
    {
        if (param[i] >= 'A'&& param[i] <= 'z'){
            param[i] = param[i] + 32 ;
        }
        else if (param[i] >= 'a' && param[i] <= 'z') {
			param[i] = param[i] - 32;
		}
    }

    
    
}

	int my_printf(char *format_string, char *param) {
    int j = 3;
    for (int i = 0; i < strlen(format_string); i++){
         if (format_string[i] != '#')
         {
            putchar(format_string[i]);
            continue;
         }

         if (format_string[i+1] == 'k')
         {
            i++;
            swap_case(param);
            printf("%s",param);
            continue;
         }

         if (i+2 >= strlen(format_string))
         {
            putchar(format_string[i]);
            continue;
         }
         if (format_string[i+2] == 'k')
         {
            i += 2;
            continue;
         }
         if (format_string[i+2] < '0' || format_string[i+2]>'9'){
            putchar(format_string[i]);
            continue;
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
    
    
