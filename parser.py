class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def consumir(self, tipo_esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == tipo_esperado:
            self.pos += 1
            return True
        return False

    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def parse(self):
        if self.formula():
            return self.pos == len(self.tokens)  # sucesso apenas se todos tokens foram consumidos
        return False

    def formula(self):
        atual = self.token_atual()
        if atual is None:
            return False

        tipo, valor = atual

        # CONSTANTE
        if tipo == "CONSTANTE":
            self.pos += 1
            return True

        # PROPOSICAO
        if tipo == "PROPOSICAO":
            self.pos += 1
            return True

        # FORMULAUNARIA → ( \neg FORMULA )
        if tipo == "ABREPAREN":
            self.pos += 1  # consome '('

            if self.consumir("OP_UNARIO"):
                if self.formula() and self.consumir("FECHAPAREN"):
                    return True
                return False

            # FORMULABINARIA → ( OP_BINARIO FORMULA FORMULA )
            if self.consumir("OP_BINARIO"):
                if self.formula() and self.formula() and self.consumir("FECHAPAREN"):
                    return True
                return False

        return False
