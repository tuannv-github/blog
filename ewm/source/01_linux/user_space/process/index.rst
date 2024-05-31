=======
Process
=======

.. toctree:: 
    
    ps
    status


Source:

.. code-block:: C

    #include <stdio.h>

    int main()
    {
        printf("Hello\n");
        return 0;
    }

.. code-block:: Makefile

    all:
        gcc -m32 -o hello hello.c

.. code-block:: 

    objdump -f hello

    hello:     file format elf32-i386
    architecture: i386, flags 0x00000150:
    HAS_SYMS, DYNAMIC, D_PAGED
    start address 0x00001090


.. code-block::

    objdump -d hello

    hello:     file format elf32-i386


    Disassembly of section .init:

    00001000 <_init>:
        1000:       f3 0f 1e fb             endbr32 
        1004:       53                      push   %ebx
        1005:       83 ec 08                sub    $0x8,%esp
        1008:       e8 e3 00 00 00          call   10f0 <__x86.get_pc_thunk.bx>
        100d:       81 c3 c7 2f 00 00       add    $0x2fc7,%ebx
        1013:       8b 83 20 00 00 00       mov    0x20(%ebx),%eax
        1019:       85 c0                   test   %eax,%eax
        101b:       74 02                   je     101f <_init+0x1f>
        101d:       ff d0                   call   *%eax
        101f:       83 c4 08                add    $0x8,%esp
        1022:       5b                      pop    %ebx
        1023:       c3                      ret    

    Disassembly of section .plt:

    00001030 <.plt>:
        1030:       ff b3 04 00 00 00       pushl  0x4(%ebx)
        1036:       ff a3 08 00 00 00       jmp    *0x8(%ebx)
        103c:       0f 1f 40 00             nopl   0x0(%eax)
        1040:       f3 0f 1e fb             endbr32 
        1044:       68 00 00 00 00          push   $0x0
        1049:       e9 e2 ff ff ff          jmp    1030 <.plt>
        104e:       66 90                   xchg   %ax,%ax
        1050:       f3 0f 1e fb             endbr32 
        1054:       68 08 00 00 00          push   $0x8
        1059:       e9 d2 ff ff ff          jmp    1030 <.plt>
        105e:       66 90                   xchg   %ax,%ax
        1060:       f3 0f 1e fb             endbr32 
        1064:       68 10 00 00 00          push   $0x10
        1069:       e9 c2 ff ff ff          jmp    1030 <.plt>
        106e:       66 90                   xchg   %ax,%ax

    Disassembly of section .plt.got:

    00001070 <__cxa_finalize@plt>:
        1070:       f3 0f 1e fb             endbr32 
        1074:       ff a3 1c 00 00 00       jmp    *0x1c(%ebx)
        107a:       66 0f 1f 44 00 00       nopw   0x0(%eax,%eax,1)

    Disassembly of section .plt.sec:

    00001080 <printf@plt>:
        1080:       f3 0f 1e fb             endbr32 
        1084:       ff a3 0c 00 00 00       jmp    *0xc(%ebx)
        108a:       66 0f 1f 44 00 00       nopw   0x0(%eax,%eax,1)

    00001090 <sleep@plt>:
        1090:       f3 0f 1e fb             endbr32 
        1094:       ff a3 10 00 00 00       jmp    *0x10(%ebx)
        109a:       66 0f 1f 44 00 00       nopw   0x0(%eax,%eax,1)

    000010a0 <__libc_start_main@plt>:
        10a0:       f3 0f 1e fb             endbr32 
        10a4:       ff a3 14 00 00 00       jmp    *0x14(%ebx)
        10aa:       66 0f 1f 44 00 00       nopw   0x0(%eax,%eax,1)

    Disassembly of section .text:

    000010b0 <_start>:
        10b0:       f3 0f 1e fb             endbr32 
        10b4:       31 ed                   xor    %ebp,%ebp
        10b6:       5e                      pop    %esi
        10b7:       89 e1                   mov    %esp,%ecx
        10b9:       83 e4 f0                and    $0xfffffff0,%esp
        10bc:       50                      push   %eax
        10bd:       54                      push   %esp
        10be:       52                      push   %edx
        10bf:       e8 22 00 00 00          call   10e6 <_start+0x36>
        10c4:       81 c3 10 2f 00 00       add    $0x2f10,%ebx
        10ca:       8d 83 dc d2 ff ff       lea    -0x2d24(%ebx),%eax
        10d0:       50                      push   %eax
        10d1:       8d 83 6c d2 ff ff       lea    -0x2d94(%ebx),%eax
        10d7:       50                      push   %eax
        10d8:       51                      push   %ecx
        10d9:       56                      push   %esi
        10da:       ff b3 24 00 00 00       pushl  0x24(%ebx)
        10e0:       e8 bb ff ff ff          call   10a0 <__libc_start_main@plt>
        10e5:       f4                      hlt    
        10e6:       8b 1c 24                mov    (%esp),%ebx
        10e9:       c3                      ret    
        10ea:       66 90                   xchg   %ax,%ax
        10ec:       66 90                   xchg   %ax,%ax
        10ee:       66 90                   xchg   %ax,%ax

    000010f0 <__x86.get_pc_thunk.bx>:
        10f0:       8b 1c 24                mov    (%esp),%ebx
        10f3:       c3                      ret    
        10f4:       66 90                   xchg   %ax,%ax
        10f6:       66 90                   xchg   %ax,%ax
        10f8:       66 90                   xchg   %ax,%ax
        10fa:       66 90                   xchg   %ax,%ax
        10fc:       66 90                   xchg   %ax,%ax
        10fe:       66 90                   xchg   %ax,%ax

    00001100 <deregister_tm_clones>:
        1100:       e8 e4 00 00 00          call   11e9 <__x86.get_pc_thunk.dx>
        1105:       81 c2 cf 2e 00 00       add    $0x2ecf,%edx
        110b:       8d 8a 34 00 00 00       lea    0x34(%edx),%ecx
        1111:       8d 82 34 00 00 00       lea    0x34(%edx),%eax
        1117:       39 c8                   cmp    %ecx,%eax
        1119:       74 1d                   je     1138 <deregister_tm_clones+0x38>
        111b:       8b 82 18 00 00 00       mov    0x18(%edx),%eax
        1121:       85 c0                   test   %eax,%eax
        1123:       74 13                   je     1138 <deregister_tm_clones+0x38>
        1125:       55                      push   %ebp
        1126:       89 e5                   mov    %esp,%ebp
        1128:       83 ec 14                sub    $0x14,%esp
        112b:       51                      push   %ecx
        112c:       ff d0                   call   *%eax
        112e:       83 c4 10                add    $0x10,%esp
        1131:       c9                      leave  
        1132:       c3                      ret    
        1133:       8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
        1137:       90                      nop
        1138:       c3                      ret    
        1139:       8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi

    00001140 <register_tm_clones>:
        1140:       e8 a4 00 00 00          call   11e9 <__x86.get_pc_thunk.dx>
        1145:       81 c2 8f 2e 00 00       add    $0x2e8f,%edx
        114b:       55                      push   %ebp
        114c:       89 e5                   mov    %esp,%ebp
        114e:       53                      push   %ebx
        114f:       8d 8a 34 00 00 00       lea    0x34(%edx),%ecx
        1155:       8d 82 34 00 00 00       lea    0x34(%edx),%eax
        115b:       83 ec 04                sub    $0x4,%esp
        115e:       29 c8                   sub    %ecx,%eax
        1160:       89 c3                   mov    %eax,%ebx
        1162:       c1 e8 1f                shr    $0x1f,%eax
        1165:       c1 fb 02                sar    $0x2,%ebx
        1168:       01 d8                   add    %ebx,%eax
        116a:       d1 f8                   sar    %eax
        116c:       74 14                   je     1182 <register_tm_clones+0x42>
        116e:       8b 92 28 00 00 00       mov    0x28(%edx),%edx
        1174:       85 d2                   test   %edx,%edx
        1176:       74 0a                   je     1182 <register_tm_clones+0x42>
        1178:       83 ec 08                sub    $0x8,%esp
        117b:       50                      push   %eax
        117c:       51                      push   %ecx
        117d:       ff d2                   call   *%edx
        117f:       83 c4 10                add    $0x10,%esp
        1182:       8b 5d fc                mov    -0x4(%ebp),%ebx
        1185:       c9                      leave  
        1186:       c3                      ret    
        1187:       8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
        118e:       66 90                   xchg   %ax,%ax

    00001190 <__do_global_dtors_aux>:
        1190:       f3 0f 1e fb             endbr32 
        1194:       55                      push   %ebp
        1195:       89 e5                   mov    %esp,%ebp
        1197:       53                      push   %ebx
        1198:       e8 53 ff ff ff          call   10f0 <__x86.get_pc_thunk.bx>
        119d:       81 c3 37 2e 00 00       add    $0x2e37,%ebx
        11a3:       83 ec 04                sub    $0x4,%esp
        11a6:       80 bb 34 00 00 00 00    cmpb   $0x0,0x34(%ebx)
        11ad:       75 27                   jne    11d6 <__do_global_dtors_aux+0x46>
        11af:       8b 83 1c 00 00 00       mov    0x1c(%ebx),%eax
        11b5:       85 c0                   test   %eax,%eax
        11b7:       74 11                   je     11ca <__do_global_dtors_aux+0x3a>
        11b9:       83 ec 0c                sub    $0xc,%esp
        11bc:       ff b3 30 00 00 00       pushl  0x30(%ebx)
        11c2:       e8 a9 fe ff ff          call   1070 <__cxa_finalize@plt>
        11c7:       83 c4 10                add    $0x10,%esp
        11ca:       e8 31 ff ff ff          call   1100 <deregister_tm_clones>
        11cf:       c6 83 34 00 00 00 01    movb   $0x1,0x34(%ebx)
        11d6:       8b 5d fc                mov    -0x4(%ebp),%ebx
        11d9:       c9                      leave  
        11da:       c3                      ret    
        11db:       8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi
        11df:       90                      nop

    000011e0 <frame_dummy>:
        11e0:       f3 0f 1e fb             endbr32 
        11e4:       e9 57 ff ff ff          jmp    1140 <register_tm_clones>

    000011e9 <__x86.get_pc_thunk.dx>:
        11e9:       8b 14 24                mov    (%esp),%edx
        11ec:       c3                      ret    

    000011ed <main>:
        11ed:       f3 0f 1e fb             endbr32 
        11f1:       8d 4c 24 04             lea    0x4(%esp),%ecx
        11f5:       83 e4 f0                and    $0xfffffff0,%esp
        11f8:       ff 71 fc                pushl  -0x4(%ecx)
        11fb:       55                      push   %ebp
        11fc:       89 e5                   mov    %esp,%ebp
        11fe:       53                      push   %ebx
        11ff:       51                      push   %ecx
        1200:       83 ec 10                sub    $0x10,%esp
        1203:       e8 e8 fe ff ff          call   10f0 <__x86.get_pc_thunk.bx>
        1208:       81 c3 cc 2d 00 00       add    $0x2dcc,%ebx
        120e:       c7 45 f4 00 00 00 00    movl   $0x0,-0xc(%ebp)
        1215:       8b 45 f4                mov    -0xc(%ebp),%eax
        1218:       8d 50 01                lea    0x1(%eax),%edx
        121b:       89 55 f4                mov    %edx,-0xc(%ebp)
        121e:       83 ec 08                sub    $0x8,%esp
        1221:       50                      push   %eax
        1222:       8d 83 34 e0 ff ff       lea    -0x1fcc(%ebx),%eax
        1228:       50                      push   %eax
        1229:       e8 52 fe ff ff          call   1080 <printf@plt>
        122e:       83 c4 10                add    $0x10,%esp
        1231:       83 ec 0c                sub    $0xc,%esp
        1234:       6a 01                   push   $0x1
        1236:       e8 55 fe ff ff          call   1090 <sleep@plt>
        123b:       83 c4 10                add    $0x10,%esp
        123e:       eb d5                   jmp    1215 <main+0x28>

    00001240 <__libc_csu_init>:
        1240:       f3 0f 1e fb             endbr32 
        1244:       55                      push   %ebp
        1245:       e8 6b 00 00 00          call   12b5 <__x86.get_pc_thunk.bp>
        124a:       81 c5 8a 2d 00 00       add    $0x2d8a,%ebp
        1250:       57                      push   %edi
        1251:       56                      push   %esi
        1252:       53                      push   %ebx
        1253:       83 ec 0c                sub    $0xc,%esp
        1256:       89 eb                   mov    %ebp,%ebx
        1258:       8b 7c 24 28             mov    0x28(%esp),%edi
        125c:       e8 9f fd ff ff          call   1000 <_init>
        1261:       8d 9d 04 ff ff ff       lea    -0xfc(%ebp),%ebx
        1267:       8d 85 00 ff ff ff       lea    -0x100(%ebp),%eax
        126d:       29 c3                   sub    %eax,%ebx
        126f:       c1 fb 02                sar    $0x2,%ebx
        1272:       74 29                   je     129d <__libc_csu_init+0x5d>
        1274:       31 f6                   xor    %esi,%esi
        1276:       8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
        127d:       8d 76 00                lea    0x0(%esi),%esi
        1280:       83 ec 04                sub    $0x4,%esp
        1283:       57                      push   %edi
        1284:       ff 74 24 2c             pushl  0x2c(%esp)
        1288:       ff 74 24 2c             pushl  0x2c(%esp)
        128c:       ff 94 b5 00 ff ff ff    call   *-0x100(%ebp,%esi,4)
        1293:       83 c6 01                add    $0x1,%esi
        1296:       83 c4 10                add    $0x10,%esp
        1299:       39 f3                   cmp    %esi,%ebx
        129b:       75 e3                   jne    1280 <__libc_csu_init+0x40>
        129d:       83 c4 0c                add    $0xc,%esp
        12a0:       5b                      pop    %ebx
        12a1:       5e                      pop    %esi
        12a2:       5f                      pop    %edi
        12a3:       5d                      pop    %ebp
        12a4:       c3                      ret    
        12a5:       8d b4 26 00 00 00 00    lea    0x0(%esi,%eiz,1),%esi
        12ac:       8d 74 26 00             lea    0x0(%esi,%eiz,1),%esi

    000012b0 <__libc_csu_fini>:
        12b0:       f3 0f 1e fb             endbr32 
        12b4:       c3                      ret    

    000012b5 <__x86.get_pc_thunk.bp>:
        12b5:       8b 2c 24                mov    (%esp),%ebp
        12b8:       c3                      ret    

    Disassembly of section .fini:

    000012bc <_fini>:
        12bc:       f3 0f 1e fb             endbr32 
        12c0:       53                      push   %ebx
        12c1:       83 ec 08                sub    $0x8,%esp
        12c4:       e8 27 fe ff ff          call   10f0 <__x86.get_pc_thunk.bx>
        12c9:       81 c3 0b 2d 00 00       add    $0x2d0b,%ebx
        12cf:       83 c4 08                add    $0x8,%esp
        12d2:       5b                      pop    %ebx
        12d3:       c3                      ret    

