# 1. Press and release immediately
# 2. Hold until timer shows specific digit

def solve(data: dict, info: dict) -> list:
    solution = []
    batteries = int(info['Batteries'])
    indicator = info['Label']
    
    if data['color'] == 'Blue' and data['text'] == 'Abort':
        release_held_button(solution, data['strip_color'])
    elif batteries > 1 and data['text'] == 'Detonate':
        pass    
    return solution


def release_held_button(solution: list, strip_color: str):
    solution.append('2')
    if strip_color == 'Blue':
        solution.append('4')
    elif strip_color == 'White':
        solution.append('1')
    elif strip_color == 'Yellow':
        solution.append('5')
    else:
        solution.append('1')
        
            