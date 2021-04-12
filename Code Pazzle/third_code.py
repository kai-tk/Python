morse={
        "iI":"A",
        "Iiii":"B",
        "IiIi":"C",
        "Iii":"D",
        "i":"E",
        "iiIi":"F",
        "IIi":"G",
        "iiii":"H",
        "ii":"I",
        "iIII":"J",
        "IiI":"K",
        "iIii":"L",
        "II":"M",
        "Ii":"N",
        "III":"O",
        "iIIi":"P",
        "IIiI":"Q",
        "iIi":"R",
        "iii":"S",
        "I":"T",
        "iiI":"U",
        "iiiI":"V",
        "iII":"W",
        "IiiI":"X",
        "IiII":"Y",
        "IIii":"Z",
        "iIIII":"1",
        "iiIII":"2",
        "iiiII":"3",
        "iiiiI":"4",
        "iiiii":"5",
        "Iiiii":"6",
        "IIiii":"7",
        "IIIii":"8",
        "IIIIi":"9",
        "IIIII":"0",
        "iIiiIi":"\"",
        "iIIIIi":"\'",
        "iIiIiI":".",
        "IIiiII":",",
        "IIIiii":":",
        "iiIIii":"?",
        "iiIIiI":"_",
        "iIiIi":"+",
        "IiiiiI":"-",
        "iiiiii":"^",
        "IiiIi":"/",
        "iIIiIi":"@",
        "IiIIi":"(",
        "IiIIiI":")"
    }

def decode_morse(code):
    s=""
    text=""
    for i in range(len(code)):
        if code[i]==" ":
            if s!="":
                text+=morse[s]
            s=""
        else:
            s+=code[i]
    return text

def encode_morse(text):
    code=""
    for i in range(len(text)):
        code = [k for k, v in morse.items() if v == text[i]][0]
    return code
