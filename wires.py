# Output string of number

def solve(data: dict, info: dict) -> list:
    colors = data['colors']
    if data['amount'] == '3':
        if 'Red' not in colors:
            return ['2']
        elif colors[-1] == 'White':
            return ['3']
        elif colors.count('Blue') > 1:
            return [str(len(colors) - colors[::-1].index('Blue'))] # last blue wire
        else:
            return['3']
    
    if data['amount'] == '4':
        if colors.count('Red') > 1 and (int(info['Serial Number'][-1]) % 2) == 1:
            return [str(len(colors) - colors[::-1].index('Red'))] # last red wire
        elif colors[-1] == 'Yellow' and 'Red' not in colors:
            return ['1']
        elif colors.count('Blue') == 1:
            return ['1']
        elif colors.count('Yellow') > 1:
            return ['1']
        else:
            return ['2']
    
    if data['amount'] == '5':
        if colors[-1] == 'Black' and (int(info['Serial Number']) % 2 == 1):
            return ['4']
        elif colors.count('Red') == 1 and colors.count('Yellow') > 1:
            return ['1']
        elif 'Black' not in colors:
            return ['2']
        else:
            return ['1']
        
    if data['amount'] == '6':
        if 'Yellow' not in colors and (int(info['Serial Number']) % 2 == 1):
            return ['3']
        elif colors.count('Yellow') == 1 and colors.count('White') > 1:
            return ['4']
        elif 'Red' not in colors:
            return ['6']
        else:
            return ['4']        
            