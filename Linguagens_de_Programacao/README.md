# 🐍 Linguagens de Programação — FATEC Itaquaquecetuba

Este repositório reúne os exercícios, atividades práticas e projetos desenvolvidos durante a disciplina de **Linguagens de Programação**, cursada no 2º semestre do **Curso Superior de Tecnologia em Gestão da Tecnologia da Informação (GTI)**, na **Faculdade de Tecnologia (FATEC) de Itaquaquecetuba**, em 2026.

A disciplina tem como objetivo desenvolver conhecimentos fundamentais de lógica de programação, resolução de problemas e desenvolvimento de aplicações utilizando a linguagem Python, abordando desde conceitos básicos até programação orientada a objetos e integração com bancos de dados.

---

## 📁 Estrutura de Pastas e Projetos

Os códigos estão organizados na pasta [`Projetos_python`](./Projetos_python), estruturados em conteúdos de estudo e atividades práticas:

```text
Projetos_python/
├── 01_Fundamentos_e_Operadores/
│   ├── area_circulo.py
│   ├── area_retangulo.py
│   ├── conversor_temperatura.py
│   ├── expressoes_booleanas.py
│   ├── media_ponderada.py
│   ├── operadores_logicos_and.py
│   ├── operadores_logicos_not.py
│   └── operadores_logicos_or.py
│
├── 02_Estruturas_Condicionais/
│   ├── estrutura_decisao.py
│   └── estrutura_elif.py
│
├── 03_Estruturas_de_Dados/
│   └── operacao_conjuntos.py
│
├── 04_Modularizacao/
│   ├── formas_importacao.py
│   ├── main.py
│   ├── modularizacao_bibliotecas.py
│   └── operacoes.py
│
├── 05_Banco_de_Dados/
│   ├── desafio_pratico.py
│   ├── produtos.db
│   └── python_sqlite.py
│
└── Atividades/
    ├── Atividade_18_09_Gerenciador_Equipamentos/
    │   ├── exercicio_18_09.py
    │   └── exercicio_18_09_2.py
    │
    ├── Atividade_02_10_Monitoramento_Servidores/
    │   ├── exercicio_02_10.py
    │   └── exercicio2_02_10.py
    │
    ├── Atividade_24_10_Sistema_Chamados/
    │   └── Sistema_chamados_24_10.py
    │
    └── Desafios_de_Logica/
        ├── desafio_1.py
        ├── desafio_1_sem_if.py
        ├── desafio_2.py
        ├── desafio_3.py
        ├── exercicio_cinema.py
        └── votacao_desafio.py
```

---

## 📚 Conteúdos e Módulos Estudados

### 1. [01_Fundamentos_e_Operadores](./Projetos_python/01_Fundamentos_e_Operadores)
- **`area_circulo.py`**: Cálculo da área do círculo utilizando `math.pi` e exponenciação.
- **`area_retangulo.py`**: Cálculo da área do retângulo com validação de dimensões.
- **`conversor_temperatura.py`**: Conversão de temperaturas entre Celsius e Fahrenheit.
- **`media_ponderada.py`**: Cálculo de média ponderada de notas de alunos.
- **`expressoes_booleanas.py`**: Conceito de expressões lógicas e retorno booleano (`True` / `False`).
- **`operadores_logicos_and.py`**, **`operadores_logicos_or.py`**, **`operadores_logicos_not.py`**: Demonstração e prática dos operadores lógicos em Python.

### 2. [02_Estruturas_Condicionais](./Projetos_python/02_Estruturas_Condicionais)
- **`estrutura_decisao.py`**: Tomada de decisão básica com `if` e `else`.
- **`estrutura_elif.py`**: Estruturas de múltiplas condições com `if`, `elif` e `else` (classificação de notas).

### 3. [03_Estruturas_de_Dados](./Projetos_python/03_Estruturas_de_Dados)
- **`operacao_conjuntos.py`**: Manipulação de conjuntos (`set`) em Python: união (`|`), interseção (`&`) e diferença (`-`) aplicados a redes de computadores.

