# 🕵️ Agente 062 — Jogo de Adivinha Senha

> *"O Brasil está nas suas mãos. Três códigos. Sem segunda chance."*

<div align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="52" alt="Python" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="52" alt="Pandas" />
  <img width="12" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="52" alt="Git" />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="52" alt="GitHub" />
</div>

<br>

<p align="center">
  <strong>Status:</strong> Em desenvolvimento &nbsp; | &nbsp;
  <strong>Licença:</strong> MIT
</p>

---

## 📖 História

**Ano 2048.**

O Brasil vive um dos momentos mais perigosos de sua história. Uma potência rival fictícia chamada **República de Kronvia** iniciou uma guerra tecnológica contra o país. Utilizando uma rede de satélites militares e silos nucleares automatizados, Kronvia ameaça destruir as principais cidades brasileiras.

As agências de inteligência descobriram que os sistemas de lançamento são protegidos por **três códigos secretos**. Se forem descobertos a tempo, o ataque será interrompido. Para essa missão impossível, foi escolhido o melhor agente da inteligência nacional: **Agente 062**.

Veterano de dezenas de operações secretas, 062 deixou sua família para trás em uma missão sem garantias de retorno. Sua tarefa: infiltrar-se no centro de comando inimigo, localizar os códigos nucleares e impedir o lançamento dos mísseis.

---

## 🎮 Fases do Jogo

### 🔴 Fase 1 — A Infiltração
O Agente 062 chega a uma base de comunicação militar nas montanhas. Lá está o **Primeiro Código de Acesso**, responsável por liberar os servidores internos do inimigo.

- ✅ **Vitória:** *"Acesso autorizado. O primeiro firewall foi desativado."*
- ❌ **Derrota:** *"Tentativas excedidas."* — Alarmes ativados. Missão fracassada.

### 🟠 Fase 2 — O Centro de Comando
Com as informações da Fase 1, 062 invade uma instalação subterrânea altamente protegida. Nesse local está o **Segundo Código Nuclear**.

- ✅ **Vitória:** *"Autenticação comprometida."* — Comunicações inimigas interrompidas.
- ❌ **Derrota:** *"Invasor identificado."* — A contagem regressiva começa.

### ☢️ Fase 3 — O Código do Apocalipse
O coração da operação inimiga: um bunker sob a capital de Kronvia. O último código é o **Código do Apocalipse**. A contagem regressiva já começou.

- ✅ **Vitória:** *"PROTOCOLO NUCLEAR CANCELADO."* — **VOCÊ SALVOU O BRASIL!** 🇧🇷
- ❌ **Derrota:** *"CONTAGEM REGRESSIVA CONCLUÍDA."* — **O BRASIL FOI DESTRUÍDO.**

---

## 🚀 Como Executar

### Pré-requisitos
- [Python 3.x](https://www.python.org/downloads/) instalado na máquina

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/SilvestreFernandes/jogo-de-adivinha-senha.git

# 2. Entre na pasta do projeto
cd jogo-de-adivinha-senha

# 3. Execute o jogo
python main.py
```

---

## 🕹️ Como Jogar

1. Ao iniciar, você será apresentado à história e à **Fase 1**
2. O sistema escolhe um código secreto (número)
3. Você tem **tentativas limitadas** para adivinhar
4. O jogo dá dicas a cada tentativa:
   - *"Muito alto"* / *"Muito baixo"* para números
5. Acertou? Avança para a próxima fase. Errou? A missão falha.

---

## 📁 Estrutura do Projeto

```
jogo-de-adivinha-senha/
│
├── main.py           # Arquivo principal — inicia o jogo
├── menu.py           # Menu de interação — interage com o usuário
├── fase1.py          # Lógica da Fase 1 — A Infiltração
├── fase2.py          # Lógica da Fase 2 — O Centro de Comando
├── fase3.py          # Lógica da Fase 3 — O Código do Apocalipse
├── README.md         # Documentação do projeto
└── LICENSE           # Licença MIT
```

---

## 👥 Equipe

| Integrante | Responsabilidade |
|---|---|
| [Silvestre Fernandes](https://github.com/SilvestreFernandes) | Organização do repositório e README |
| [Diego Azevedo](https://github.com/diegoliminha) | Função ainda não definida |
| [Filipe Amancio](https://github.com/filipe-amancio) | Criação da história e integração dela na interface do usuário |
| [Gabriel Duarte](https://github.com/gabriel-lab-ia) | Desenvolvimento do algoritmo |

---

## 📚 Conceitos Trabalhados

- Entrada e saída de dados (`input` / `print`)
- Condicionais (`if` / `elif` / `else`)
- Laços de repetição (`while`)
- Variáveis e strings
- Modularização com funções

---

## 📜 Licença

Este projeto está sob a licença [MIT](LICENSE).

---

<p align="center">
  Desenvolvido como atividade final de Lógica de Programação — CEUB 2026
</p>
