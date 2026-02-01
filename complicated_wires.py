# Output: list of 'cut' or 'skip'
# Data: {'amount': 2, 'colors': ['White', 'Red'], 'leds': [True, True], 'stars': [True, True]}

# key: red, blue, star, led
WIRE_TO_LETTER = {
    '0000': 'C', '0001': 'D', '0010': 'C', '0011': 'B',
    '0100': 'S', '0101': 'P', '0110': 'D', '0111': 'P', 
    '1000': 'S', '1001': 'B', '1010': 'C', '1011': 'B',
    '1100': 'S', '1101': 'S', '1110': 'P', '1111': 'D'
}

def solve(data: dict, info: dict) -> list:
    solution = []
    
    for i in range(data['amount']):
        wire = "".join(str(int(b)) for b in [
            'Red' in data['colors'][i],
            'Blue' in data['colors'][i],
            data['stars'][i] == 'True',
            data['leds'][i] == 'True'
        ])
        match (WIRE_TO_LETTER[wire]):
            case 'C':
                solution.append('cut')
            case 'D':
                solution.append('skip')
            case 'S':
                if info['Serial Number'][-1] == 7:
                    solution.append('cut')
            case 'P':
                if 'parallel' in info['Ports']:
                    solution.append('cut')
            case 'B':
                if int(info['Batteries']) >= 2:
                    solution.append('cut')
    
    return solution