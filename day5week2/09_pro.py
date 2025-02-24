#count consonants
def counts(text):
    vowels="aeiouAEIOU"
    vow_count=0
    
    for char in text:
        #print(char)
        if char not in vowels:
            vow_count+=1
    print(f"Consonents counts are: {vow_count}")
text=str(input("Enter the text to check number of Consonents: "))
counts(text)