#include <stdio.h>

int main() {
	FILE* fh = fopen("/pwn/flag.txt","r");
	char buf[128];
	fgets(buf,128,(FILE*)fh);
	fclose(fh);
}