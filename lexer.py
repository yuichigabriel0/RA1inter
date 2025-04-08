#1- É um dicionário que mapeia símbolos de lógica para os nomes dos tipos de token: "\\neg" → negação (unário). "\\wedge" → ∧ (binário). "true" / "false" → constantes. Parênteses também são reconhecidos.

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

#2- Verifica se c é uma letra minúscula (entre 'a' e 'z').
def eh_letra_minuscula(c):
    return 'a' <= c <= 'z'
#3- Verifica se c é um dígito (0 a 9).
def eh_digito(c):
    return '0' <= c <= '9'
#4- Essa é a principal. Ela recebe uma string da expressão lógica e retorna uma lista de tokens.  tokens guarda os tokens que serão encontrados. i é o índice do caractere atual. n é o tamanho total da string.
def lexer(expr):
    tokens = []
    i = 0
    n = len(expr)
#5- Percorre a expressão caractere por caractere.
    while i < n:
        c = expr[i]

#6- Ignora espaços
        if c == ' ':
            i += 1
            continue

#7- Parênteses simples
        if c == '(':
            tokens.append(("ABREPAREN", '('))
            i += 1
            continue
        elif c == ')':
            tokens.append(("FECHAPAREN", ')'))
            i += 1
            continue

        # Constantes ou operadores
#8- Quando vê uma barra (\), começa a ler um operador. Junta tudo até formar algo como \neg, \vee, etc. Se for válido, adiciona como token. Se não for reconhecido, retorna None (expressão inválida).
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
#9- Verifica se a parte da string é true ou false e adiciona como constante.
        if expr[i:i+4] == 'true':
            tokens.append(("CONSTANTE", "true"))
            i += 4
            continue
        if expr[i:i+5] == 'false':
            tokens.append(("CONSTANTE", "false"))
            i += 5
            continue

        # Proposição
#10- Começa com número (1, 2, etc), depois pode vir letras minúsculas. Exemplo: 1a, 2z, 3p → vira token de tipo PROPOSICAO.
        if eh_digito(c):
            inicio = i
            i += 1
            while i < n and (eh_digito(expr[i]) or eh_letra_minuscula(expr[i])):
                i += 1
            valor = expr[inicio:i]
            tokens.append(("PROPOSICAO", valor))
            continue

        # Qualquer coisa fora disso é inválida
#11- Se não se encaixa em nenhum dos casos, a expressão tem erro léxico → retorna None.
        return None
#12- Se tudo deu certo, retorna a lista de tokens.
    return tokens
