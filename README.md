
<div align="center">

# 📊 Processamento e Análise de Dados CSV

**Processamento, consolidação e análise de dados do Poder Judiciário utilizando Python e programação paralela.**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Multiprocessing](https://img.shields.io/badge/Multiprocessing-334155?style=for-the-badge)
![Projeto Acadêmico](https://img.shields.io/badge/Projeto-Acadêmico-6D28D9?style=for-the-badge)

<br>

[Sobre](#-sobre-o-projeto) •
[Funcionalidades](#-funcionalidades) •
[Tecnologias](#-tecnologias-utilizadas) •
[Como executar](#-instalação-e-execução) •
[Estrutura](#-estrutura-do-repositório)

</div>

---

## 📖 Sobre o projeto

Este repositório apresenta um projeto acadêmico desenvolvido em **Python** para processamento, consolidação e análise de arquivos CSV contendo informações de tribunais brasileiros e indicadores relacionados às **Metas do Poder Judiciário**.

O projeto possui duas abordagens de implementação:

- **Versão não paralela:** processamento sequencial dos arquivos.
- **Versão paralela:** distribuição de tarefas entre processos utilizando a biblioteca `multiprocessing`.

As duas versões realizam a leitura dos dados, normalização dos ramos da Justiça, cálculo de indicadores e geração de arquivos CSV com os resultados.

### 🎯 Objetivos

- Aplicar técnicas de manipulação de dados com Python.
- Automatizar a leitura e consolidação de múltiplos arquivos CSV.
- Implementar cálculos de indicadores relacionados às metas judiciais.
- Explorar conceitos de programação sequencial e paralela.
- Comparar diferentes estratégias de processamento de dados.

---

## ✨ Funcionalidades

### 📂 Processamento de arquivos

- Leitura de múltiplos arquivos no formato CSV.
- Consolidação de dados em um único arquivo.
- Identificação de tribunais e seus respectivos ramos da Justiça.
- Normalização de categorias utilizadas nos dados.
- Exportação dos resultados em arquivos CSV.

### 📈 Cálculo de indicadores

O projeto implementa funções de cálculo para diferentes metas, incluindo:

| Indicador | Identificação no código |
|:---|:---|
| Meta 1 | `meta1` |
| Meta 2 | `meta2A`, `meta2B`, `meta2C`, `meta2ANT` |
| Meta 4 | `meta4A`, `meta4B` |
| Meta 6 | `meta6` |
| Meta 7 | `meta7A`, `meta7B` |
| Meta 8 | `meta8`, `meta8A`, `meta8B` |
| Meta 10 | `meta10`, `meta10A`, `meta10B` |

Os cálculos utilizam informações extraídas dos arquivos de entrada e consideram fatores específicos definidos no código para determinados ramos da Justiça.

Quando uma meta não se aplica a determinado ramo, ou quando não é possível realizar o cálculo, o programa pode retornar `NA`.

> As fórmulas são implementações acadêmicas presentes no código e não devem ser interpretadas como uma validação oficial dos indicadores do Poder Judiciário.

### ⚡ Processamento paralelo

A versão paralela utiliza `multiprocessing` para distribuir operações de leitura e processamento entre diferentes processos.

São utilizados:

- `Pool`: gerenciamento de um conjunto de processos.
- `cpu_count()`: identificação da quantidade de CPUs disponíveis.
- `pool.map()`: distribuição das tarefas de processamento.

O objetivo é explorar o uso de múltiplos núcleos do processador em tarefas que envolvem diferentes arquivos.

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Finalidade |
|:---|:---|
| **Python** | Linguagem principal do projeto |
| **Pandas** | Leitura, manipulação, consolidação e exportação de dados |
| **Multiprocessing** | Execução paralela de tarefas |
| **OS** | Acesso aos arquivos e diretórios |
| **Time** | Medição do tempo de execução |
| **CSV** | Formato dos dados de entrada e saída |

---

## ⚙️ Versões do processamento

O projeto permite estudar duas estratégias de execução.

### 1. Versão não paralela — `Versao_NP.py`

Executa o processamento de maneira sequencial, utilizando estruturas de repetição e operações do Pandas.

**Fluxo de execução:**

1. Localiza os arquivos CSV disponíveis.
2. Realiza a leitura dos arquivos.
3. Consolida os dados em um único DataFrame.
4. Processa individualmente as informações de cada tribunal.
5. Calcula os indicadores das metas.
6. Exporta os resultados.

### 2. Versão paralela — `Versao_P.py`

Utiliza múltiplos processos para distribuir a leitura e o processamento dos arquivos.

**Fluxo de execução:**

1. Identifica os arquivos CSV.
2. Cria um conjunto de processos.
3. Distribui a leitura dos arquivos entre os processos.
4. Consolida os dados.
5. Distribui o cálculo das metas.
6. Reúne os resultados e exporta os relatórios.

### 📊 Comparação das abordagens

| Característica | Não paralela | Paralela |
|:---|:---:|:---:|
| Processamento sequencial | ✅ | — |
| Múltiplos processos | — | ✅ |
| Biblioteca Pandas | ✅ | ✅ |
| Cálculo de indicadores | ✅ | ✅ |
| Consolidação de arquivos | ✅ | ✅ |
| Medição do tempo de execução | ✅ | ✅ |

> **Nota:** a implementação paralela não garante menor tempo de execução em todos os cenários. O desempenho depende da quantidade de arquivos, do volume de dados e dos recursos disponíveis no computador.

---

## 📁 Estrutura do repositório

```text
Processando_CSVs/
│
├── Versao_NP.py       # Processamento sequencial
├── Versao_P.py        # Processamento paralelo
└── README.md          # Documentação do projeto
```

Para executar os scripts, é necessário disponibilizar um diretório `Dados/` contendo os arquivos CSV de entrada.

```text
Processando_CSVs/
│
├── Dados/
│   ├── arquivo_01.csv
│   ├── arquivo_02.csv
│   └── ...
│
├── Versao_NP.py
├── Versao_P.py
└── README.md
```

> A pasta `Dados/` não está incluída nos arquivos disponibilizados neste repositório.

---

## 🚀 Instalação e execução

### Pré-requisitos

- Python 3 instalado.
- Gerenciador de pacotes pip.
- Git, caso deseje clonar o repositório.

### 1. Clone o repositório

```bash
git clone https://github.com/JuliaGabrielyPereiraRodrigues/Processando_CSVs.git
```

Acesse o diretório:

```bash
cd Processando_CSVs
```

### 2. Instale as dependências

```bash
python -m pip install pandas
```

### 3. Prepare os arquivos de entrada

Crie uma pasta chamada `Dados` na raiz do projeto e adicione os arquivos CSV que serão processados.

Os arquivos devem conter as colunas esperadas pelos scripts, incluindo:

- `sigla_tribunal`
- `ramo_justica`
- `julgados_2025`
- `casos_novos_2025`
- `dessobrestados_2025`
- `suspensos_2025`

Também são necessárias as colunas específicas para o cálculo das demais metas.

### 4. Execute a versão desejada

**Processamento sequencial:**

```bash
python Versao_NP.py
```

**Processamento paralelo:**

```bash
python Versao_P.py
```

> Execute os comandos a partir da raiz do repositório. Os scripts utilizam caminhos relativos para localizar a pasta `Dados/`.

---

## 📄 Arquivos de saída

Após o processamento, são gerados dois arquivos no diretório de execução.

### `Consolidado.csv`

Contém os registros dos arquivos CSV de entrada reunidos em um único conjunto de dados.

### `ResumoMetas.csv`

Apresenta os resultados dos indicadores calculados para cada tribunal.

Entre as colunas do arquivo estão:

```text
tribunal
ramo_justica
meta1
meta2A
meta2B
meta2C
meta2ANT
meta4A
meta4B
meta6
meta7A
meta7B
meta8
meta8A
meta8B
meta10
meta10A
meta10B
```

Os resultados são gravados no formato CSV e podem ser consultados em ferramentas de análise de dados.

---

## ⏱️ Análise de desempenho

Ambas as versões incluem uma medição do tempo total de execução utilizando a biblioteca `time`.

Exemplo do formato de saída:

```text
Tempo total de execução: X.XX segundos
```

Essa funcionalidade permite observar o tempo utilizado por cada abordagem ao processar um mesmo conjunto de arquivos.

Para uma comparação mais confiável, recomenda-se executar ambas as versões com os mesmos dados, repetir as medições e comparar os resultados.

---

## 📚 Aprendizados

O desenvolvimento deste projeto envolve conceitos de:

- Programação em Python.
- Manipulação de dados estruturados.
- Processamento de arquivos CSV.
- Utilização da biblioteca Pandas.
- Consolidação e transformação de dados.
- Automação de cálculos.
- Programação paralela com múltiplos processos.
- Medição de desempenho computacional.
- Tratamento de exceções.

---

## 🔮 Possíveis melhorias

- Implementar validações para a estrutura dos arquivos CSV.
- Adicionar tratamento para pastas vazias e arquivos inconsistentes.
- Criar testes automatizados para os cálculos das metas.
- Separar as funções de cálculo em módulos reutilizáveis.
- Automatizar a comparação de desempenho entre as versões.
- Gerar relatórios com visualizações gráficas.
- Documentar o formato completo dos arquivos de entrada.

---

## 🎓 Contexto acadêmico

Projeto desenvolvido individualmente para fins educacionais, com foco na aplicação de conceitos de programação, processamento de dados e paralelismo.

---

## 👩‍💻 Autoria

Desenvolvido por **[Julia Gabriely](https://github.com/JuliaGabrielyPereiraRodrigues)**.

<div align="center">

---

**[⬆ Voltar ao topo](#-processamento-e-análise-de-dados-csv)**

</div>
