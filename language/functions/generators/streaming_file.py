file = "text.txt"

def generate_file_streamer(file):
    with open(file, "r") as f:
        for line in f:
            yield line

file_stream = generate_file_streamer(file)
file_lines = []

while True:
    try:
        next_line = next(file_stream)
        file_lines.append(next_line)
        print(next_line)
    except:
        break