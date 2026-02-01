from pwn import remote

p = remote("scripting.ctf.pascalctf.it", 6004)

p.sendline(b"")

p.recvuntil(b"Module: ")
module = p.recvline().decode().strip()
print(module)

match module:
    case "Keypads":
        print("it is keypads!")
    case "Complicated Wires":
        print("it is complicated wires")
    case "Wires":
        print("it is wires")
    case "Button":
        print("it is button")
    case _:
        print(f"something new: {module}")

p.recvuntil(b"Data: ")
response = p.recvline().decode().strip()
print(response)

p.close()
