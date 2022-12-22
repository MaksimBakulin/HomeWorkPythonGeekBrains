import datetime
def Logging_rational(a, b, c, d):
    time = str(datetime.datetime.now())
    log_file = open("Log.txt", "a", encoding="utf-8")
    log_file.write(time)
    if b == "+":
        if c >= 0:
            log_file.write(f" Произведено вычисление: {a}{b}{c}. Полученный результат = {d}")
            log_file.write("\n")
        elif c < 0:
            log_file.write(f" Произведено вычисление: {a}{c}. Полученный результат = {d}")
            log_file.write("\n")
    elif b == "-":
        if c >= 0:
            log_file.write(f" Произведено вычисление: {a}{b}{c}. Полученный результат = {d}")
            log_file.write("\n")
        elif c < 0:
            log_file.write(f" Произведено вычисление: {a}{b}({c}). Полученный результат = {d}")
            log_file.write("\n")
    else:
        log_file.write(f" Произведено вычисление: {a}{b}{c}. Полученный результат = {d}")
        log_file.write("\n")
    log_file.close()

def Logging_complex(a, b, c, d, e, f, h):
    time = str(datetime.datetime.now())
    log_file = open("Log.txt", "a", encoding="utf-8")
    log_file.write(time)
    if b >= 0 and d >= 0:
        log_file.write(f" Произведено вычисление: ({a}+{b}{e}){f}({c}+{d}{e}). Полученный результат = {h}")
        log_file.write("\n")
    elif b >= 0 and d < 0:
        log_file.write(f" Произведено вычисление: ({a}+{b}{e}){f}({c}{d}{e}). Полученный результат = {h}")
        log_file.write("\n")
    elif b < 0 and d >= 0:
        log_file.write(f" Произведено вычисление: ({a}{b}{e}){f}({c}+{d}{e}). Полученный результат = {h}")
        log_file.write("\n")
    elif b < 0 and d < 0:
        log_file.write(f" Произведено вычисление: ({a}{b}{e}){f}({c}{d}{e}). Полученный результат = {h}")
        log_file.write("\n")
    log_file.close()