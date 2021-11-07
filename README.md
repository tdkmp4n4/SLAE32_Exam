# SecurityTube Linux Assembly Expert 32-bit (SLAE32)
This course focuses on teaching the basics of 32-bit assembly language for the Intel Architecture (IA-32) family of processors on the Linux platform and applying it to Infosec. Once we are through with the basics, we will look at writing shellcode, encoders, decoders, crypters and other advanced low level applications.

This repository contains all the resources developed by the student David Álvarez Robles in order to pass the exam and get SLAE32 certification. The following assignments are implemented:

## Assignment 1 - Shell Bind TCP
Detailed blog post: 
  - Create a Shell_Bind_TCP shellcode
      - Binds to a port
      - Executes shell on incoming connection
  - Port number should be easily configurable

## Assignment 2 - Shell Reverse TCP
Detailed blog post:
  - Create a Shell_Reverse_TCP shellcode
      - Reverse connects to configured IP and port 
      - Executes shell on successful connection
  - IP and port should be easily configurable

## Assignment 3 - EggHunter shellcode
Detailed blog post:  
   - Study about the EggHunter shellcode
   - Create a working demo off the EggHunter
   - Should be configurable for different payloads

## Assignment 4 - Custom encoding scheme
Detailed blog post: 
  - Create a custom encoding scheme like the "Insertion Encoder" shown in the course
  - PoC with using execve-stack as the shellcode to encode and execute with the schema

## Assignment 5 - Metasploit shellcode analysis
Detailed blog post: 
  - Take up at least 3 shellcode samples created using Msfpayload for linux/x86
  - Use GDB/Ndisasm/Libemu to dissect the functionality of the shellcode
  - Present your analysis

## Assignment 6 - Creating polymorphic shellcode
Detailed blog post: 
  - Take up 3 shellcodes from Shell‐Storm and create polymorphic versions of them to beat pattern matching
  - The polymorphic versions cannot be larger 150% of the existing shellcode
  - Bonus points for making it shorter in length than original

## Assignment 7 - Creating a custom crypter
Detailed blog post: 
  - Create a custom crypter like the one shown in the “crypters” video
  - Free to use any existing encryption schema
  - Can use any programming language
