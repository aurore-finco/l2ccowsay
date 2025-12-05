import sys
sys.path.insert(0, r"C:\Users\yassi\l2ccowsay\src\l2ccowsay")

from characters import DRAGON

def roar(txt: str = 'rrrrrr'):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + DRAGON

print(roar())
