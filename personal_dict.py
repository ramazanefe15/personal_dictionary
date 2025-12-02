import dictfilehandle
import regex
class PersonalDict:
    def __init__ (self,filename):
        self.filename=filename
        self.file=dictfilehandle.dict_file(filename)
    def seperate_word(self,word):
        reg=r"[a-zA-Z]+"
        x=regex.findall(reg,word)
        return x[0]
    def add(self,word):
        ex_data=self.file.load()
        self.file.save(ex_data+[word])
    def delete(self,word):
        ex_data=self.file.load()
        new_data=[]
        for ex in ex_data:
            if self.seperate_word(ex)!=word:
                new_data+=[ex]
        self.file.save(new_data)
    def show_word(self,word):
        data=self.file.load()
        for ex in data:
            if self.seperate_word(ex)==word:
                print(ex)
                break
    def show_all(self):
        data=self.file.load()
        for line in data:
            print(line)
    def edit(self,word,new_def):
        ex_data=self.file.load()
        new_data=[]
        for ex in ex_data:
            if self.seperate_word(ex)==word:
                new_data+=[f"{word} : {new_def}"]
            else:
                new_data+=[ex]
        self.file.save(new_data)