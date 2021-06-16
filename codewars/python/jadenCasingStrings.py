def to_jaden_case(string):
    # get tokens into a string
    token_list = string.split(sep =" ")
    string = ""
    for i in range(len(token_list)):
        if i == len(token_list) - 1:
            string = string + token_list[i].capitalize() + ""
        else:
            string = string + token_list[i].capitalize() + " "
            
    return string 