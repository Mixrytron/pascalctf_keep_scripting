symbols = "Ѽ æ © Ӭ Ҩ  Ҋ  ϗ  ϰ  Ԇ  Ϙ  Ѯ  ƛ  Ω  ¶  ¿  Ϭ  Ͼ  Ͽ  ҂  Ѣ  Ѭ  Ѧ  Җ  ψ  ټ  ☆ ★"

arrays = [
    ["Ϙ", "Ѧ", "ƛ", "ϰ", "Ѭ", "ϗ", "Ͽ"],
    ["Ӭ", "Ϙ", "Ͽ", "Ҩ", "☆", "ϗ", "¿"],
    ["©", "Ѽ", "Ҩ", "Җ", "Ԇ", "ƛ", "☆"],
    ["k", "¶", "Ѣ", "Ѭ", "Җ", "¿", "ټ"],
    ["ψ", "ټ", "Ѣ", "Ͼ", "¶", "Ѯ", "★"],
    ["k", "Ӭ", "҂", "æ", "ψ", "Ҋ", "Ω"],
]

target = ["Ҋ", "ψ", "҂", "Ω"]
data = {"symbols": target}

# print(set(target).issubset(arrays[0]))
# print(set(target).issubset(arrays[1]))
# print(set(target).issubset(arrays[2]))
# print(set(target).issubset(arrays[3]))
# print(set(target).issubset(arrays[4]))
# print(set(target).issubset(arrays[5]))


def find_target_array(target) -> int:
    for i in range(len(arrays)):
        if set(target).issubset(arrays[i]):
            return i
    return -1


def compute_order(data: dict) -> list[str]:
    order = []
    symbols = data["symbols"]
    for i in arrays[find_target_array(symbols)]:
        if i in symbols:
            order.append(str(symbols.index(i) + 1))

    return order
