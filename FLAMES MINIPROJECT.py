def flames(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    common_letters = set(name1) & set(name2)
    count = len(common_letters)
    flames_acronym = ["F", "L", "A", "M", "E", "S"]
    index = (len(name1) + len(name2) - count) % 6
    return flames_acronym[index]

def print_result(result):
    meanings = {
        "F": "Friends",
        "L": "Lovers",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    print(f"The result is: {result} ({meanings[result]})")

name1 = input("Enter the first person's name: ")
name2 = input("Enter the second person's name: ")
result = flames(name1, name2)
print_result(result)
