def generate_duplicate_flowers():
    """A generator that yields flower names, each duplicated."""

    flower = yield

    while True:
        print(flower)
        flower = yield

duplicate_flower = generate_duplicate_flowers()

duplicate_flower.send(None)  # Prime the generator

duplicate_flower.send("Dhotra")
duplicate_flower.send("Chameli")

duplicate_flower.close()