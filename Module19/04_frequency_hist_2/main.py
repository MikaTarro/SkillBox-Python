def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = 'здесь что-то написано'. lower()


string = 'здесь что-то написано' #input('Введите текст: ')

hist = {sym: string.count(sym) for sym in string}

print('\nОригинальный словарь частот:')
for key in sorted(hist.keys()):
    print(key, ':', hist[key])

rev_hist = {val: [i_key for i_key in hist.keys() if hist[i_key] == val] for val in set(hist.values())}

print('\nИнвертированный словарь частот:')
for rev_key in rev_hist:
    print(rev_key, ':', rev_hist[rev_key])