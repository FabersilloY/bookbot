from operator import itemgetter

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        characters = {}
        for char in file_contents:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    sorted_list(characters)

def sorted_list(dict):
    clean = []
    for key in dict:
        if key.isalpha():
            di = ({
                "letter": key,
                "amount": dict[key]
            })
            clean.append(di)

    sorted_list = sorted(clean, key=itemgetter("amount"), reverse=True)
    print(sorted_list)

    for char in sorted_list:
        letter = char.get("letter")
        amount = char.get("amount")
        print(f"The letter {letter} was used {amount} times in this book.")
    
          

        

main()