##
#DEPENDENCIES

import re

#FUNCTIONS

def delete_retweets_func(lines):
    lines_copy = list() 
    for i in range(len(lines)):
        if 'RT' in lines[i]:
            continue 
        else:
            lines_copy.append(lines[i]) 
    return lines_copy

def delete_blank_cells_func(lines):
    lines_copy = list()
    for i in range(len(lines)):
        if lines[i] == ' ':
            continue
        else:
            lines_copy.append(lines[i])
    return lines_copy

def remove_links_func(lines):
    lines_copy = list()
    for i in range(len(lines)):
        if 'https' in lines[i]:
            continue
        else:
            lines_copy.append(lines[i])
    return lines_copy    

def remove_mentions_func(lines):
    lines_copy = list()
    for i in range(len(lines)):
        lines_copy.append(re.sub("@[A-Za-z0-9]+","", lines[i]))
    return lines_copy

def save_txt_func(lines,txt_name):
    f=open(txt_name,'w')
    for line in lines:
        f.write(line+'\n')

#MAIN CLASS

class filter_tweets:
    
    def __init__(self,data,encoding='utf-8'):

        self.data = data
        self.encoding = encoding

    def read_txt_file(self):
        with open(self.data, 'r', errors='replace', encoding=self.encoding) as f:
            self.lines = f.readlines()

    def read_list(self):
        self.lines = self.data

    def apply_filter(self,delete_retweets=True,delete_blank_cells=True,remove_links=True,remove_mentions=False):

        if delete_retweets == True:
            self.lines = delete_retweets_func(self.lines)

        if delete_blank_cells == True:
            self.lines = delete_blank_cells_func(self.lines)

        if remove_links == True:
            self.lines = remove_links_func(self.lines)

        if remove_mentions == True:
            self.lines = remove_mentions_func(self.lines)

    def get_filtered_data(self):
        
        return self.lines 

    def to_txt(self,txt_name):

        print(f"FILENAME: {txt_name}")
        print(f"FILE LENGHT: {len(self.lines)}")
        save_txt_func(self.lines,txt_name)
        print("FILE SAVED")

        
        
## GIST LINK FOR EXAMPLES: https://gist.github.com/HenrySilvaCS/1e23b55ab02ce0ec11c933330c51a64f
