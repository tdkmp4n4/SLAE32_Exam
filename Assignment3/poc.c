#include<stdlib.h>
#include<stdio.h>
#include<string.h>

unsigned char egghunter[] = "\x31\xd2\x66\x81\xca\xff\x0f\x42\x8d\x5a\x04\x6a\x21\x58\xcd\x80\x3c\xf2\x74\xee\xb8\x90\x50\x90\x50\x89\xd7\xaf\x75\xe9\xaf\x75\xe6\xff\xe7";

unsigned char code[] = "\x90\x50\x90\x50\x90\x50\x90\x50\xeb\x17\x31\xc0\xb0\x04\x31\xdb\xb3\x01\x59\x31\xd2\xb2\x0d\xcd\x80\x31\xc0\xb0\x01\x31\xdb\xcd\x80\xe8\xe4\xff\xff\xff\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0a";

main()
{
	char *buffer;
	buffer = malloc(strlen(code));
	memcpy(buffer, code, strlen(code));

	printf("EggHunter routine length: %d\n", strlen(egghunter));
	printf("Shellcode length: %d\n", strlen(code));

	int (*ret) () = (int(*)())egghunter;

	ret();

	free(buffer);
}

