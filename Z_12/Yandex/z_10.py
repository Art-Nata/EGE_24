"""ПОКА нашлось(10) ИЛИ нашлось(20)
   ЕСЛИ нашлось(20)
      ТО заменить(20,00)
      ИНАЧЕ заменить(10,200)
   КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
Определите максимально возможное количество цифр 0, которое может получиться в результате применения представленного
выше алгоритма к строке, состоящей из 19 цифр 0, 13 цифр 1 и 17 цифр 2, идущих в произвольном порядке."""


s = '1' * 13 + '2' * 17 + '0' * 19
while '10' in s or '20' in s:
    if '20' in s:
        s = s.replace('20', '00', 1)
    else:
        s = s.replace('10', '200', 1)
print(s)
print(s.count('0'))