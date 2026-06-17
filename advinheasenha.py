"""
Jogo: Adivinhação de Senha 0/100
Autor: Gabriel Duarte

Como executar:
    python advinheasenha.py

Requisito:
    pandas
"""

from pathlib import Path
import random
import time

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_HISTORIA = BASE_DIR / "message.txt"

VALOR_MINIMO = 0
VALOR_MAXIMO = 100


def carregar_historia(caminho: Path = ARQUIVO_HISTORIA) -> list[str]:
    """Carrega o arquivo message.txt usando pandas.read_table."""
    try:
        df = pd.read_table(caminho, header=None, names=["linha"], encoding="utf-8")
        linhas = df["linha"].fillna("").astype(str).tolist()

        if not linhas:
            print("\n[ERRO] O arquivo message.txt está vazio.")
            print("Preencha o arquivo com a história do jogo e tente novamente.\n")
            raise SystemExit(1)

        return linhas

    except FileNotFoundError:
        print(f"\n[ERRO] O arquivo '{caminho.name}' não foi encontrado.")
        print("Coloque o message.txt na mesma pasta deste arquivo .py e tente novamente.\n")
        raise SystemExit(1)

    except Exception as erro:
        print(f"\n[ERRO] Não foi possível carregar o arquivo '{caminho.name}'.")
        print(f"Detalhes: {erro}\n")
        raise SystemExit(1)


def limpar_markdown(texto: str) -> str:
    """Remove marcações simples de Markdown para ficar mais limpo no terminal."""
    return (
        texto.replace("**", "")
        .replace("### ", "")
        .replace("## ", "")
        .replace("---", "")
        .replace("✅", "[VITORIA]")
        .replace("❌", "[DERROTA]")
    )


def digitar(texto: str, pausa: float = 0.0) -> None:
    """Imprime texto com pequena pausa opcional para dar clima de jogo."""
    print(texto)
    if pausa > 0:
        time.sleep(pausa)


def mostrar_bloco(linhas: list[str], inicio: str, fim: str | None = None) -> None:
    """Mostra uma parte específica do arquivo de história."""
    imprimindo = False

    for linha in linhas:
        if inicio in linha:
            imprimindo = True

        if imprimindo:
            linha_limpa = limpar_markdown(linha).strip()
            if linha_limpa:
                digitar(linha_limpa)

        if fim and imprimindo and fim in linha:
            break

    print()


def gerar_codigo_inteligente(fase: int) -> int:
    return random.randint(VALOR_MINIMO, VALOR_MAXIMO)


def analisar_temperatura(palpite: int, codigo: int) -> str:
    """Retorna uma dica de proximidade entre o palpite e o código."""
    distancia = abs(palpite - codigo)

    if distancia == 0:
        return "alvo exato"
    if distancia <= 3:
        return "fervendo"
    if distancia <= 8:
        return "muito quente"
    if distancia <= 15:
        return "quente"
    if distancia <= 25:
        return "morno"

    return "frio"


def dica_binaria(palpite: int, codigo: int, minimo: int, maximo: int) -> tuple[int, int, str]:
    """
    Aplica lógica de busca binária.
    Se o palpite for menor que o código, o limite mínimo sobe.
    Se o palpite for maior que o código, o limite máximo desce.
    """
    if palpite < codigo:
        minimo = max(minimo, palpite + 1)
        direcao = "O código é MAIOR."
    else:
        maximo = min(maximo, palpite - 1)
        direcao = "O código é MENOR."

    return minimo, maximo, direcao


def gerar_dica_extra(codigo: int, tentativa_atual: int, fase: int) -> str:
    """Libera pistas extras conforme a dificuldade e o número de tentativas."""
    dicas = []

    if tentativa_atual >= 2:
        dicas.append("O código é PAR." if codigo % 2 == 0 else "O código é ÍMPAR.")

    if fase >= 2 and tentativa_atual >= 3:
        if codigo % 5 == 0:
            dicas.append("O código é múltiplo de 5.")
        elif codigo % 3 == 0:
            dicas.append("O código é múltiplo de 3.")
        else:
            dicas.append("O código não é múltiplo de 3 nem de 5.")

    if fase == 3 and tentativa_atual >= 4:
        dezena = codigo // 10
        dicas.append(f"O código está na dezena dos {dezena * 10}.")

    return " ".join(dicas)


def estrategia_otima(minimo: int, maximo: int) -> str:
    """
    Sugere o próximo palpite pela estratégia ótima de busca binária.
    Exemplo: se o intervalo é 0 a 100, o melhor chute inicial é 50.
    """
    if minimo > maximo:
        return "Intervalo inconsistente. Revise os palpites."

    meio = (minimo + maximo) // 2
    possibilidades = maximo - minimo + 1
    return f"Estratégia da IA: teste algo perto de {meio}. Restam {possibilidades} possibilidades."


