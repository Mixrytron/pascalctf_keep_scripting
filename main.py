from pwn import remote
import json

p = remote("scripting.ctf.pascalctf.it", 6004)

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
r_dict = eval(response)  # convert to dict
print(r_dict)

match module:
    case "Keypads":
        print("it is Keypads")
    case "Complicated Wires":
        print("it is Complicated Wires")
    case "Wires":
        print("it is Wires")
    case "Button":
        print("it is Button")
    case _:
        print(f"something new: {module}")

# write data to the io

p.close()

# def button(data: dict) -> None:
