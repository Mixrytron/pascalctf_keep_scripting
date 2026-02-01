symbols = "Ѽ æ © Ӭ Ҩ  Ҋ  ϗ  ϰ  Ԇ  Ϙ  Ѯ  ƛ  Ω  ¶  ¿  Ϭ  Ͼ  Ͽ  ҂  Ѣ  Ѭ  Ѧ  Җ  ψ  ټ  ☆ ★"


class Keypads:
    def __init__(self) -> None:
        self.arrays = [
            ["Ϙ", "Ѧ", "ƛ", "Ϟ", "Ѭ", "ϗ", "Ͽ"],
            ["Ӭ", "Ϙ", "Ͽ", "Ҩ", "☆", "ϗ", "¿"],
            ["©", "Ѽ", "Ҩ", "Җ", "Ԇ", "ƛ", "☆"],
            ["б", "¶", "ƀ", "Ѭ", "Җ", "¿", "ټ"],
            ["ψ", "ټ", "ƀ", "Ͼ", "¶", "Ѯ", "★"],
            ["б", "Ӭ", "҂", "æ", "ψ", "Ҋ", "Ω"],
        ]

    def find_target_array(self, target) -> int:
        for i in range(len(self.arrays)):
            if set(target).issubset(self.arrays[i]):
                return i
        return -1

    def compute_order(self, data: dict) -> list[str]:
        order = []
        symbols = data["symbols"]
        index = self.find_target_array(symbols)
        if index < 0:
            raise IndexError("The array is wrong!")
        for i in self.arrays[index]:
            if i in symbols:
                order.append(str(symbols.index(i) + 1))

        return [" ".join(order)]


if __name__ == "__main__":
    keypads = Keypads()
    # d = {"symbols": ["ټ", "ƀ", "Ͼ", "ψ"]}
    # d = {"symbols": ["ƛ", "Ϟ", "Ѭ", "ϗ"]}
    d = {"symbols": ["¶", "б", "Җ", "¿"]}
    print(keypads.find_target_array(d["symbols"]))
