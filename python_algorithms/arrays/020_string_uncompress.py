def string_uncompress(string: str) -> str:
    if len(string) == 0:
        return ""

    decompressed, current = "", 0

    while current < len(string):
        char = string[current]
        if char.isdigit():
            count = int(char)
            current += 1
            decompressed += string[current] * count
        else:
            decompressed += char
        current += 1

    return decompressed


if __name__ == "__main__":
    assert string_uncompress("") == ""
    assert string_uncompress("4eas2y") == "eeeeasyy"
