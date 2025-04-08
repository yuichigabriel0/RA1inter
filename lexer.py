TOKENS_ESPECIAIS = {
    '(': "ABREPAREN",
    ')': "FECHAPAREN",
    "\\neg": "OP_UNARIO",
    "\\wedge": "OP_BINARIO",
    "\\vee": "OP_BINARIO",
    "\\rightarrow": "OP_BINARIO",
    "\\leftrightarrow": "OP_BINARIO",
    "true": "CONSTANTE",
    "false": "CONSTANTE"
}

def eh_letra_minuscula(c):
    return 'a' <= c <= 'z'

def eh_digito(c):
    return '0' <= c <= '9'

def lexer(expr):
    tokens = []
    i = 0
    n = len(expr)

    while i < n:
        c = expr[i]

        # Ignora espaços
        if c == ' ':
            i += 1
            continue

        # Parênteses simples
        if c == '(':
            tokens.append(("ABREPAREN", '('))
            i += 1
            continue
        elif c == ')':
            tokens.append(("FECHAPAREN", ')'))
            i += 1
            continue

        # Constantes ou operadores
        if expr[i] == '\\':  # operadores LaTeX sempre começam com '\'
            inicio = i
            while i < n and (eh_letra_minuscula(expr[i]) or expr[i] == '\\'):
                i += 1
            valor = expr[inicio:i]
            if valor in TOKENS_ESPECIAIS:
                tokens.append((TOKENS_ESPECIAIS[valor], valor))
            else:
                return None  # operador inválido
            continue

        # Constantes true ou false
        if expr[i:i+4] == 'true':
            tokens.append(("CONSTANTE", "true"))
            i += 4
            continue
        if expr[i:i+5] == 'false':
            tokens.append(("CONSTANTE", "false"))
            i += 5
            continue

        # Proposição
        if eh_digito(c):
            inicio = i
            i += 1
            while i < n and (eh_digito(expr[i]) or eh_letra_minuscula(expr[i])):
                i += 1
            valor = expr[inicio:i]
            tokens.append(("PROPOSICAO", valor))
            continue

        # Qualquer coisa fora disso é inválida
        return None

    return tokens
