"""170)	Заглавные буквы русского алфавита закодированы неравномерным двоичным кодом, в котором никакое
 кодовое слово не является началом другого кодового слова. Это условие обеспечивает возможность однозначной
  расшифровки закодированных сообщений. Известно, что все кодовые слова содержат не меньше двух двоичных знаков,
   а слову ГОЛОД соответствует код 0100001100111. Какой код соответствует слову ДОГ?"""


def phano():    # проверка выполнения условия Фано
    dl = list(d.values())
    for i in range(len(dl)):
        for j in range(len(dl)):
            if i != j and dl[i].startswith(dl[j]):
                return False
    return True


def build_dict(word, code):
    #   print(word, code, d)
    if not word:
        if not code:
            print('***', d)
            global dSave
            dSave = d.copy()
            return True
        else:
            return False
    if len(code) < 2:
        return False
    c = word[0]
    if c in d:
        code1 = d[c]
        m = len(code1)
        if code.startswith(code1):
            build_dict(word[1:], code[m:])
        return
    d[c] = code[:2]
    if phano():
        build_dict(word[1:], code[2:])
    del d[c]
    if len(code) < 3:
        return False
    d[c] = code[:3]
    if phano():
        build_dict(word[1:], code[3:])
    del d[c]
    if len(code) < 4:
        return False
    d[c] = code[:4]
    if phano():
        build_dict(word[1:], code[4:])
    del d[c]


def encode(s, d1):
    code1 = ""
    for c in s:
        code1 += d1[c]
    return code1


dSave = {}
d = {}

w1 = "ГОЛОД"
w2 = "ДОГ"
code = '0100001100111'
build_dict(w1, code)
print(encode(w2, dSave))

