with open('awscli.txt', 'r') as file:
    lines = file.read()
    print(lines)

    private_key = lines.replace("\\n", "\n")

    print(private_key)