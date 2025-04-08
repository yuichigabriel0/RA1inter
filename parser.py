#1- Define um analisador sintático (parser), que vai verificar se os tokens de uma fórmula lógica estão corretos.

#2- tokens: é a lista de pedaços da fórmula (como palavras). self.pos: é onde o parser está lendo dentro dessa lista, começando do início.
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        
#3- Verifica se o token atual é do tipo esperado (por exemplo, "PROPOSICAO"). Se for, avança para o próximo token. Se não for, retorna False.
    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == tipo_esperado:
            self.pos += 1
            return True
        return False
        
#4- Retorna o token atual que o parser está olhando. Se já estiver no fim da lista, retorna None.
    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

#5- Tenta analisar a fórmula completa com self.formula(). Se der certo, verifica se todos os tokens foram usados (nenhum token sobrando). Retorna True se a fórmula é válida, False caso contrário.
    def parse(self):
        if self.formula():
            return self.pos == len(self.tokens)  # sucesso apenas se todos tokens foram consumidos
        return False

#6- Pega o token atual. Se não tiver mais tokens, a fórmula está incompleta → False.
    def formula(self):
        atual = self.token_atual()
        if atual is None:
            return False

#7- Se for uma constante (⊤, ⊥), avança e retorna True.
        tipo, valor = atual
        # CONSTANTE
        if tipo == "CONSTANTE":
            self.pos += 1
            return True

        # PROPOSICAO
#8- Se for uma letra proposicional (tipo P, Q, etc), também aceita.
        if tipo == "PROPOSICAO":
            self.pos += 1
            return True

        # FORMULAUNARIA → ( \neg FORMULA )
#9-  Começou com parêntese? Pode ser uma fórmula complexa: Pode ser uma unária: (¬ F). Ou binária: (& F1 F2).
        if tipo == "ABREPAREN":
            self.pos += 1  # consome '('
#10- Verifica se depois de ( vem um operador unário (como ¬). Depois espera uma fórmula dentro. E então fecha com ).
            if self.consumir("OP_UNARIO"):
                if self.formula() and self.consumir("FECHAPAREN"):
                    return True
                return False
#11- Verifica se depois de ( vem um operador binário (como ∧, ∨, →). Depois espera duas fórmulas. E então fecha com ).
            # FORMULABINARIA → ( OP_BINARIO FORMULA FORMULA )
            if self.consumir("OP_BINARIO"):
                if self.formula() and self.formula() and self.consumir("FECHAPAREN"):
                    return True
                return False
#12- A estrutura está errada e a fórmula não é válida.
        return False
