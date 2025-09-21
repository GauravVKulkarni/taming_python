try:
    print(100 / 0)
except Exception as e:
    print(e)
finally:
    print("Condemned to clean memory")