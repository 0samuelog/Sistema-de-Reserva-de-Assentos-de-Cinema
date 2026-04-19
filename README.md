# Sistema de Reserva de Assentos de Cinema

Um aplicativo simples de console em Python para gerenciar reservas de assentos em um cinema.

## Funcionalidades

- Exibir assentos disponíveis e ocupados
- Reservar um assento
- Cancelar uma reserva
- Mostrar assentos livres
- Calcular resumo dos assentos
- Armazenamento persistente dos dados dos assentos usando JSON

## Instalação

1. Certifique-se de ter o Python 3.14+ instalado.
2. Clone o repositório.
3. Instale as dependências: `uv sync`
4. Para desenvolvimento: `uv sync --group dev`

## Como Executar

Execute o aplicativo: `uv run python main.py`

## Testes

Execute os testes: `uv run pytest`

## Estrutura do Projeto

- `main.py`: Código principal do aplicativo com a classe Cinema
- `tests/`: Testes unitários
- `seats.json`: Dados persistentes dos assentos (criado automaticamente)

## Tecnologias Utilizadas

- Python 3.14+
- JSON para persistência de dados
- Pytest para testes

## Licença

Este projeto é de código aberto. Sinta-se à vontade para contribuir!
