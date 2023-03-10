def printc(txt):
    cols = {
        "%HEADER%": '\033[95m',
        "%WARNING%": '\033[93m',
        "%FAIL%": '\033[91m',
        "%ENDC%": '\033[0m',
        "%BOLD%": '\033[1m',
        "%UNDERLINE%": '\033[4m',
        "%RED%": '\033[91m',
        "%GREEN%": '\033[92m',
        "%BLUE%": '\033[94m',
        "%CYAN%": '\033[96m',
        "%WHITE%": '\033[97m',
        "%YELLOW%": '\033[93m',
        "%MAGENTA%": '\033[95m',
        "%ORANGE%": '\033[38;5;208m',
        "%GREY%": '\033[90m',
        "%BLACK%": '\033[90m',
        "%DEFAULT%": '\033[99m',
    }

    for col, repl in cols.items():
        txt = txt.replace(col, repl)
    print(txt)

