import json
import os


class Cinema:
    """Sistema de Reserva de Assentos de Cinema."""

    def __init__(self, num_seats=8, data_file='seats.json'):
        """Inicializa o cinema com um número de assentos e arquivo de dados."""
        self.num_seats = num_seats
        self.data_file = data_file
        self.seats = self.carregar_assentos()

    def carregar_assentos(self):
        """Carrega os dados dos assentos do arquivo ou inicializa todos como livres."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return [0] * self.num_seats

    def salvar_assentos(self):
        """Salva o estado atual dos assentos no arquivo."""
        with open(self.data_file, 'w') as f:
            json.dump(self.seats, f)

    def mostrar_assentos(self):
        """Exibe o status atual de todos os assentos."""
        print("- Cadeiras:")
        for i in range(len(self.seats)):
            status = "L" if self.seats[i] == 0 else "O"
            print(f"[{i + 1}: {status}] ", end=" ")
        print()

    def reservar_assento(self, numero_assento):
        """Reserva um assento se estiver livre. Retorna True se bem-sucedido."""
        if 1 <= numero_assento <= self.num_seats:
            pos = numero_assento - 1
            if self.seats[pos] == 0:
                self.seats[pos] = 1
                self.salvar_assentos()
                print(f"Cadeira {numero_assento} reservada com sucesso!")
                return True
            else:
                print("Essa cadeira já está reservada, selecione outra.")
                return False
        else:
            print("Número da cadeira inválido!")
            return False

    def cancelar_reserva(self, numero_assento):
        """Cancela a reserva de um assento se estiver ocupado. Retorna True se bem-sucedido."""
        if 1 <= numero_assento <= self.num_seats:
            pos = numero_assento - 1
            if self.seats[pos] == 1:
                self.seats[pos] = 0
                self.salvar_assentos()
                print(f"Reserva da cadeira {numero_assento} cancelada com sucesso!")
                return True
            else:
                print("Essa cadeira não está ocupada.")
                return False
        else:
            print("Número da cadeira inválido!")
            return False

    def mostrar_livres(self):
        """Exibe todos os assentos livres."""
        livres = [i + 1 for i, s in enumerate(self.seats) if s == 0]
        print("- Cadeiras livres: ", end=" ")
        print(" ".join(map(str, livres)))
        if not livres:
            print("Nenhuma cadeira está livre!")
        else:
            print(f"{len(livres)} cadeiras estão livres!")

    def calcular_resumo(self):
        """Exibe um resumo do total, livres e ocupados."""
        livres = sum(1 for s in self.seats if s == 0)
        ocupadas = self.num_seats - livres
        print("- Resumo:")
        print()
        print(f"Total de cadeiras: {self.num_seats}")
        print("-----------------------")
        print(f"Livres: {livres} | Ocupadas: {ocupadas}")
        print()


def menu():
    print("\n===================")
    print("SISTEMA - CINEMA")
    print("===================\n")
    print("1 - Mostrar cadeiras")
    print("2 - Reservar cadeira")
    print("3 - Cancelar reserva")
    print("4 - Mostrar livres")
    print("5 - Calcular resumo")
    print("0 - Sair\n")


def main():
    cinema = Cinema()
    while True:
        menu()
        try:
            opcao = int(input("- Escolha uma opção: "))
            print()
        except ValueError:
            print("Insira apenas números!")
            continue

        if opcao == 1:
            cinema.mostrar_assentos()
        elif opcao == 2:
            try:
                assento = int(input(f"- Insira o número da cadeira (1 a {cinema.num_seats}): "))
                cinema.reservar_assento(assento)
            except ValueError:
                print("Insira apenas números!")
        elif opcao == 3:
            try:
                assento = int(input(f"- Insira o número da cadeira (1 a {cinema.num_seats}): "))
                cinema.cancelar_reserva(assento)
            except ValueError:
                print("Insira apenas números!")
        elif opcao == 4:
            cinema.mostrar_livres()
        elif opcao == 5:
            cinema.calcular_resumo()
        elif opcao == 0:
            print("Desligando o sistema...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
