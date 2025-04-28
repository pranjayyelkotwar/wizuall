import ply.lex as lex

states = (
    ('auxcode', 'exclusive'),
)

tokens = (
    'ID', 'NUM', 'PLUS', 'MINUS', 'MULT', 'DIV', 'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET', 'EQ', 'IF', 'ELSE', 'WHILE', 'LBRACE', 'RBRACE', 'COMMA',
    'AUX_START', 'AUX_END'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_EQ = r'='
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUM(t):
    r'-?\d+(\.\d*)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print(f"Error converting number: {t.value}")
        t.value = 0.0
    return t

def t_AUX_START(t):
    r',\*'
    t.lexer.begin('auxcode')
    t.lexer.aux_code = []
    return t

def t_auxcode_AUX_END(t):
    r',\*'
    t.lexer.begin('INITIAL')
    return t

def t_auxcode_content(t):
    r'([^,]|,(?!\*))+'
    t.lexer.aux_code.append(t.value)
    return None

def t_auxcode_newline(t):
    r'\n+'
    t.lexer.aux_code.append(t.value)
    t.lexer.lineno += len(t.value)
    return None

t_ignore = ' \t'
t_auxcode_ignore = ''

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

def t_auxcode_error(t):
    t.lexer.skip(1)

lexer = lex.lex()
lexer.aux_code = []