from pwn import remote
from keypads import Keypads
from complicated_wires import CWire


def write_output(p, answer_sequence):
    # p.sendline(" ".join(answer_sequence).encode())
    for i in answer_sequence:
        p.sendline(i.encode())


def read_solve_cycle(p) -> None:
    bomb_info: dict = {}
    p.recvuntil(b"Serial Number: ")
    bomb_info["Serial Number"] = p.recvline().decode().strip()

    p.recvuntil(b"Batteries: ")
    bomb_info["Batteries"] = p.recvline().decode().strip()

    p.recvuntil(b"Label: ")
    bomb_info["Label"] = p.recvline().decode().strip()

    p.recvuntil(b"Ports: ")
    bomb_info["Ports"] = p.recvline().decode().strip().split(", ")

    print(bomb_info)

    p.sendline(b"")

    p.recvuntil(b"Module: ")
    module = p.recvline().decode().strip()
    print(module)

    p.recvuntil(b"Data: ")
    response = p.recvline().decode().strip()
    data = eval(response)  # convert to dict
    print(data)

    match module:
        case "Keypads":
            print("it is Keypads")
            keypads = Keypads()
            answer_sequence = keypads.compute_order(data)
            print(answer_sequence)
            write_output(p, answer_sequence)
        case "Complicated Wires":
            print("it is Complicated Wires")
            c_wire = CWire()
            answer_sequence = c_wire.solve(data, bomb_info)
            print(answer_sequence)
            write_output(p, answer_sequence)
        case "Wires":
            print("it is Wires")
        case "Button":
            print("it is Button")
        case _:
            print(f"something new: {module}")

    # p.sendline(b"")
    p.interactive()


def main() -> None:
    p = remote("scripting.ctf.pascalctf.it", 6004)
    read_solve_cycle(p)


if __name__ == "__main__":
    main()

# def button(data: dict) -> None:
