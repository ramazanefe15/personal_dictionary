import os
class dict_file:
    def __init__ (self,filename):
        self.filename=filename
    def load(self):
        if not os.path.exists(self.filename):
            with open(self.filename,"w") as f:
                print("File created")
        with open(self.filename,"r") as f:
            data=f.readlines()
        print(data)
        return data
    def save(self,data):
        with open(self.filename,"w") as f:
            for line in data:
                f.write(line.strip()+"\n")