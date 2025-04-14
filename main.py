#GABRIEL YUICHI SUZAKI
#MARIA JULIA PRADO LAZAROTO
from lexer import lexer
from parser import Parser
import sys

def ler_entrada(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            linhas = [linha.strip() for linha in f if linha.strip()]
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        return None, None

    try:
        quantidade = int(linhas[0])
        expressoes = linhas[1:]
    except (ValueError, IndexError):
        print("Formato de entrada inválido.")
        return None, None

    if len(expressoes) != quantidade:
        print("Quantidade de expressões não corresponde ao valor informado.")
        return None, None

    return quantidade, expressoes


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo_entrada>")
        return

    caminho_arquivo = sys.argv[1]
    _, expressoes = ler_entrada(caminho_arquivo)

    if expressoes is None:
        return

    for expressao in expressoes:
        tokens = lexer(expressao)
        if tokens is None:
            print("inválida")
            continue

        parser = Parser(tokens)
        if parser.parse():
            print("valida")
        else:
            print("inválida")

if __name__ == "__main__":
    main()
