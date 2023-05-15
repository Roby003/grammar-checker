def check_word(grammar,word,symbol):
    if len(word)==0:
        if symbol in grammar:
            for i in grammar[symbol]:
                if i[1]=='$':
                    return True
        elif symbol=='$':
            return True
    else:
        if symbol in grammar:
            for i in grammar[symbol]:
                if word[0] in i: 
                    if check_word(grammar,word[1:],i[1]):
                        return True    

grammar = {'S':[['a','A'],['d','E']]
           ,'A':[['a','B'],['a','S']]
           ,'B':[['b','C']]
           , 'C':[['b','D'],['b','B']]
           , 'D':[['c','D'],['e','$'],[ '$', '$' ]]
           ,'E':[['d','$']]}
start_symbol = 'S'
word='aabbe'
print(check_word(grammar,word,start_symbol))
