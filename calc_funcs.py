stripzero = lambda x: (x).rstrip('0').rstrip('.')
striptuple = lambda x: (x).replace(",", "").replace("(", "").replace(")", "").replace("'", "")

def charposition(string, char):
    pos = []
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos

def auto(x): 
    symbols = ("+", "*", "/", "%")
    while x[0] in symbols:
        x = x[1:]
    z = x[-1]
    symbols = ("+", "*", "/", "-", "%")
    while x[-1] in symbols:
        x = x[:-1]
    while x[-1].isdigit == False:
        x = x[:1]
    if x.count("-") > 3 and x[0] == "-":
        while x[1] == "-":
            x = x[1:]       
    elif x.count("+") == 1:
        plus_position = charposition(x, "+")
        first_plus_position = plus_position[0]
        last_plus_position = plus_position[-1]
        part0 = x[0:first_plus_position]
        after_middle = last_plus_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'+ {part1}'),stripzero(f'= {part0 + part1}'))
    elif x.count("*") == 1:
        plus_position = charposition(x, "*")
        first_plus_position = plus_position[0]
        last_plus_position = plus_position[-1]
        part0 = x[0:first_plus_position]
        after_middle = last_plus_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'* {part1}'),stripzero(f'= {part0 * part1}'))    
    elif x.count("*") == 2:
        plus_position = charposition(x, "*")
        first_plus_position = plus_position[0]
        last_plus_position = plus_position[-1]
        part0 = x[0:first_plus_position]
        after_middle = last_plus_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'** {part1}'),stripzero(f'= {part0 ** part1}'))
    elif x.count("/") == 2 and "-" in x:
        div_position = charposition(x, "/")
        first_div_position = div_position[0]
        second_position = div_position[-1]
        part0 = x[0:first_div_position]
        after_middle = second_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'// {part1}'),stripzero(f'= {part0 // part1}'))
    elif x.count("-") == 1 and x.count("/") == 1:
            part = x.split("/")
            part[0] = float(part[0])
            part[1] = float(part[1])
            return (stripzero(f'{part[0]}'),stripzero(f'/ {part[1]}'),stripzero(f'= {part[0] / part[1]}'))   
    elif x.count("%") == 1:
        part = x.split("%")
        part[0] = float(part[0])
        part[1] = float(part[1])
        return (stripzero(f'{part[0]}'),stripzero(f'% {part[1]}'),stripzero(f'= {part[0] % part[1]}')) 
    elif x.count("-") <= 2 and x.count("%") == 1:
        part = x.split("%")
        part[0] = float(part[0])
        part[1] = float(part[1])
        return (stripzero(f'{part[0]}'),stripzero(f'% {part[1]}'),stripzero(f'= {part[0] % part[1]}')) 
    elif x.count("-") == 1:
            part = x.split("-")
            part[0] = float(part[0])
            part[1] = float(part[1])
            return (stripzero(f'{part[0]}'),stripzero(f'- {part[1]}'),stripzero(f'= {part[0] - part[1]}'))
    elif x.count("-") == 2 and "/" in x:
            part = x.split("/")
            part[0] = float(part[0])
            part[1] = float(part[1])
            return (stripzero(f'{part[0]}'),stripzero(f'/ {part[1]}'),stripzero(f'= {part[0] / part[1]}'))
    elif x.count("-") == 2:
        if x[0] == "-":
            minus_position = charposition(x, "-")
            second_minus_position = minus_position[1]
            part0 = x[0:second_minus_position]
            after_middle = second_minus_position + 1
            part1 = x[after_middle:]
            part0 = float(part0)
            part1 = float(part1)
            return (stripzero(f'{part0}'),stripzero(f'- {part1}'),stripzero(f'= {part0 - part1}'))
        elif x[0].isdigit():
            minus_position = charposition(x, "-")
            first_minus_position = minus_position[0]
            part0 = x[0:first_minus_position]
            after_middle = first_minus_position + 1
            part1 = x[after_middle:]
            part0 = float(part0)
            part1 = float(part1)
            return (stripzero(f'{part0}'),stripzero(f'- {part1}'),stripzero(f'= {part0 - part1}'))
    elif x.count("-") == 3 and (charposition(x, "-")[2]-charposition(x, "-")[1]) == 1:
            minus_position = charposition(x, "-")
            middle_minus_position = minus_position[1]
            part0 = x[0:middle_minus_position]
            after_middle = middle_minus_position + 1
            part1 = x[after_middle:]
            part0 = float(part0)
            part1 = float(part1)
            return (stripzero(f'{part0}'),stripzero(f'- {part1}'),stripzero(f'= {part0 - part1}'))
    elif x.count("/") == 1:
        div_position = charposition(x, "/")
        first_div_position = div_position[0]
        last_div_position = div_position[-1]
        part0 = x[0:first_div_position]
        after_middle = last_div_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'/ {part1}'),stripzero(f'= {part0 / part1}'))
    elif x.count("/") == 2 and "-" in x:
        div_position = charposition(x, "/")
        first_div_position = div_position[0]
        second_position = div_position[-1]
        part0 = x[0:first_div_position]
        after_middle = second_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'// {part1}'),stripzero(f'= {part0 // part1}'))
    elif x.count("/") == 2:
        div_position = charposition(x, "/")
        first_div_position = div_position[0]
        last_div_position = div_position[-1]
        part0 = x[0:first_div_position]
        after_middle = last_div_position + 1
        part1 = x[after_middle:]
        part0 = float(part0)
        part1 = float(part1)
        return (stripzero(f'{part0}'),stripzero(f'// {part1}'),stripzero(f'= {part0 // part1}'))
    elif x[0] != ("-"):
        return(x)
    else:
        return x
   