### 4. [04_Modularizacao](./Projetos_python/04_Modularizacao)
- **`formas_importacao.py`**: Demonstração de importação seletiva (`from ... import ...`) e uso de alias (`import ... as ...`).
- **`operacoes.py`**: Módulo contendo funções matemáticas básicas (soma, subtração, multiplicação, divisão).
- **`main.py`**: Arquivo principal consumindo o módulo `operacoes`.
- **`modularizacao_bibliotecas.py`**: Estrutura e boas práticas de arquitetura em múltiplos módulos.

### 5. [05_Banco_de_Dados](./Projetos_python/05_Banco_de_Dados)
- **`python_sqlite.py`**: Introdução à integração do Python com SQLite 3 e conceitos de CRUD.
- **`desafio_pratico.py`**: Criação de tabela `produtos`, inserção parametrizada e consulta formatada dos registros.
- **`produtos.db`**: Arquivo de banco de dados SQLite persistido.

---

## 🎯 Atividades Práticas e Desafios

### 🛠️ [Atividade 18/09 — Gerenciador de Equipamentos](./Projetos_python/Atividades/Atividade_18_09_Gerenciador_Equipamentos)
- **`exercicio_18_09.py`**: Cadastro de equipamentos em listas com laço `for`, validação de meta e busca com `in`.
- **`exercicio_18_09_2.py`**: Sistema interativo em terminal com menu numérico (`while`), cadastro, exibição, contagem e remoção de equipamentos de TI.

### 🖥️ [Atividade 02/10 — Monitoramento de Servidores e Hardware](./Projetos_python/Atividades/Atividade_02_10_Monitoramento_Servidores)
- **`exercicio_02_10.py`**: Modelagem de patrimônio/computador com dicionários Python, alteração de valores e consulta de chaves.
- **`exercicio2_02_10.py`**: Monitoramento de parque de servidores com lista de dicionários, contagem de servidores online/offline e emissão de alertas de sobrecarga.

### 🎫 [Atividade 24/10 — Sistema de Chamados de TI](./Projetos_python/Atividades/Atividade_24_10_Sistema_Chamados)
- **`Sistema_chamados_24_10.py`**: Estruturação de dados para gerenciamento de chamados de suporte técnico (ID, descrição, prioridade e status).

### 💡 [Desafios de Lógica](./Projetos_python/Atividades/Desafios_de_Logica)
- **`desafio_1.py`**: Verificação condicional de idade e cadastro com `and`.
- **`desafio_1_sem_if.py`**: Resolução da mesma lógica condicional usando apenas avaliação booleana direta.
- **`desafio_2.py`**: Cálculo de total e desconto comercial de produtos.
- **`desafio_3.py`**: Exercício complementar de fixação.
- **`votacao_desafio.py`**: Verificação simples de idade mínima permitida para voto.
- **`exercicio_cinema.py`**: Avaliação de elegibilidade e critérios compostos com operadores lógicos.

---

## 📌 Conteúdos Previstos

Os seguintes assuntos também fazem parte do planejamento da disciplina:
- Programação Orientada a Objetos (POO): classes, objetos, atributos e métodos.
- Herança e polimorfismo: reutilização de código e princípios de orientação a objetos.

---

## 💻 Tecnologias Utilizadas

- **Python 3** — Linguagem principal utilizada no desenvolvimento das atividades.
- **SQLite 3** — Banco de dados relacional utilizado para persistência de dados.
- **SQL** — Linguagem utilizada para operações de consulta e manipulação de dados.

---

## 🎯 Objetivos do Repositório

Este repositório tem como finalidade registrar minha evolução acadêmica e prática durante a disciplina, reunindo códigos e atividades que demonstram a aplicação dos conceitos estudados em sala de aula.

Além de servir como material de consulta e revisão, os projetos permitem acompanhar o desenvolvimento das minhas habilidades em programação, raciocínio lógico, organização de código e resolução de problemas utilizando Python.
