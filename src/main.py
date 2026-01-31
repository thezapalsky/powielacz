
if __name__ == "__main__":
    words = open("data/names.txt", "r").read().splitlines()
    print(words[:10])
    print(len(words))
