# Olá, eu sou o Samuel! 👋

### 🛡️ Aspirante a Analista de Cibersegurança | Entusiasta de Red & Blue Team

Atualmente, estou mergulhando no mundo da Segurança da Informação, com foco em entender tanto as táticas ofensivas quanto as defesas de rede. Sou um entusiasta de Linux e busco constantemente aprimorar minhas habilidades.

---

### 🚀 Sobre Mim
- 🎓 **Foco Atual:** Estudando fundamentos de Red Team e Blue Team no **TryHackMe**.
- 💻 **Linguagens:** Python e JavaScript para automação e ferramentas de segurança.
- 🐧 **OS Preferido:** Kali Linux e sistemas baseados em Debian.
- 📍 **Localização:** Brasília, Brasil.

---

### 🛠️ Ferramentas e Tecnologias

#### **Cibersegurança & Redes**
![Nmap](https://img.shields.io/badge/Nmap-DFE1E5?style=for-the-badge&logo=nmap&logoColor=black)
![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kali-linux&logoColor=white)
![Wireshark](https://img.shields.io/badge/Wireshark-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![TryHackMe](https://img.shields.io/badge/TryHackMe-212c42?style=for-the-badge&logo=tryhackme&logoColor=red)

#### **Programação**
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)

---

## 📂 Meus Projetos em Destaque

### Sistema de Reserva de Assentos de Cinema 🎬

Um sistema completo para gerenciar reservas de assentos em uma sala de cinema com funcionalidades como:
- ✅ Seleção de Assentos
- ✅ Validação de Ocupação
- ✅ Cálculo de Receita
- ✅ Visualização do Mapa da Sala

(Estou começando agora, esse é só o primeiro de muitos projetos razoavelmente grandes. Estou sempre disposto a aprender!)

---

## 🚀 Como Executar o Projeto - Tutorial Passo a Passo

### 📋 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu sistema:

1. **Python 3.8+** - [Baixar aqui](https://www.python.org/downloads/)
2. **Git** - [Baixar aqui](https://git-scm.com/downloads)
3. **uv** (Gerenciador de pacotes) - Instale com:
   ```bash
   pip install uv
   ```

### 📥 Passo 1: Clonar o Repositório

Abra o terminal/prompt de comando e execute:

```bash
git clone https://github.com/0samuelog/Sistema-de-Reserva-de-Assentos-de-Cinema.git
cd Sistema-de-Reserva-de-Assentos-de-Cinema
```

### 📦 Passo 2: Instalar as Dependências

Com o `uv`, instale as dependências do projeto automaticamente:

```bash
uv sync
```

**Alternativa (se preferir usar pip diretamente):**
```bash
pip install -r requirements.txt
```

### ▶️ Passo 3: Executar o Projeto

Para iniciar o sistema de reserva de assentos de cinema:

```bash
python main.py
```

Ou, se estiver usando o `uv`:

```bash
uv run python main.py
```

### 🧪 Passo 4: Executar os Testes (Opcional)

Para validar que tudo está funcionando corretamente, execute os testes:

```bash
python -m pytest tests/
```

Ou com `uv`:

```bash
uv run pytest tests/
```

---

## 📁 Estrutura do Projeto

```
Sistema-de-Reserva-de-Assentos-de-Cinema/
├── tests/
│   └── test_cinema.py          # Testes automatizados
├── main.py                      # Arquivo principal de execução
├── pyproject.toml               # Configuração do projeto
├── uv.lock                      # Lock de dependências
├── .gitignore                   # Arquivos ignorados pelo Git
├── LICENSE                      # Licença do projeto
└── README.md                    # Este arquivo
```

---

## 🎯 Funcionalidades do Sistema

1. **Visualizar Mapa da Sala** - Veja todos os assentos disponíveis
2. **Reservar Assentos** - Selecione e reserve os assentos desejados
3. **Validação de Ocupação** - Sistema valida se os assentos já foram reservados
4. **Calcular Receita** - Total arrecadado com as reservas
5. **Cancelar Reserva** - Remova reservas existentes (se implementado)

---

## 🐛 Solução de Problemas

### Problema: "command not found: python"
**Solução:** Certifique-se de que Python está instalado e adicione ao PATH do seu sistema. Tente `python3` ao invés de `python`.

### Problema: "ModuleNotFoundError"
**Solução:** Certifique-se de que todas as dependências foram instaladas corretamente com `uv sync`.

### Problema: "Permission denied" ao executar scripts
**Solução (Linux/Mac):**
```bash
chmod +x main.py
./main.py
```

---

## 📚 Recursos Úteis

- [Documentação do Python](https://docs.python.org/3/)
- [Guia do uv](https://docs.astral.sh/uv/)
- [Tutorial de Git](https://git-scm.com/doc)

---

### 📫 Como me encontrar:
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/0samuelog/)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:0samuel.a021@gmail.com)
