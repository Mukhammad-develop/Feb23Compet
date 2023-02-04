def secProg(real_str, sub_str):
    if real_str.find(sub_str):
        return "The substring exists in the string."
    else:
        return "The substring not exists in the string."

print(secProg(input("Enter the string : "), input("Input the substring to search : ")))
