COLORS = {\
'black': '\u001b[30m',
'red': '\u001b[31m',
'green': '\u001b[32m',
'blue': '\u001b[34m',
'white': '\u001b[37m',
'white-background': '\u001b[47m',
'black-background' : '\u001b[40m',
'blue-background' : '\u001b[44;1m'
}

def colorText(text):
    for color in COLORS:
        text = text.replace('[[' + color + ']]', COLORS[color])
    return text
