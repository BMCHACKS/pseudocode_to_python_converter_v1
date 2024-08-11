'''
    how it works:
    input is taken line by line, instead of taking it all and storing in a list, 
    each line is converted and then sotred in the list till 'END' is entered where
    converted lines are output, any extra function called i.e other_fuctions_2(), it 
    is added to the main program once.
'''

# global vars
pcc, cr, ef, classes = [[] for _ in range(4)]
line_counter = 0
flag_list = [False for _ in range(21)]


def boolean_fixer(al):
    boolean_logic = ['AND', 'OR', 'NOT']
    boolean_logic_tf = ['TRUE', 'FALSE']
    if_else = ["IF", "ELSE", "ELSEIF", "ELSE IF"]

    for i in range(len(al)):
        if al[i] == "<>":
            al[i] = "!="
        if al[i] in boolean_logic:
            al[i] = al[i].lower()
        if al[i] == "=":
            al[i] = al[i] + "="
        if al[i] in boolean_logic_tf:
            al[i] = "True" if al[i] == "TRUE" else "False"
        if al[i] in if_else:
            if al[i] == if_else[0]:
                al[i] = 'if'
            elif al[i] == if_else[1]:
                al[i] = 'else'
            elif al[i] == if_else[2] or if_else[3]:
                al[i] = 'elif'
    return al


def other_functions_2(al):
    global ef, flag_list
    # ok other functions!
    al = "".join(al)
    if "LENGTH(" in al and flag_list[0] == False:
        ef.append("def LENGTH(string): return len(string)")
        flag_list[0] = True
    if "LCASE(" in al and flag_list[1] == False:
        ef.append("def LCASE(char): return char.lower()")
        flag_list[1] = True
    if "UCASE(" in al and flag_list[2] == False:
        ef.append("def UCASE(char): return char.upper()")
        flag_list[2] = True
    if "TO_UPPER(" in al and flag_list[3] == False:
        ef.append("def TO_UPPER(string): return string.upper()")
        flag_list[3] = True
    if "TO_LOWER(" in al and flag_list[4] == False:
        ef.append("def TO_LOWER(string): return string.lower()")
        flag_list[4] = True
    if "NUM_TO_STR(" in al and flag_list[5] == False:
        ef.append("def NUM_TO_STR(num): return str(num)")
        flag_list[5] = True
    if "STR_TO_NUM(" in al and flag_list[6] == False:
        ef.append('def STR_TO_NUM(string): return float(string) if "." in string else int(string)')
        flag_list[6] = True
    if "IS_NUM(" in al and flag_list[7] == False:
        ef.append("def IS_NUM(string): return string.isnumeric()")
        flag_list[7] = True
    if "ASC(" in al and flag_list[8] == False:
        ef.append("def ASC(char): return ord(char)")
        flag_list[8] = True
    if "CHR(" in al and flag_list[9] == False:
        ef.append("def CHR(char): return chr(char)")
        flag_list[9] = True
    if "INT(" in al and flag_list[10] == False:
        ef.append("def INT(x): return int(x)")
        flag_list[10] = True
    if "RAND(" in al and flag_list[11] == False:
        ef.append("import random")
        ef.append("def RAND(x): return round(random.uniform(0, x-1), 2)")
        flag_list[11] = True
    if "LEFT(" in al and flag_list[12] == False:
        ef.append("def LEFT(string, x): return string[:x]")
        flag_list[12] = True
    if "RIGHT(" in al and flag_list[13] == False:
        ef.append("def RIGHT(string, x): return string[len(string)-x:]")
        flag_list[13] = True
    if "MID(" in al and flag_list[14] == False:
        ef.append("def MID(string, x, y): return string[x-1:x+y-1]")
        flag_list[14] = True
    if "DAY_INDEX(" in al or "NOW(" in al:
        ef.append("from datetime import date")
        if "DAY_INDEX(" in al and flag_list[15] == False:
            ef.append("def DAY_INDEX(thisdate): return DAY_INDEX_FIX(thisdate.weekday())")
            ef.append("def DAY_INDEX_FIX(thisday):")
            ef.append("    og = [0,1,2,3,4,5,6]")
            ef.append("    ng = [2,3,4,5,6,7,1]")
            ef.append("    return ng[og.index(thisday)]")
            flag_list[15] = True
        if "NOW(" in al and flag_list[16] == False:
            ef.append("def NOW(): return date.today()")
            flag_list[16] = True
    if "SETDATE(" in al and flag_list[17] == False:
        ef.append('def SETDATE(day, month, year): return f"{day}/{month}/{year}"')
        flag_list[17] = True
    if "YEAR(" in al and flag_list[18] == False:
        ef.append("def YEAR(thisdate): return str(thisdate).split('-')[0]")
        flag_list[18] = True
    if "MONTH(" in al and flag_list[19] == False:
        ef.append("def MONTH(thisdate): return str(thisdate).split('-')[1]")
        flag_list[19] = True
    if "DAY(" in al and "INDEX" not in al and flag_list[20] == False:
        ef.append("def DAY(thisdate): return str(thisdate).split('-')[2]")
        flag_list[20] = True


