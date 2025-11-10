# 🐍 SIMULADOR DE FINANÇAS PESSOAIS (CLI)

Um projeto prático e modular em Python para gestão básica de entradas e saídas financeiras via linha de comando (CLI).

## 💡 Motivação & Aprimoramento

Este projeto foi desenvolvido como um **desafio pessoal** para aprofundar e consolidar meus conhecimentos em Python. O foco principal foi garantir a **boa arquitetura** e a **separação de responsabilidades** dentro do código.

Com o desenvolvimento deste simulador, busquei praticar:

✅ **Modularização Eficaz:** Dividindo a aplicação em módulos lógicos (`transacoes.py`, `relatorios.py`, `menu.py`).
✅ **Persistência de Dados:** Implementação do módulo nativo `csv` para salvar e recuperar o histórico financeiro.
✅ **Estrutura de Projeto:** Organização de arquivos em diretórios (`src`, `dados`) seguindo boas práticas de projetos Python.
✅ **Lógica de Negócio:** Criação de algoritmos para cálculo de saldo e geração de relatórios.

---

## ✨ Funcionalidades

O programa oferece uma interface de menu simples e direta:

| Opção | Descrição | Módulo Principal |
| :---: | :--- | :--- |
| **1** | Adicionar Entrada/Saída | `transacoes.py` |
| **2** | Listar Todo o Histórico | `transacoes.py` |
| **3** | Visualizar Saldo Atual | `transacoes.py` |
| **4** | Gerar Relatório (TXT) | `relatorios.py` |
| **5** | Sair do Programa | `menu.py` |

---

## 🛠️ Como Iniciar

O projeto não exige a instalação de bibliotecas externas, apenas uma instalação padrão do Python 3.

1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/CarlosEduardo-J/simulador-de-financas.git
    cd simulador-financas
    ```

2.  **Executar a Aplicação:**
    Basta rodar o arquivo `main.py` dentro da pasta `src`:
    ```bash
    python src/main.py
    ```
3.  **Aproveite!**
    O menu interativo será exibido no seu terminal.

---

## 🔮 Futuras Melhorias

Como um projeto em constante evolução, as seguintes melhorias estão planejadas:

* **Validação de Input:** Implementar checagem mais robusta para entradas de usuário.
* **Edição/Exclusão:** Adicionar opções para modificar ou remover transações existentes.
* **Melhoria em Relatórios:** Gerar relatórios em formatos mais estruturados (JSON ou gráficos simples).