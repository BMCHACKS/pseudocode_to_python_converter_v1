<html>
  <py-script>
    # global vars
    pcc, cr, ef, classes = [[] for _ in range(4)]
    line_counter = 0
    flag_list = [False for _ in range(21)]
    file_data = [False, ""]
  
    def read_from_file_checker():
        global file_data
        x = input("Do you want to enter manually or read code from file? (y or n): ")
        while x != 'y' and x != 'n':
            x = input("Please enter 'y' for reading from file or 'n' for manual input: ")
        if x == 'n':
            file_data.append(False)
            print("\n -- Taking Input Manually -- \n")
        else:
            a = False
            while not a:
                file_name = input("Enter the name of the file (include .txt at the end): ")
                try:
                    file = open(file_name)
                    file_data[0] = True
                    file_data[1] = file_name
                    a = True
                except FileNotFoundError:
                    print("File does not exist or file name is wrong. Please try again.")
  
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
        dtd = [":", "DECLARE", "REAL", "BOOLEAN", "INTEGER", "STRING", "CHAR"]
        for p in range(len(pcc)):
            if "class" in pcc[p]: 
                break
        for c in range(len(cr)):
            if "TYPE" in cr[c]: 
                break 
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
        classes.append(f"{s}):")
        for x in to_add:
            classes.append(f"       self.{x} = {x}")
  
    def case_of_fixer():
        global pcc
  
        for p in range(len(pcc)):
            if "match" in pcc[p]: break
        for c in range(len(cr)):
            if "CASE OF" in cr[c]: break     
        to_remove = len(pcc) - p
        for _ in range(to_remove-1): pcc.pop()
        for i in range(c+1, len(cr)):
            if "OTHERWISE" in cr[i]:
                pcc.append("case _:")
                pcc.append(f"{converter(cr[-1])}")
            elif "OTHERWISE" not in cr[i-1]:
                s = [str(x) for x in cr[i].split()]
                pcc.append(f"case {s[0]}:")
                s.remove(s[0])
                s.remove(s[0])
                pcc.append(converter(" ".join(s)))
  
    def converter(x):
        # symbols for maths
        artimatic_symbols = ['*', '+', '-', '/']
        s = [str(i) for i in x.split()]
        # length of the list we will loop through
        s_length = len(s)
        # for finding single line comments
        try:
            comment_index = s.index("//")
        except ValueError:
            comment_index = -1
        try:
            # we check if there is a single line comment - done
            if comment_index != -1:
                x = " ".join(s[:comment_index])
                return x
            # bool symbols - done
            s = boolean_fixer(s)
            # checking to see if there are multiple line comments - done
            if s[0] == "/*":
                pcc.append(x)
                return "flag = False"
            # declaring vars - done
            if "DECLARE" in s:
                return "flag = True"
            # TYPE handling - done
            if s[0] == "TYPE":
                return "class " + s[1] + ":"
            if "ARRAY" in s:
                x = x.split("OF")
                y = [str(a) for a in x[0].split()]
                if y[2] == 'INTEGER':
                    pcc.append(f"{y[1]} = [0 for _ in range({x[1].strip()})]")
                elif y[2] == 'STRING':
                    pcc.append(f'{y[1]} = ["" for _ in range({x[1].strip()})]')
                elif y[2] == 'REAL':
                    pcc.append(f"{y[1]} = [0.0 for _ in range({x[1].strip()})]")
                elif y[2] == 'CHAR':
                    pcc.append(f'{y[1]} = ["" for _ in range({x[1].strip()})]')
                elif y[2] == 'BOOLEAN':
                    pcc.append(f"{y[1]} = [False for _ in range({x[1].strip()})]")
                return
            # math - done
            if any(i in s for i in artimatic_symbols):
                return other_functions_1(s)
            if len(s) == 1:
                return s[0]
            # pointer to record
            if s[1] == "^":
                s[1] = ""
                s[2] = "." + s[2]
                return "".join(s)
            # handling loops
            if s[0] == "WHILE":
                s = " ".join(s)
                s = s.replace("DO", ":")
                return s
            if s[0] == "ENDWHILE":
                return "flag = False"
            if s[0] == "FOR":
                s = " ".join(s)
                s = s.replace("TO", "in range(")
                s = s.replace("DO", ":")
                s = s + ")"
                return s
            if s[0] == "ENDFOR":
                return "flag = False"
            # handling if
            if s[0] == "if" or s[0] == "else":
                s = " ".join(s)
                s = s.replace("THEN", ":")
                return s
            if s[0] == "endif":
                return "flag = False"
            # handling records
            if "." in s[0]:
                s[0] = s[0].replace(".", "['") + "']"
                s = " ".join(s)
                s = s.replace("=", ":")
                s = s + "}"
                return s
            if s[0] == "READ":
                return f"{s[1]} = input({s[1]})"
            if s[0] == "OUTPUT":
                return f"print({s[1]})"
            if "CASE" in s and "OF" in s:
                return "match " + s[1] + ":"
            return " ".join(s)
        except Exception as e:
            return str(e)
        return x
  
    def main():
        global pcc, cr, ef, classes, line_counter, flag_list
        read_from_file_checker()
        if file_data[0]:
            with open(file_data[1], "r") as file:
                for x in file:
                    cr.append(x)
        else:
            # manually taking input line by line
            while True:
                x = input("Enter Line: ")
                cr.append(x)
                if x == "":
                    break
  
        for x in cr:
            s = converter(x)
            if type(s) == list:
                pcc.append(s)
                flag_list[line_counter] = True
            else:
                pcc.append(s)
            line_counter += 1
  
        class_fixer()
        case_of_fixer()
  
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  
        print("Extra Functions - ", end=" ")
        print(ef, end=" ")
        print("\n")
        print("Classes - ", end=" ")
        print(classes, end=" ")
        print("\n")
        print("Code - ", end=" ")
        print(pcc, end=" ")
        print("\n")
  
        print("Code")
        for x in ef:
            print(x)
        for x in classes:
            print(x)
        for x in pcc:
            print(x)
  
    main()
  </py-script>
</html>
