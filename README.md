# Guia prático de Git e GitHub

Material de apoio da aula **Versionamento de código: boas práticas e comandos do GitHub**.
Use este guia durante a atividade e depois, como referência rápida.

- Repositório da aula: <https://github.com/josepaes23/sudoku-game/>
- Códigop de da atividade: Sudoku-game
- Código da atividade: [`gerenciador_notas.py`](gerenciador_notas.py) (contém **bugs de propósito**)
- Verificador automático: [`test_gerenciador_notas.py`](test_gerenciador_notas.py)

---

## Sumário

1. [Conceitos em 1 minuto](#1-conceitos-em-1-minuto)
2. [Preparando o ambiente](#2-preparando-o-ambiente)
3. [A atividade: caçando bugs com Git](#3-a-atividade-caçando-bugs-com-git)
4. [Cheat sheet de comandos](#4-cheat-sheet-de-comandos)
5. [Resolvendo conflitos](#5-resolvendo-conflitos)
6. [Boas práticas](#6-boas-práticas)
7. [Problemas comuns e soluções](#7-problemas-comuns-e-soluções)
8. [Referências](#8-referências)

---

## 1. Conceitos em 1 minuto

| Termo | Significado |
|-------|-------------|
| **Repositório** | Pasta do projeto com todo o histórico de alterações (a pasta oculta `.git`). |
| **Commit** | Uma "foto" do projeto em um momento, com autor, data e mensagem. |
| **Branch** (ramo) | Linha independente de commits. Permite trabalhar sem mexer na `main`. |
| **Remoto (`origin`)** | Cópia do repositório hospedada no GitHub. |
| **Clone** | Copiar um repositório remoto para o seu computador. |
| **Fork** | Cópia do repositório de outra pessoa para a sua conta no GitHub. |
| **Pull Request (PR)** | Pedido para incorporar uma branch na `main`, com revisão e discussão. |
| **Issue** | Registro de uma tarefa, bug ou ideia. |
| **Merge** | Junção do histórico de duas branches. |

Os **três estados** de um arquivo no Git:

```
Diretório de trabalho  --git add-->  Área de preparação (staging)  --git commit-->  Repositório local  --git push-->  GitHub
```

---

## 2. Preparando o ambiente

### 2.1 Instalar

- **Git**: <https://git-scm.com/downloads>
- **Python 3.10+**: <https://www.python.org/downloads/>
- (Opcional) **GitHub CLI** (`gh`): <https://cli.github.com/>

Confira:

```bash
git --version
python --version        # no Mac/Linux, pode ser python3
```

### 2.2 Configurar sua identidade (uma única vez)

```bash
git config --global user.name  "Seu Nome"
git config --global user.email "seu-email-do-github@exemplo.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"   # opcional: usar o VS Code como editor
git config --list                                 # confere as configurações
```

### 2.3 Autenticar no GitHub

O GitHub **não aceita mais a senha da conta** para `git push` via HTTPS. Escolha **uma** opção:

| Opção | Como |
|-------|------|
| **GitHub CLI** (mais simples) | `gh auth login` e siga as perguntas (HTTPS + login pelo navegador). |
| **Personal Access Token (PAT)** | GitHub → Settings → Developer settings → Personal access tokens. Use o token no lugar da senha quando o Git pedir. |
| **Chave SSH** | `ssh-keygen -t ed25519 -C "seu-email"` → adicione o conteúdo de `~/.ssh/id_ed25519.pub` em GitHub → Settings → SSH and GPG keys. Clone com a URL `git@github.com:...`. |

> Nunca compartilhe tokens ou chaves privadas, e nunca os coloque em commits.

---

## 3. A atividade: caçando bugs com Git

**Objetivo:** corrigir os bugs de `gerenciador_notas.py` usando o fluxo profissional do GitHub:
**issue → branch → correção → commit → push → pull request → revisão → merge**.
O programa só está correto quando **todos os testes passam**.

### 3.1 Conhecendo o projeto

```bash
python -m unittest -v test_gerenciador_notas     # roda os testes (vários vão FALHAR no início)
python gerenciador_notas.py                      # abre o menu interativo
```

> Cada teste que falha aponta para um bug. **Não edite o arquivo de testes.**

### 3.2 Passo a passo (fluxo com fork)

> Se o professor adicionou você como **colaborador** do repositório, pule o fork: clone o repositório direto, use `origin` onde este guia diz `upstream` e abra os Pull Requests dentro do próprio repositório.

**1. Fork e clone**

1. No GitHub, clique em **Fork** no repositório da aula.
2. Clone o **seu** fork:

```bash
git clone https://github.com/<seu-usuario>/sudoku-game.git
cd sudoku-game
git remote add upstream https://github.com/josepaes23/sudoku-game.git   # repositório original
git remote -v                                                            # origin = seu fork; upstream = original
```

**2. Crie uma issue para o bug** (aba *Issues* → *New issue*). Exemplo: *"menor_nota sempre retorna 0"*, anotando o teste que falha.

**3. Crie uma branch para a issue**

```bash
git switch main
git pull upstream main              # garante que você parte do código mais recente
git switch -c fix/menor-nota        # cria e já troca para a nova branch
```

**4. Encontre e corrija o bug** (use os testes como guia)

```bash
python -m unittest -v test_gerenciador_notas.TestValidacaoECalculos.test_menor_nota
```

**5. Revise o que mudou antes de commitar**

```bash
git status
git diff                            # alterações ainda não preparadas
git add gerenciador_notas.py
git diff --staged                   # o que vai entrar no commit
```

**6. Faça o commit** (uma correção = um commit)

```bash
git commit -m "fix: inicializa menor com a primeira nota"
```

**7. Envie a branch e abra o Pull Request**

```bash
git push -u origin fix/menor-nota
```

No GitHub, clique em **Compare & pull request**. Na descrição escreva `Closes #<número da issue>` para fechar a issue automaticamente no merge. Pelo terminal:

```bash
gh pr create --title "fix: menor_nota sempre retorna 0" --body "Closes #1"
```

**8. Revisão:** peça a um colega que revise (aba *Files changed* → comentários). Ajuste e faça novos commits na mesma branch, se necessário.

**9. Merge** do PR pelo botão **Merge pull request** e limpeza:

```bash
git switch main
git pull upstream main              # traz o que foi aprovado
git push origin main                # atualiza o seu fork
git branch -d fix/menor-nota        # apaga a branch local
git push origin --delete fix/menor-nota   # apaga a branch remota (opcional)
```

**10. Repita** com o próximo bug, **sempre começando de uma `main` atualizada**.

### 3.3 Desafios extras

- **Conflito:** duas pessoas corrigem o mesmo bug de formas diferentes; resolvam o conflito no merge (seção 5).
- **Desfazer:** faça um commit com mensagem errada e corrija com `git commit --amend`; faça um commit ruim e desfaça com `git revert`.
- **Guardar trabalho:** altere um arquivo, troque de branch usando `git stash` e depois recupere com `git stash pop`.
- **Investigar:** use `git log -p gerenciador_notas.py` e `git blame gerenciador_notas.py` para descobrir quem alterou cada linha.
- **Release:** quando todos os testes passarem, crie uma tag: `git tag -a v1.0 -m "Todos os bugs corrigidos"` e `git push origin v1.0`.

---

## 4. Cheat sheet de comandos

### 4.1 Configuração e início

| Comando | O que faz |
|---------|-----------|
| `git config --global user.name "Nome"` | Define seu nome nos commits. |
| `git config --global user.email "email"` | Define seu e-mail nos commits. |
| `git init` | Cria um repositório novo na pasta atual. |
| `git clone <url>` | Copia um repositório remoto para o computador. |
| `git remote -v` | Lista os remotos configurados. |
| `git remote add <nome> <url>` | Adiciona um remoto (ex.: `upstream`). |

### 4.2 Ciclo básico

| Comando | O que faz |
|---------|-----------|
| `git status` | Mostra o estado dos arquivos (modificados, preparados, novos). |
| `git add <arquivo>` | Prepara um arquivo para o commit. |
| `git add .` | Prepara tudo da pasta atual (confira com `git status` antes!). |
| `git add -p` | Escolhe, trecho por trecho, o que preparar. |
| `git diff` | Mostra alterações **não** preparadas. |
| `git diff --staged` | Mostra alterações preparadas (o que entrará no commit). |
| `git commit -m "mensagem"` | Cria um commit com o que está preparado. |
| `git commit --amend` | Altera o **último** commit (mensagem ou conteúdo). |
| `git push` | Envia commits para o remoto. |
| `git push -u origin <branch>` | Primeiro envio de uma branch (guarda o vínculo). |
| `git fetch` | Baixa novidades do remoto **sem** alterar seus arquivos. |
| `git pull` | `fetch` + merge das novidades na branch atual. |
| `git pull --rebase` | Traz as novidades reaplicando seus commits por cima (histórico linear). |

### 4.3 Branches

| Comando | O que faz |
|---------|-----------|
| `git branch` | Lista as branches locais (`-a` inclui as remotas). |
| `git switch <branch>` | Troca de branch. |
| `git switch -c <branch>` | Cria uma branch e troca para ela. |
| `git merge <branch>` | Junta a `<branch>` na branch atual. |
| `git branch -d <branch>` | Apaga uma branch já integrada (`-D` força). |
| `git push origin --delete <branch>` | Apaga a branch no remoto. |

### 4.4 Histórico e investigação

| Comando | O que faz |
|---------|-----------|
| `git log --oneline` | Histórico resumido, um commit por linha. |
| `git log --oneline --graph --decorate --all` | Histórico em forma de grafo, com todas as branches. |
| `git log -p <arquivo>` | Histórico de um arquivo, com as alterações. |
| `git log --author="Nome"` | Commits de uma pessoa. |
| `git show <hash>` | Detalhes e alterações de um commit. |
| `git blame <arquivo>` | Quem alterou cada linha, e em qual commit. |

### 4.5 Desfazer (do menos para o mais perigoso)

| Situação | Comando |
|----------|---------|
| Descartar alterações **não preparadas** de um arquivo | `git restore <arquivo>` |
| Tirar um arquivo da área de preparação (mantém a alteração) | `git restore --staged <arquivo>` |
| Corrigir mensagem/conteúdo do último commit (ainda **não enviado**) | `git commit --amend` |
| Desfazer o último commit mantendo as alterações preparadas | `git reset --soft HEAD~1` |
| Desfazer o último commit mantendo as alterações no arquivo | `git reset HEAD~1` |
| Desfazer um commit **já enviado**, criando um novo commit inverso | `git revert <hash>` |
| Guardar alterações temporariamente | `git stash` (depois `git stash pop`; lista: `git stash list`) |
| Descartar **tudo** e voltar ao último commit (**irreversível**) | `git reset --hard` |
| Recuperar commits "perdidos" | `git reflog` |

> **Regra de ouro:** em commits que já foram para o GitHub, use `git revert`. Evite `reset` e `push --force` em branches compartilhadas.

### 4.6 Tags

| Comando | O que faz |
|---------|-----------|
| `git tag -a v1.0 -m "mensagem"` | Cria uma tag anotada (marco de versão). |
| `git push origin v1.0` | Envia a tag para o GitHub. |

### 4.7 GitHub CLI (`gh`)

| Comando | O que faz |
|---------|-----------|
| `gh auth login` | Autentica no GitHub. |
| `gh repo clone <usuario>/<repo>` | Clona um repositório. |
| `gh repo fork --clone` | Faz fork e clona. |
| `gh issue create` | Cria uma issue. |
| `gh issue list` | Lista issues abertas. |
| `gh pr create` | Abre um Pull Request da branch atual. |
| `gh pr list` / `gh pr view` | Lista / mostra Pull Requests. |
| `gh pr checkout <número>` | Baixa a branch de um PR para revisar. |
| `gh pr merge` | Faz o merge de um PR. |

---

## 5. Resolvendo conflitos

Um **conflito** acontece quando duas branches alteram **as mesmas linhas** e o Git não sabe qual versão manter. Exemplo ao rodar `git merge fix/ranking-ordem`:

```
Auto-merging gerenciador_notas.py
CONFLICT (content): Merge conflict in gerenciador_notas.py
Automatic merge failed; fix conflicts and then commit the result.
```

O arquivo fica marcado assim:

```
<<<<<<< HEAD
            if media_a < media_b:
=======
            if media_b > media_a:
>>>>>>> fix/ranking-ordem
```

- Entre `<<<<<<< HEAD` e `=======`: a versão da **sua** branch atual.
- Entre `=======` e `>>>>>>>`: a versão da **outra** branch.

**Passo a passo:**

1. `git status` — veja quais arquivos estão em conflito.
2. Abra o arquivo, **escolha (ou combine) o código correto** e **apague as marcas** `<<<<<<<`, `=======` e `>>>>>>>`.
3. Rode os testes para garantir que o resultado funciona.
4. `git add gerenciador_notas.py`
5. `git commit` (o Git sugere uma mensagem de merge pronta).

Desistiu? `git merge --abort` volta ao estado anterior ao merge. O VS Code também oferece os botões *Accept Current / Incoming / Both Changes*.

**Como evitar:** branches curtas, `git pull` frequente, PRs pequenos e comunicação com a equipe sobre quem altera o quê.

---

## 6. Boas práticas

### 6.1 Commits

- **Atômicos:** um commit = uma mudança lógica. Não misture correção de bug com formatação de outro arquivo.
- **Frequentes e pequenos:** facilitam revisão, `revert` e `blame`.
- **Funcionando:** não commite código que quebra o projeto ou os testes.
- **Revise antes:** `git status` e `git diff --staged` antes de cada `git commit`.
- **Não use `git add .` no automático:** você pode incluir arquivos indesejados (senhas, binários, pastas de cache).

### 6.2 Mensagens de commit

Use o padrão **Conventional Commits**: `tipo: descrição curta no imperativo`.

| Tipo | Quando usar | Exemplo |
|------|-------------|---------|
| `feat` | Nova funcionalidade | `feat: adiciona média ponderada` |
| `fix` | Correção de bug | `fix: considera todas as notas em calcular_media` |
| `docs` | Documentação | `docs: adiciona guia de comandos ao README` |
| `test` | Testes | `test: cobre limite de 25% de faltas` |
| `refactor` | Reorganização sem mudar comportamento | `refactor: extrai função percentual_faltas` |
| `style` | Formatação (sem mudar lógica) | `style: ajusta espaçamento` |
| `chore` | Tarefas de manutenção | `chore: adiciona .gitignore` |

Regras de ouro:

1. Assunto com **até ~50 caracteres**, no imperativo ("corrige", "adiciona"), sem ponto final.
2. Se precisar, deixe uma **linha em branco** e explique o **porquê** no corpo da mensagem.
3. Evite mensagens vagas: ~~`ajustes`~~, ~~`teste`~~, ~~`agora vai`~~, ~~`asdf`~~.

### 6.3 Branches

- A `main` deve estar **sempre funcionando**. Nada de commitar direto nela em trabalho em equipe.
- **Uma branch por tarefa/issue**, curta e focada.
- Nomes com prefixo e palavras separadas por hífen: `feature/login`, `fix/menor-nota`, `docs/readme`.
- Depois do merge, **apague** a branch.
- **Atualize antes de começar** (`git pull`) e traga a `main` para sua branch de tempos em tempos.

### 6.4 Pull Requests e revisão de código

- PRs **pequenos** (idealmente que dê para revisar em poucos minutos).
- Título claro e descrição com **o que mudou, por quê e como testar**; referencie a issue (`Closes #12`).
- Rode os testes **antes** de abrir o PR.
- Revise com respeito: comente o código, não a pessoa; sugira, pergunte, explique.
- Não faça o merge do seu próprio PR sem revisão em projetos de equipe.

### 6.5 O que **não** versionar: `.gitignore`

Crie um arquivo `.gitignore` na raiz. Para Python:

```gitignore
__pycache__/
*.pyc
.venv/
venv/
.env
.idea/
.vscode/
.DS_Store
```

- **Nunca** versione senhas, tokens, chaves de API ou arquivos `.env`.
- Se um segredo foi commitado: **revogue/troque imediatamente** (apagar o commit depois **não** basta, pois o histórico é público).
- Evite versionar arquivos gerados (builds, caches) e binários grandes.

### 6.6 Colaboração

- **Sincronize** com frequência: `git pull` antes de começar e antes de dar `push`.
- **Nunca reescreva histórico compartilhado** (`push --force`, `reset` em commits já enviados). Se precisar forçar em uma branch **só sua**, prefira `git push --force-with-lease`.
- Use **issues** para registrar bugs e tarefas, e **labels/milestones** para organizar.
- Mantenha um **README** atualizado (o que é o projeto, como instalar, como rodar os testes) e, em projetos públicos, uma **licença**.
- Habilite a **proteção da branch `main`** (Settings → Branches) exigindo PR e revisão.

### 6.7 Checklist antes de cada commit

- [ ] O código roda e os testes passam?
- [ ] `git status` mostra apenas os arquivos que eu quero?
- [ ] `git diff --staged` não tem *prints* de depuração, senhas ou lixo?
- [ ] A mensagem explica a mudança e segue o padrão?

---

## 7. Problemas comuns e soluções

| Problema | Solução |
|----------|---------|
| `fatal: not a git repository` | Você não está na pasta do projeto. Use `cd` até ela (ou `git init`/`git clone`). |
| `Authentication failed` / `Permission denied` no push | Use `gh auth login`, um token (PAT) ou chave SSH (seção 2.3). Confirme que o fork é seu. |
| `rejected ... (non-fast-forward)` / `Updates were rejected` | O remoto tem commits que você não tem. Faça `git pull` (ou `git pull --rebase`), resolva conflitos e tente de novo. |
| Commitei na `main` sem querer (ainda não enviei) | `git branch fix/minha-correcao` (guarda o commit) → `git reset --hard origin/main` (volta a `main`) → `git switch fix/minha-correcao`. |
| Errei a mensagem do último commit (ainda não enviei) | `git commit --amend -m "mensagem correta"`. |
| Adicionei um arquivo errado ao staging | `git restore --staged <arquivo>`. |
| Quero voltar um arquivo ao último commit | `git restore <arquivo>` (descarta suas alterações nele). |
| Preciso trocar de branch com alterações pendentes | `git stash` → `git switch outra-branch` → depois `git stash pop`. |
| `Your local changes would be overwritten by merge` | Commit ou `git stash` suas alterações e repita o comando. |
| Commitei um arquivo que devia estar no `.gitignore` | `git rm --cached <arquivo>` → adicione ao `.gitignore` → commit. |
| "Detached HEAD" | Você está em um commit solto. Para guardar o trabalho: `git switch -c nova-branch`. Para sair: `git switch main`. |
| Apaguei algo importante | `git reflog` mostra os commits recentes; recupere com `git switch -c recuperada <hash>`. |

---

## 8. Referências

- Livro **Pro Git** (gratuito, em português): <https://git-scm.com/book/pt-br/v2>
- Documentação do GitHub: <https://docs.github.com/pt>
- Referência de comandos do Git: <https://git-scm.com/docs>
- Conventional Commits: <https://www.conventionalcommits.org/pt-br/>
- GitHub Skills (cursos práticos interativos): <https://skills.github.com/>
- Aprender Git visualmente (branches): <https://learngitbranching.js.org/?locale=pt_BR>
- Gerador de `.gitignore`: <https://www.toptal.com/developers/gitignore>
- GitHub CLI: <https://cli.github.com/manual/>
