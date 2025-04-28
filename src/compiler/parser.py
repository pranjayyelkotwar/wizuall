import ply.yacc as yacc
from collections import defaultdict
from .lexer import tokens, lexer

precedence = (
    ('right', 'UMINUS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULT', 'DIV'),
)

symbol_table = defaultdict(list)
auxiliary_code_blocks = []

VISUALIZATION_PRIMITIVES = {'histogram', 'scatter', 'plot', 'reverse', 'slice', 'cluster'}

def indent_block(code_list):
    if not code_list:
        return ["    pass"]
    indented = []
    for item in code_list:
        if isinstance(item, str):
            indented.extend(["    " + line for line in item.splitlines()])
        elif isinstance(item, list):
            indented.extend(indent_block(item))
    return indented if indented else ["    pass"]

def p_program(p):
    '''program : statement_list'''
    p[0] = [line for item in p[1] for line in item if item is not None]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment
                 | conditional
                 | while_loop
                 | function_call
                 | auxiliary
                 | expression'''
    p[0] = p[1] if isinstance(p[1], list) else [p[1]] if isinstance(p[1], str) else []

def p_assignment(p):
    'assignment : ID EQ expression'
    p[0] = [f"{p[1]} = {p[3]}"]
    symbol_table[p[1]] = None

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = f"np.add({p[1]}, {p[3]})"
    else:
        p[0] = f"np.subtract({p[1]}, {p[3]})"

def p_term(p):
    '''term : term MULT factor
            | term DIV factor
            | factor'''
    if len(p) == 4:
        p[0] = f"np.multiply({p[1]}, {p[3]})" if p[2] == '*' else f"np.divide({p[1]}, {p[3]})"
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUM
              | ID
              | LPAREN expression RPAREN
              | MINUS factor %prec UMINUS
              | LBRACKET list_elements RBRACKET'''
    if len(p) == 2:
        p[0] = str(p[1]) if isinstance(p[1], (int, float)) else p[1]
    elif len(p) == 4:
        if p[1] == '[':
            p[0] = f"[{', '.join(map(str, p[2]))}]"
        else:
            p[0] = f"({p[2]})"
    elif len(p) == 3:
        p[0] = f"np.negative({p[2]})"