.. code-block:: 

    ✗ cat /proc/23250/maps    
    56584000-56585000 r--p 00000000 103:05 10490665                          /home/tuannv/ws/blog/ewm/source/01_linux/general/process/src/hello
    56585000-56586000 r-xp 00001000 103:05 10490665                          /home/tuannv/ws/blog/ewm/source/01_linux/general/process/src/hello
    56586000-56587000 r--p 00002000 103:05 10490665                          /home/tuannv/ws/blog/ewm/source/01_linux/general/process/src/hello
    56587000-56588000 r--p 00002000 103:05 10490665                          /home/tuannv/ws/blog/ewm/source/01_linux/general/process/src/hello
    56588000-56589000 rw-p 00003000 103:05 10490665                          /home/tuannv/ws/blog/ewm/source/01_linux/general/process/src/hello
    57f99000-57fbb000 rw-p 00000000 00:00 0                                  [heap]
    f7cbc000-f7cd5000 r--p 00000000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7cd5000-f7e30000 r-xp 00019000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7e30000-f7ea4000 r--p 00174000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7ea4000-f7ea5000 ---p 001e8000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7ea5000-f7ea7000 r--p 001e8000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7ea7000-f7ea8000 rw-p 001ea000 103:04 531884                            /usr/lib/i386-linux-gnu/libc-2.31.so
    f7ea8000-f7eab000 rw-p 00000000 00:00 0 
    f7ede000-f7ee0000 rw-p 00000000 00:00 0 
    f7ee0000-f7ee4000 r--p 00000000 00:00 0                                  [vvar]
    f7ee4000-f7ee6000 r-xp 00000000 00:00 0                                  [vdso]
    f7ee6000-f7ee7000 r--p 00000000 103:04 529708                            /usr/lib/i386-linux-gnu/ld-2.31.so
    f7ee7000-f7f05000 r-xp 00001000 103:04 529708                            /usr/lib/i386-linux-gnu/ld-2.31.so
    f7f05000-f7f10000 r--p 0001f000 103:04 529708                            /usr/lib/i386-linux-gnu/ld-2.31.so
    f7f11000-f7f12000 r--p 0002a000 103:04 529708                            /usr/lib/i386-linux-gnu/ld-2.31.so
    f7f12000-f7f13000 rw-p 0002b000 103:04 529708                            /usr/lib/i386-linux-gnu/ld-2.31.so
    ffcb0000-ffcd2000 rw-p 00000000 00:00 0                                  [stack]
    ➜  src git:(main) ✗ 
