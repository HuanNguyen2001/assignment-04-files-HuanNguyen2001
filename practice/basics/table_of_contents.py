def table_of_contents(filename):
    """Дописать оглавление и номер его начала в файл (см. _legend.md)"""
    with open(filename, 'r+') as f:
        f.seek(0)
        f.write('\n')
        lines = f.readlines()
        d = 0
        z = 0
        u = 0
        for line in lines:
            d += 1
            if '#' in line:
                u += 1
                if u == 1:
                    g = line[1:len(line) - 1]
                    f.writelines(str(d) + '.....' + str(g))
                if u > 1:
                    g = line[1:len(line) - 1]
                    f.write('\n')
                    f.writelines(str(d) + '.....' + str(g))
        o = f.read()
    with open(filename, 'r+') as f:
        f.write(o)
        y = f.read()
    with open(filename, 'r+') as f:
        if d == 0 or d == 10:
            d += 1
        f.writelines(str(d + 2))
        f.write('\n')
        f.write(y)
    return f
