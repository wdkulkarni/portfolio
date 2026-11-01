#For colors go to https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 or google ANSI escape codes and click on the github gist page.
def esc(code):
    return f'\033[{code}m'
print(esc('38;5;20') + 'formatted' + esc(0) + ' normal')