class Shortlived:
    def __init__(self, name, file):
        self.name = name
        self.file = open(file, "w")

    def write(self, data):
        self.file.write(data)

    def __del__(self):
        self.file.close()

file = "text.txt"

file_writer = Shortlived("Amarendra", file)

file_writer.write("Why Katappa?")

del file_writer