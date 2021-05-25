# Damien Rodriguez
# CSCD 420 - Automata and Compilers
# This program acts as a very simple lexical analyzer for
# .php files


import sys
import re   #look through later. Probably can use a regular expression to find everything we need
import os.path
import token_table


global sym_suffix
sym_suffix = '.sym'

global tkn_suffix
tkn_suffix = '.tkn'

#####################################################
# MAIN DRIVER CODE
# This section of code is strictly to get the
# program running. 
# 
# COMMAND FOR COMMANDLINE: python lex.py filename
#####################################################

def main():
    fn = sys.argv[1] # system argument 1 is our file we are working with
    prefix = get_file_prefix(fn)
    create_files(prefix)
    fin = open_file(fn) # remember to close file at the end of main
    

    array = sym_pass(fin)
    sym_create(array, prefix)
    

    fin.seek(0) # fin.seek(0) will return file pointer to the start of the file
    
    tkn_array = tkn_pass(fin)
    print(tkn_array)



    fin.close()

#####################################################





#####################################################
# FILES SECTION
# The functions below are all about working with the
# files that will be worked with.
#####################################################

def open_file(file_name):
    return open(file_name)


def get_file_prefix(file_name):
    return file_name.split('.')[0]


def create_files(prefix):
    fn1 = prefix + sym_suffix
    fn2 = prefix + tkn_suffix

    create_file(fn1)
    create_file(fn2)

def create_file(fn):
    if not os.path.exists('./'+fn):
        print("File " + fn + " successfully created...")
        f = open(fn,'x')
        f.close()

#####################################################





#####################################################
# SYMBOL TABLE CREATION
# The fucntions below have to do with the creation
# and filling in of the symbol table.
#####################################################

def sym_pass(file):
    array = file.readlines()
    r_array = []
    for i in array:
        r_array.append(re.findall(r'\$[a-zA-Z0-9_]*',i))

    r_array = delete_duplicate_variables(r_array)
    return r_array

def delete_duplicate_variables(array):
    r_array = []
    for i in array:
        for j in i:
            if '$' in j and not j in r_array: r_array.append(j)
    
    return r_array


def sym_create(array, prefix):
    file_name = prefix + sym_suffix
    
    file = open(file_name, 'w')
    for i in range(0, len(array)):
        file.write(str(i) + "\t\t" + array[i] +"\n")
    
    file.close()

#####################################################


# TO DO
# Token file creation

def tkn_pass(file):
    array = file.readlines()
    r_array = []
    
    for line in array:
        temp_array = []

        char_queue = list(line)             # We now have an array whose items are all of the characters that are found in the file.
        temp_array = tokenize(char_queue)   # Call method that tokenizes the lines and returns all of the objects we are looking for
        r_array.append(temp_array)          # Append the returned tokens to a larger array that will serve as the template

    return r_array                          # return larger array of tokens for creation of the file




# In this method, our queue is a list that is a char array made from a single line within
# The file we are working with.
def tokenize(queue):
    r_array = []
    token_lookup = token_table.Token_Table()



    while(len(queue) != 0):
                
        peak = queue[0]
        if peak == ' ' or peak == '\n':
            print("WHITE SPACE FOUND\n")
            queue.pop(0)




        elif peak in token_lookup.operators_list:     # Operations operators
            print("OPERATOR FOUND\n")
            if peak == '!':                         # Need to handle ! edge case
                i = queue.pop(0)
                r_array.append(i)
            else:                                   # Everything else can be handled like in the human words check
                r_array.append(construct_kw_or_id(queue))

        
        elif peak in token_lookup.punctuation_list:      # Punctuation operators
            # Need to handle string literals within this portion of the if block

            print("PUNCTUATION FOUND\n")
            i = queue.pop(0)
           
            if(len(queue) > 0):                         #checking to make sure we aren't looking ahead in an
                                                        #empty queue

                peak = queue[0]

                if peak == '>':                             # Need to handle arrow edge cases
                    i+=queue.pop(0)
            
            print(i)
            r_array.append(i)

 
        elif peak.isalpha() or peak == '_' or peak == '$':             # human words check
            print("KEYWORD OR OTHER HUMAN WORD FOUND\n")
            word = construct_kw_or_id(queue)
            print(word)
            r_array.append(word)


    # Peek stack to see where we should start processing
    # Order in which we will check the stack:
    #   1. human words
    #   2. Punctuation
    #   3. Operators
    #   4. Literally anything else

    print("RETURNED ARRAY: \n")
    print(r_array)
    print("##########################\n")
    return r_array




# This function is used to help construct tokens that are used for tokens.
# The tokens this function will handle are ones that are between things 
# that are in white space. (e.g. $var = 18)
def construct_kw_or_id(queue):
    token = ""
    i = queue.pop(0)
    while(i != ' '):
        token += i
        if(len(queue) > 0):
            i = queue.pop(0)
        else:
            break

    return token.strip()








main()
