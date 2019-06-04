ch=input()
if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    if((ch==('a'or'e'or'i'or'o'or'u') or (ch==('A'or'E'or'I'or'O'or'U')))):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
