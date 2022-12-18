#include <stdio.h>
#include <string.h>


void change_to_hex(char *str1)  {
	int i, len, temp;
    len = strlen(str1);
    for (i = 0; i < len; i++) {
        


    }
}

int my_printf(char *format_string, char *param){
	for(int i=0;i<strlen(format_string);i++){
		if((format_string[i] == '#') && (format_string[i+1] == 'j')){
			i++;

			int paramIsNumber = 1;
            for (int j = 0; j < strlen(param); j++) {
				if (!isdigit(param[j])) {
					paramIsNumber = 0;
					break;
				}
            }

			if (paramIsNumber) {
				change_to_hex(param);
			} else {
				puts("");
				return 0;
			}
			



			printf("%s",param);
		}else
			putchar(format_string[i]);
	}
	puts("");
	return 0;
}

int main(int argc, char *argv[]){
	char buf[1024],buf2[1024];
	while(gets(buf)){
		gets(buf2);
		my_printf(buf,buf2);
	}
	return 0;
}