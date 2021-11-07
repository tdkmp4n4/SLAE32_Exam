; Filename: exec.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

xor ecx,ecx 		; Clear ECX register
mul ecx			; Clear EDX register, as well as EAX register
mov al,0xb		; Move 0xb value to AL register (execve call number 11 (first argument))
push dword 0x68732f	; Push "hs/" to the stack
push dword 0x6e69622f	; Push "nib/" to the stack
mov ebx,esp		; Move stack pointer to EBX register (second argument)
int 0x80		; Perform system call to execute /bin/sh
