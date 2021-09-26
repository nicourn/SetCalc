import types
import string

def add(a: list, b: list):  # 2
    return list(set(a + b))
def crossing(a: list, b: list):  # 3
    return [x for x in a + b if x in a and x in b]
def minus(a: list, b: list):  # 3
    return [x for x in a if x not in b]
def anti(a: list):  # 1
    return [x for x in u if x not in a]
def str_set(args: str):
    if len(args) == 1:
        return str(global_sets[args])

procedures_order: list[dict[str, list[int, types.FunctionType]]] = [
    {'~':[1, anti]}, {'+':[2, add]}, {'+-': [2, crossing], '-': [2, minus]}]
functions: dict[str, types.FunctionType] = {"print": str_set}

global_sets: dict[str, list[str]] = {
    "u": []
}

template_variables: list[list[str]] = []

def brace_handline(line: str):
    local_step = ""
    add_to_step = False
    while "(" in line:
        for c in line:
            if c == "(":
                add_to_step = True
                local_step = ""
            elif c == ")" and add_to_step:
                add_to_step = False
                line = line.replace("(" + local_step + ")", str(len(template_variables)))
                template_variables.append(local_step)
            elif add_to_step:
                local_step += c
            
        print(line)

def get_set(var_name: str):
    if var_name in global_sets.keys():
        return global_sets[var_name]
    try: 
        if len(template_variables) > int(var_name):
            return template_variables(int(var_name))
        else:
            raise ""
    except:
        print("sets not found")
        return []

def procedure_handline():
    template_calculation = []
    for variable in template_variables:
        for c in range(len(variable)):
            for order in procedures_order:
                if variable[c] in order.keys():
                    result = []
                    if (order[variable[c]])[0] == 1:
                        result = order[variable[c]][1](get_set(variable[c+1]))
                    elif order[variable[c]][0] == 1:
                        result = order[variable[c]][1](get_set(variable[c-1], get_set(variable[c+1])))
                    variable = line.replace(variable[c-1:c+2], str(len(global_sets)))
                    global_sets[str(len(global_sets))] = result
    print(global_sets)

def do_procedure(line: str):
    """Ввод строки с двумя множествами и действием между ними"""
    for order in procedures_order:
        for procedure in order.keys():
            if procedure in line:
                a = global_sets[line[0]]
                b = global_sets[line[2]]
                order[procedure](a, b)

def line_handler(line: str) -> list[str]:
    local_step = ""
    r = []
    doings = []
    for i in procedures_order[1:]:
        doings += i.keys()
    vars = line
    does = line
    for i in doings:
        vars = vars.replace(i, " ")
    for i in (string.ascii_lowercase + "~"):
        print(i)
        does = does.replace(i, " ")
    print(vars.split(" "))
    d = does.split(" ")
    d.remove("")
    print(d)

        

def get_data(line) -> str:
    if "=" in line:
        data = list(map(lambda x: x.strip(), line.split("=")))
        global_sets[data[0]] = data[1].split(" ")
        return f"Set {data[0]} init"
    for fn in functions.keys():
        if fn in line:
            args = line.replace(fn, "").strip()
            return functions[fn](args)
    line = "(" + line.replace(" ", "") + ")"
    brace_handline(line)
    for i in template_variables:
        line_handler(i)

    procedure_handline()


print("Hello from SetCalc")
print("Please enter a universal set for example \"1 2 3 4 5\"")

global_sets["u"] = input(">>> ").strip().split(" ")
if len(global_sets["u"]) == 0:
    global_sets["u"] = list([str(x) for x in range(21)])

while True:
    print(get_data(input(">>> ").strip()))
