import personal_dict
def main():
    pdict=personal_dict.PersonalDict("my_dict.txt")
    while  True:
        print("Enter the action you want to do: ")
        print("1-Add Word")
        print("2-Edit word")
        print("3-Delete Word")
        print("4-Show Word")
        print("5-Show all")
        print("6-Exit")
        try:
            action=int(input())
        except ValueError:
            print("You didn't enter a number!")
            continue
        if action==1:
            word=input("Please neter a word: ")
            deft=input("Please enter a definition: ")
            pdict.add(f"{word} : {deft}")
        elif action==2:
            word=input("Please enter the word you want to change: ")
            new_def=input("Please neter a new definition: ")
            pdict.edit(word,new_def)
        elif action==3:
            word=input("Please enter the word you want to delete: ")
            pdict.delete(word)
        elif action==4:
            word=input("Please enter the word you want to show: ")
            pdict.show_word(word)
        elif action==5:
            pdict.show_all()
        elif action==6:
            print("Exiting...")
            break
        else:
            print("Select from listed actions above")
if __name__ == "__main__":
    main()