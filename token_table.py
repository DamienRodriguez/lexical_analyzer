# Damien A Rodriguez
# CSCD 420 - Automata and Compilers
# This is a class that is used to fill in a look up table to be then used to fill in the .tkn file

# This is where the values for our tokens will be placed into to be checked. 
import token


class Token_Table:
    'This class is where a dictionary is that gives us a hashtable of sorts to quickly look up token values'
#####################################################
# ATTRIBUTES 
#####################################################
    token_dic = {}
    punctuation_list = [
        '(',
        ')',
        '{',
        '}',
        '[',
        ']',
        "->",
        "=>",
        ';',
        ':',
        '"',
        "'",
            ]

    operators_list = [
        "=",
        "==",
        "<",
        ">",
        "!=",
        "<=",
        ">=",
        "<=>",
        "===",
        "!=",
        "+",
        "-",
        "*",
        "/",
        "%",
        "++",
        "--",
        "+=",
        "-=",
        "*=",
        "/=",
        "%=",
        "&&",
        "and",
        "||",
        "or",
        "xor",
        "!",
            ]

##################################################### 





##################################################### 
# CONSTRUCTORS
#####################################################
    def __init__(self):
        self.fill_table()
##################################################### 





##################################################### 
# FUNCTIONS
#####################################################
# fill_table: fills in the dictionary that we are
#             using to look up accepted tokens
#####################################################
# find_accepted_token: takes in a token read from the
#                      file and returns the respective
#                      Token object
#####################################################
    def fill_table(self):
        temp_token = 0 
        file = open('DO_NOT_DELETE.txt','r')
        token_array = file.readlines()

        for i in token_array:
            temp_array = i.split(',')
            temp_token = token.Token(temp_array[0], temp_array[1], temp_array[2])
            self.token_dic[temp_array[0]] = temp_token

        file.close()

    def find_accepted_token(self,token):
        return self.token_dic[token]
#####################################################
