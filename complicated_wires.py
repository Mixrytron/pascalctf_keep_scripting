# Output: list of 'cut' or 'skip'
# Data: {'amount': 2, 'colors': ['White', 'Red'], 'leds': [True, True], 'stars': [True, True]}

# key: red, blue, star, led


class CWire:
    def __init__(self) -> None:
        self.WIRE_TO_LETTER = {
            "0000": "C",
            "0001": "D",
            "0010": "C",
            "0011": "B",
            "0100": "S",
            "0101": "P",
            "0110": "D",
            "0111": "P",
            "1000": "S",
            "1001": "B",
            "1010": "C",
            "1011": "B",
            "1100": "S",
            "1101": "S",
            "1110": "P",
            "1111": "D",
        }

    def solve(self, data: dict, info: dict) -> list:
        solution = []

        for i in range(data["amount"]):
            wire = "".join(
                str(int(b))
                for b in [
                    "Red" in data["colors"][i],
                    "Blue" in data["colors"][i],
                    data["stars"][i] is True,
                    data["leds"][i] is True,
                ]
            )
            print(wire)
            match self.WIRE_TO_LETTER[wire]:
                case "C":
                    solution.append("cut")
                case "D":
                    solution.append("skip")
                case "S":
                    if int(info["Serial Number"][-1]) % 2 == 0:
                        solution.append("cut")
                    else:
                        solution.append("skip")
                case "P":
                    if "parallel" in info["Ports"]:
                        solution.append("cut")
                    else:
                        solution.append("skip")
                case "B":
                    if int(info["Batteries"]) >= 2:
                        solution.append("cut")
                    else:
                        solution.append("skip")

        return solution


# Testing
if __name__ == "__main__":
    cw = CWire()
    d = {
        "amount": 2,
        "colors": ["Blue", "Blue"],
        "leds": [False, True],
        "stars": [False, False],
    }
    info = {
        "Serial Number": "356813",
        "Batteries": "1",
        "Label": "CAR",
        "Ports": ["parallel", "ps2", "serial"],
    }
    answer = cw.solve(d, info)
    print(answer)
