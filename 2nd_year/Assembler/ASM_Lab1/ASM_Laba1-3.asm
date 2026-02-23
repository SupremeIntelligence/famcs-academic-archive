.586
.MODEL FLAT, C
.STACK
.DATA
.CODE
CALC PROC C a : dword, b : dword, x : dword

mov eax, x
imul eax, eax
imul eax, x
imul eax, -3
mov ebx, eax

mov edi, 3
mov eax, 5
imul eax, a
imul  eax, edi
add ebx, eax

mov eax, x
imul eax, eax
imul eax, x
add ebx, eax

sub ebx, 2

mov eax, 3
imul eax, x
imul eax, x
mov ecx, eax

mov edi, 5
mov eax, 7
imul b
cdq
idiv edi
idiv a

sub ecx, eax

add ecx, b

mov eax, ebx
cdq
idiv ecx
ret

CALC ENDP
END