"""
Write right justify function, taking string as input argument
"""


def right_justify(str):
    line_len = 71
    justified_line = ""
    strlen = len(str);

    if strlen > 70:
        print "Greater than line length"
        return

    fill_length = line_len - strlen 

    for i in range(1, fill_length):
        justified_line += " "

    justified_line += str

    print justified_line, len(justified_line)

str = raw_input("Enter string\n")
right_justify(str)