def other_functions_1(al):
    ofs = ["DIV", "MOD", "&"]
    # MOD, DIV, & - done
    if ofs[0] in al: al[al.index(ofs[0])] = "//"
    if ofs[1] in al: al[al.index(ofs[1])] = "%"
    if ofs[2] in al: al[al.index(ofs[2])] = "+"
    # look at other_functions_2 for other functions
    return " ".join(al)


def class_fixer():
    global classes
    # currently only works if there is only one record type - opps
    to_add = []
    var_names = []
    dtd = [":", "DECLARE", "REAL", "BOOLEAN", "INTEGER", "STRING", "CHAR"]
    for p in range(len(pcc)):
        if "class" in pcc[p]: break
    for c in range(len(cr)):
        if "TYPE" in cr[c]: break 
    for i in range(c+1, len(cr)):
        s = [str(x) for x in cr[i].split()]
        for x in dtd:
            try:
                s.remove(x)
            except ValueError:
                pass
        to_add.append(s[0])
    s = "   def __init__(self"
    for x in to_add:
        s = s + ", " + x
    classes.append(f"{s})")
    for x in to_add:
        classes.append(f"       self.{x} = {x}")


def converter(x):
    
    # symbols for maths
    artimatic_symbols = ['*', '+', '-', '/']
    s = ""
    xl = [str(x) for x in x.split()]
 
    try:
        # constant
        if xl[0] == "CONSTANT":
            xl.remove(xl[0])
            return " ".join(xl)

        # now the most simple one - RETURN
        if xl[0] == "RETURN":
            xl[0] = "return"
            xl = boolean_fixer(xl)
            s = " ".join(xl)
            return s

        # type <name> // class
        if xl[0] == "TYPE": 
            classes.append(f"class {xl[1]}:")
            return None
        if xl[0] == "ENDTYPE" or xl[0] == "END TYPE": 
            class_fixer()
            return None
        # other functions pt.2
        other_functions_2(xl)

        # ...
        ofs = ["DIV", "MOD", "&"]
        if any(symbol in xl for symbol in ofs):
            xl = other_functions_1(xl)
            xl = converter(xl)
            return xl

        # input/output stuff
        if xl[0] == "INPUT":
            return f"{xl[1]} = input()"
        if xl[0] == "OUTPUT":
            xl.remove("OUTPUT")
            for i in range(len(xl)):
                s = s + str(xl[i]) + " "
            s = s[:-1]
            return f"print({s})"

        # now lets do the MOST important thing... IF statements

        ifs = ["IF", "ELSE", "ELSEIF"]
        if xl[0] in ifs:
            try:
                xl.remove("THEN")
            except ValueError:
                pass
            xl = boolean_fixer(xl)
            for i in range(len(xl)):
                    s = s + xl[i] + " "
            s = s[:-1]
            return f"{s}:"


        # aritimatic stuff
        if any(symbol in xl for symbol in artimatic_symbols):
            for i in range(1, len(xl)):
                s = s + xl[i] + " "
            s = s[:-1]
            s = s.replace("<--", "=")
            return f"{xl[0]} {s}"


         #below are loops - FOR, WHILE, REPEAT
        # Starting with For Loop
            # additons made: made sure that now for loop can handle variables instead of only int-type
                # made sure that for loops can hadle ex. FOR COUNT <-- 1 TO var STEP 2 etc.
        if xl[0] == "FOR":
            if len(xl) == 8:
                if xl[3].isnumeric() and xl[5].isnumeric():
                    return f"for {xl[1]} in range({int(xl[3])}, {int(xl[5])+1}, {int(xl[7])}):"
                else:
                    return f"for {xl[1]} in range({xl[3]}, {xl[5]}, {xl[7]}):"
            elif xl[3].isnumeric() and xl[5].isnumeric():
                return f"for {xl[1]} in range({int(xl[3])}, {int(xl[5])+1}):"
            else:
                return f"for {xl[1]} in range({xl[3]}, {xl[5]}):"

        # --> WHILE loop
        if xl[0] == "WHILE":
            # lower casing and upper casing depending on a case of :/
            xl = boolean_fixer(xl)
            for i in range(1,len(xl)):
                s = s + xl[i] + " "
            s = s[:-1]
            return f"while {s}:"

        # repeat until loop :)
        if xl[0] == "REPEAT":
            return "while True:"
        if xl[0] == "UNTIL":
            xl = boolean_fixer(xl)
            for i in range(1,len(xl)):
                s = s + xl[i] + " "
            s = s[:-1]
            return f"if {s}: break"


        # assignment checker :D
        if len(xl) > 1:
            if xl[1] == "<--":
                if len(xl) == 3:
                    xl = boolean_fixer(xl)
                    return f"{xl[0]} = {xl[2]}"
                else:
                    for i in range(2, len(xl)):
                        s = s + xl[i] + " "
                    s = s[:-1]
                    return f"{xl[0]} = {s}"

        # FUNCTIONS & PROCEDURES T_T

        things_to_remove = ["BYVAL", "BYREF", ":", "STRING", "INTEGER", "REAL", "BOOLEAN", "CHAR", ","]
        if (xl[0] == "FUNCTION" or xl[0] == "PROCEDURE") and "()" not in str(xl[1]):
            # removing 'RETURNS <datatype>'
            p = True if things_to_remove[0] in xl or things_to_remove[1] in xl else False
            if xl[0] == "FUNCTION":
                xl.pop()
                xl.pop()
            # change function / procedure --> def
            xl[0] = "def"
            # now lets remove all useless stuff :)
            for i in range(len(xl)):
                for x in things_to_remove:
                    try:
                        xl[i] = str(xl[i]).replace(x, "")
                    except ValueError:
                        pass
            if p:
                vars = []
                for x in xl:
                    if x != "" and x != "def" and "(" not in x:
                        vars.append(x)
                vars = ",".join(vars)
                vars = vars[:-2]
                s = f"{xl[0]} {xl[1]}{vars}):" 
            else:
                vars = []
                for x in xl:
                    if x != "" and x != "def":
                        vars.append(x)
                vars = ",".join(vars)
                vars = vars[:-2]
                s = f"{xl[0]} {vars}):" 
   
            return s
        elif "()" in str(xl[1]):
            return f"def {xl[1]}:"
        
    except IndexError:
        pass
        