def ler_palpite() -> int:
    """Lê e valida o palpite do jogador."""
    while True:
        entrada = input("Digite um número de 0 a 100: ").strip()

        if not entrada.lstrip("-").isdigit():
            print("Entrada inválida. Digite apenas números inteiros.")
            continue

        palpite = int(entrada)

        if palpite < VALOR_MINIMO or palpite > VALOR_MAXIMO:
            print("O número precisa estar entre 0 e 100.")
            continue

        return palpite


def jogar_fase(
    numero_fase: int,
    titulo: str,
    codigo: int,
    tentativas_maximas: int,
    mensagem_vitoria: str,
    mensagem_derrota: str,
) -> bool:
    """Executa uma fase completa do jogo."""
    print("=" * 72)
    print(f"FASE {numero_fase} — {titulo}")
    print("=" * 72)
    print(f"Você precisa descobrir o código secreto entre {VALOR_MINIMO} e {VALOR_MAXIMO}.")
    print(f"Tentativas disponíveis: {tentativas_maximas}\n")

    minimo = VALOR_MINIMO
    maximo = VALOR_MAXIMO
    historico = []

    for tentativa in range(1, tentativas_maximas + 1):
        print(f"Tentativa {tentativa}/{tentativas_maximas}")
        print(estrategia_otima(minimo, maximo))

        palpite = ler_palpite()
        historico.append(palpite)

        if palpite == codigo:
            print(f"\n{mensagem_vitoria}")
            print(f"Código descoberto: {codigo}")
            print(f"Histórico de palpites: {historico}\n")
            return True

        minimo, maximo, direcao = dica_binaria(palpite, codigo, minimo, maximo)
        temperatura = analisar_temperatura(palpite, codigo)
        dica_extra = gerar_dica_extra(codigo, tentativa, numero_fase)

        print(f"\n{direcao}")
        print(f"Sinal térmico: {temperatura}.")
        print(f"Novo intervalo provável: [{minimo}, {maximo}]")

        if dica_extra:
            print(f"Pista criptográfica: {dica_extra}")

        tentativas_restantes = tentativas_maximas - tentativa
        print(f"Tentativas restantes: {tentativas_restantes}\n")

    print(mensagem_derrota)
    print(f"O código correto era: {codigo}\n")
    return False


def main() -> None:
    """Função principal do jogo."""
    linhas_historia = carregar_historia()
    texto_completo = "\n".join(linhas_historia)

    print("\n" + "#" * 72)
    print("AGENTE 062 — OPERAÇÃO KRONVIA")
    print("Jogo de adivinhação de senha com algoritmos inteligentes")
    print("#" * 72 + "\n")

    mostrar_bloco(linhas_historia, "Ano 2048", "impedir o lançamento dos mísseis.")

    input("Pressione ENTER para iniciar a missão...")

    codigos = {
        1: gerar_codigo_inteligente(1),
        2: gerar_codigo_inteligente(2),
        3: gerar_codigo_inteligente(3),
    }

    fases = [
        {
            "numero": 1,
            "titulo": "A Infiltração",
            "tentativas": 10,
            "vitoria": "Acesso autorizado. O primeiro firewall foi desativado.",
            "derrota": "Tentativas excedidas. Alarmes são ativados. Missão fracassada.",
        },
        {
            "numero": 2,
            "titulo": "O Centro de Comando",
            "tentativas": 7,
            "vitoria": "Autenticação comprometida. As comunicações inimigas foram interrompidas.",
            "derrota": "Invasor identificado. Equipes de segurança cercam o complexo.",
        },
        {
            "numero": 3,
            "titulo": "O Código Final",
            "tentativas": 5,
            "vitoria": "PROTOCOLO FINAL CANCELADO. VOCÊ SALVOU A MISSÃO!",
            "derrota": "O sistema KRONVIA concluiu a operação. Missão fracassada.",
        },
    ]

    for fase in fases:
        print()
        venceu = jogar_fase(
            numero_fase=fase["numero"],
            titulo=fase["titulo"],
            codigo=codigos[fase["numero"]],
            tentativas_maximas=fase["tentativas"],
            mensagem_vitoria=fase["vitoria"],
            mensagem_derrota=fase["derrota"],
        )

        if not venceu:
            print("FIM DE JOGO.")
            return

        if fase["numero"] < 3:
            input("Pressione ENTER para avançar para a próxima fase...")

    print("=" * 72)
    print("MISSÃO FINALIZADA COM SUCESSO")
    print("O Agente 062 retorna para casa como herói nacional.")
    print("=" * 72)


if __name__ == "__main__":
    main()