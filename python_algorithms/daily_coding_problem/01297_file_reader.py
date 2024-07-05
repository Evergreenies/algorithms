"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""


class FileReader:
    def __init__(self, file_content: str) -> None:
        self.file_content = file_content
        self.file_pointer = 0
        self.buffer = []

    def read7(self) -> str:
        start = self.file_pointer
        end = min(self.file_pointer + 7, len(self.file_content))
        self.file_pointer = end

        return self.file_content[start:end]

    def read_n(self, n: int) -> str:
        result = []

        while self.buffer and len(result) < n:
            result.append(self.buffer.pop(0))

        while len(result) < n:
            chunk = self.read7()

            if not chunk:
                break

            chunk_length = min(len(chunk), n - len(result))
            result.extend(chunk[:chunk_length])
            self.buffer.extend((chunk[chunk_length:]))

        return "".join(result)


reader = FileReader("Hello World")

print(reader.read_n(5))
print(reader.read_n(4))
print(reader.read_n(3))