def indentation_():
    global pcc
    global cr
    remove_ = []
    for i in range(len(cr)):
        if "TYPE" in cr[i]:
            for x in range(i, len(cr)):
                remove_.append(cr[x])
                if "ENDTYPE" in cr[x] or "END TYPE" in cr[x]: break
            break
    for x in remove_:
        cr.remove(x) 
    for i in range(len(pcc)):
        count = 0
        string = cr[i]
        for j in range(len(string)):
            char = string[j]
            if char == "\t":
                count += 4 
            elif char == " ":
                count += 1
            else:
                break
        pcc[i] = " " * count + pcc[i]


def exit(line):
    end_commands = ["STOP", "EXIT", "END"]
    if line in end_commands: return True 


def ending_process():
    print()
    print("ENDING_PROCESS")
    print()


def input_line():
    global line_counter
    x = input(f"{line_counter}: ")
    return x


def pcc_append(x):
    if x != "":
        output = converter(x)
        if output != None:
            pcc.append(output)


def line_increment():
    global line_counter
    line_counter += 1


def cr_append(x):
    global cr
    cr.append(x)


def full_main_func():
    while True:
        x = input_line()
        if exit(x): 
            ending_process()
            break
        pcc_append(x)
        cr_append(x)
        line_increment()


def converting_():
    import random
    import time
    import sys
    import os
    if len(pcc) != 0:
        # silly little animation - I was bored
        at = ["|", '\\', "-", "/", "\\", "|"]
        percentage = random.randint(0, 30)
        for _ in range(1):
            for x in at:
                percentage += 10 
                s = x*50 + f" Converting {percentage}% " + x*50
                sys.stdout.write('\r' + s)
                sys.stdout.flush()
                time.sleep(.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    print()


def final_ending_process():
    global ef
    global pcc
    if classes != "":
        print()
        for x in classes:
            print(x)
        print()
    if ef != "":
        print()
        for x in ef:
            print(x)
        print()
        print()
    if pcc != "":
        for x in pcc:
            print(x)
        print()

    input("\n"+"Press Enter To Continue")


def reset_():
    global pcc, cr, ef, classes, line_counter, flag_list
    x = "a"
    while x != 'y' or x != 'n':
        x = input("Would you like to go again? y or n: ")
    if x == 'n':
        print('\n' + 'Okay, program ending...')
        return False
    else:
        pcc, cr, ef, classes = [[] for _ in range(4)]
        line_counter = 0
        flag_list = [False for _ in range(21)]
        return True
    

def main():
    while True:
        print('\n' + "Enter 'END' to convert.")
        global ef    
        full_main_func()
        converting_()
        indentation_()
        final_ending_process()
        if not reset_(): break


main()