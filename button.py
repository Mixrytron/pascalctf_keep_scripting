# 1. Press and release immediately
# 2. Hold until timer shows specific digit

def solve(data: dict, info: dict) -> list:
    solution = []
    batteries = int(info['Batteries'])
    indicator = info['Label']
    
    if data['color'] == 'Blue' and data['text'] == 'Abort':
        # 1
        release_held_button(solution, data['color_strip'])
    elif batteries > 1 and data['text'] == 'Detonate':
        # 2
        solution.append('1')
    elif data['color'] == 'White' and indicator == 'CAR':
        # 3
        release_held_button(solution, data['color_strip'])
    elif batteries > 2 and indicator == 'FRK':
        # 4
        solution.append('1')
    elif data['color'] == 'Yellow':
        # 5
        release_held_button(solution, data['color_strip'])
    elif data['color'] == 'Red' and data['text'] == 'Hold':
        # 6
        solution.append('1')
    else:
        release_held_button(solution, data['color_strip'])
        
    return solution


def release_held_button(solution: list, strip_color: str):
    solution.append('2')
    match (strip_color):
        case 'Blue':
            solution.append('4')
        case 'White':
            solution.append('1')
        case 'Yellow':
            solution.append('5')
        case _:
            solution.append('1')
            