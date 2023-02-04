import string
alphabet = list(string.ascii_lowercase)
def thirdProg(pan_str):
    for i in alphabet:
        if pan_str.find(i) != -1:
            pass
        else:
            return "This sentence is not pannogram sentence"
        return "This sentence is pannogram sentence"

print(thirdProg(input("Enter pannogram sentence: ")))