def p_list_elements(p):
    '''list_elements : list_elements COMMA expression
                     | expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_conditional(p):
    '''conditional : IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                   | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE'''
    condition = p[3]
    if_body_lines = indent_block(p[6])
    if_body = "\n".join(if_body_lines)
    if len(p) > 8:
        else_body_lines = indent_block(p[10])
        else_body = "\n".join(else_body_lines)
        p[0] = [f"if {condition}:\n{if_body}\nelse:\n{else_body}"]
    else:
        p[0] = [f"if {condition}:\n{if_body}"]

def p_while_loop(p):
    'while_loop : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'
    condition = p[3]
    loop_body_lines = indent_block(p[6])
    loop_body = "\n".join(loop_body_lines)
    p[0] = [f"while {condition}:\n{loop_body}"]

def p_function_call(p):
    '''function_call : ID LPAREN arg_list_opt RPAREN'''
    func_name = p[1]
    args = p[3]
    result = []
    args_str = ", ".join(map(str, args))
    
    if func_name in VISUALIZATION_PRIMITIVES:
        if func_name == 'histogram' and len(args) >= 1:
            data_arg = args[0]
            bins_arg = args[1] if len(args) > 1 else '10'
            result.append(f"data = {data_arg} if isinstance({data_arg}, (list, np.ndarray)) else [{data_arg}]")
            result.append("plt.figure()")
            result.append(f"plt.hist(data, bins=int({bins_arg}))")
            result.append(f"plt.title('Histogram')")
            result.append(f"plt.xlabel('Value')")
            result.append(f"plt.ylabel('Frequency')")
            result.append(f"plt.savefig(os.path.join(OUTPUT_DIR, 'histogram.png'))")
            result.append("plt.close()")
        elif func_name == 'scatter' and len(args) == 2:
            x_arg, y_arg = args[0], args[1]
            result.append(f"x_data = {x_arg} if isinstance({x_arg}, (list, np.ndarray)) else [{x_arg}]")
            result.append(f"y_data = {y_arg} if isinstance({y_arg}, (list, np.ndarray)) else [{y_arg}]")
            result.append("plt.figure()")
            result.append(f"plt.scatter(x_data, y_data)")
            result.append(f"plt.title('Scatter Plot')")
            result.append(f"plt.xlabel('X')")
            result.append(f"plt.ylabel('Y')")
            result.append(f"plt.savefig(os.path.join(OUTPUT_DIR, 'scatter.png'))")
            result.append("plt.close()")
        elif func_name == 'plot' and len(args) == 2:
            x_arg, y_arg = args[0], args[1]
            result.append(f"x_data = {x_arg} if isinstance({x_arg}, (list, np.ndarray)) else [{x_arg}]")
            result.append(f"y_data = {y_arg} if isinstance({y_arg}, (list, np.ndarray)) else [{y_arg}]")
            result.append("plt.figure()")
            result.append(f"plt.plot(x_data, y_data)")
            result.append(f"plt.title('Line Plot')")
            result.append(f"plt.xlabel('X')")
            result.append(f"plt.ylabel('Y')")
            result.append(f"plt.savefig(os.path.join(OUTPUT_DIR, 'plot.png'))")
            result.append("plt.close()")
        elif func_name == 'reverse' and len(args) == 1:
            data_arg = args[0]
            result.append(f"data = {data_arg} if isinstance({data_arg}, (list, np.ndarray)) else [{data_arg}]")
            result.append(f"reversed_data = data[::-1]")
            result.append(f"print('Reversed:', reversed_data)")
        elif func_name == 'slice' and len(args) >= 2:
            data_arg = args[0]
            start = args[1] if len(args) > 1 else '0'
            end = args[2] if len(args) > 2 else 'len(data)'
            result.append(f"data = {data_arg} if isinstance({data_arg}, (list, np.ndarray)) else [{data_arg}]")
            result.append(f"sliced_data = data[int({start}):int({end})]")
            result.append(f"print('Sliced:', sliced_data)")
        elif func_name == 'cluster' and len(args) == 1:
            data_arg = args[0]
            result.append(f"data = {data_arg} if isinstance({data_arg}, (list, np.ndarray)) else [{data_arg}]")
            result.append("from sklearn.cluster import KMeans")
            result.append("kmeans = KMeans(n_clusters=2, random_state=0).fit(np.array(data).reshape(-1, 1))")
            result.append("labels = kmeans.labels_")
            result.append(f"print('Cluster Labels:', labels)")
        else:
            result.append(f"{func_name}({args_str})")
    elif func_name in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
        result.append(f"np.{func_name}({args_str})")
    else:
        result.append(f"{func_name}({args_str})")
    
    p[0] = result

def p_arg_list_opt(p):
    '''arg_list_opt : arg_list
                    | empty'''
    p[0] = p[1] if p[1] else []

def p_arg_list(p):
    '''arg_list : expression
                | expression COMMA arg_list'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_empty(p):
    'empty :'
    p[0] = []

def p_auxiliary(p):
    'auxiliary : AUX_START aux_code AUX_END'
    aux_code_content = ''.join(p.lexer.aux_code) if hasattr(p.lexer, 'aux_code') else ''
    if aux_code_content:
        auxiliary_code_blocks.append(aux_code_content)
    p[0] = None

def p_aux_code(p):
    '''aux_code : empty'''
    p[0] = []

def p_error(p):
    if p:
        print(f"Syntax error at token '{p.type}' with value '{p.value}' near line {p.lineno}")
    else:
        print("Syntax error at EOF")
    raise SyntaxError("WizUALL syntax error")

parser = yacc.yacc()