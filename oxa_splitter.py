syntax_equals_to   = ":"
syntax_fullstop    = ";"
syntax_print_start = "["
syntax_print_end   = "]"
syntax_quote       = "\""
def oxa_split(file):
    # Stage 1 file_content_array
    file = [char for char in file]
    file_content_array = []
    word = ""
    for i in file:
        if not word and not i.isalnum():
            file_content_array.append(i)
        elif word and not i.isalnum():
            file_content_array.append(word)
            word = ""
            file_content_array.append(i)
        elif i.isalnum():
            word = word + i

    # Stage 2 unsplit variables
    file_content_unsplit_vars = []
    variable = ""
    for i in file_content_array:
        if variable and i.isalnum() or i == " ":
            variable = variable + i 
        elif not variable and i.isalnum() or i == " ":
            variable = variable + i
        else: 
            file_content_unsplit_vars.append(variable)
            variable = ""
            file_content_unsplit_vars.append(i)

    # Stage 3 cleanup
    cleaned_file_content = []
    for i in file_content_unsplit_vars:
        if i == "" or i == " ":
            pass
        else:
            cleaned_file_content.append(i.strip())

    # Stage 4 string combines
    parsable_file_content = []
    string=[]
    final_string=''
    string_enable = False
    for i in cleaned_file_content:
        if not string_enable and i != syntax_quote:
            parsable_file_content.append(i)
        elif not string_enable and i == syntax_quote:
            string_enable = True
            string.append(i)
        elif string_enable and i != syntax_quote:
            string.append(i)
        elif string_enable and i == syntax_quote:
            string_enable = False 
            string.append(i)
            for x in string:
                final_string = final_string + x
            parsable_file_content.append(final_string)
            final_string=''
            string=[]

    return parsable_file_content    
            