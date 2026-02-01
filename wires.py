# Output string of number

def solve(data: dict, info: dict) -> list:
    colors = data['colors']
    if data['amount'] == '3':
        if 'Red' not in colors:
            return ['2']
        elif colors[2] == 'White':
            return ['3']
        elif colors[0] == 'Blue' and colors[1] == 'Blue':
            return ['2']
        elif (colors[0] == 'Blue' or colors[1] == 'Blue') and colors[2] == 'Blue':
            return ['3']
        else:
            return['3']
    
    if data['amount'] == '4':
        pass
        
        
            