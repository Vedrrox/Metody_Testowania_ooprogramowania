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
    int a= 0 ;
    for (int i = 0; i < strlen(format_string); i++){
         if (format_string[i] != '#')
         {
            putchar(format_string[i]);
            a = 0 ;
            continue;
         }
         if (format_string[i+1 == '.']){
            if (format_string[i+2] == 'k')
            {
               i++;
               swap_case(param);
               printf("%s",param);
               continue;
            }
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




         int second_i = i+2;
         char second_char = format_string[second_i];
         int length = 0;
         while (second_char >= '0' && second_char <= '9' && second_i <= strlen(format_string)){
            length = (length * 10) + second_char - '0';
            second_i++;
            second_char = format_string[second_i];
         }
         if(second_char != 'k'){
            putchar(format_string[i]);
            continue;
         }
         i= second_i;
         swap_case(param);
         for (int j = 0; j < length ; j++)
         {
            if( j >= strlen(param)){
                break;
            }
            putchar(param[j]);
            
         }
          
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
    
    
