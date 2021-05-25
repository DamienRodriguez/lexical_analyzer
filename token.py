# Damien A Rodriguez
# CSCD 420 - Automata and Compilers
# This is the Token class, that will be used as a data class to place into a hashtable that will be used to look up
# the associated value within a dictionary that will be able to add things to itself when there are other things like literals
# involved into the mix. 


class Token:
    'This class is used strictly as a data class to be placed into a dictionary'    

#####################################################
# ATTRIBUTES 
#####################################################
    lexeme = ''
    token_name = ''
    attribute_val = ''
#####################################################





##################################################### 
# CONSTRUCTORS
#####################################################
    def __init__(self,lexeme, token_name, attribute_val):
        self.lexeme = lexeme
        self.token_name = token_name
        self.attribute_val = attribute_val

#####################################################





##################################################### 
# GETTERS
#####################################################
    def get_lexeme(self):
        return self.lexeme

    def get_token_name(self):
        return self.token_name
    
    def get_attribute_val(self):
        return self.attribute_val
#####################################################





#####################################################
# TEST CODE
# This code is not used anywhere else in the code
# and is only used for testing purposes
#####################################################

    def print_vals(self):
        return self.lexeme + ' | ' + self.token_name + ' | ' + self.attribute_val

#####################################################
