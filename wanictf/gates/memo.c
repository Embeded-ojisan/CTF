undefined8 FUN_00101080(void)
{
  int iVar1;
  char *pcVar2;
  char *pcVar3;
  undefined1 *puVar4;
  undefined1 *puVar5;
  
  puVar4 = &DAT_0010404c;
  do {
    puVar5 = puVar4 + 0x10;
    iVar1 = getc(stdin);
    *puVar4 = 1;
    puVar4[1] = (char)iVar1;
    puVar4 = puVar5;
  } while (puVar5 != &DAT_0010424c);
  iVar1 = 0x100;
  do {
    FUN_00101220();
    iVar1 = iVar1 + -1;
  } while (iVar1 != 0);
  pcVar2 = &DAT_00104e4d;
  pcVar3 = &DAT_00104020;
  do {
    if (*pcVar2 != *pcVar3) {
      puts("Wrong!");
      return 1;
    }
    pcVar2 = pcVar2 + 0x10;
    pcVar3 = pcVar3 + 1;
  } while (pcVar2 != &DAT_0010504d);
  puts("Correct!");
  return 0;
}