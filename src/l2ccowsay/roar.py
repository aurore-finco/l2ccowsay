from .characters import DRAGON

def roar(txt: str = 'rrrrrr'):
    tt = f'{"="*(len(txt)+4)}\n'
    tt += f"| {txt} |\n"
    tt += f'{"="*(len(txt)+4)}'
    return tt + DRAGON

print(roar())
