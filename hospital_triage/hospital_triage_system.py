# Exigencia de código 1 de 7
# lista encadeada simples para pacientes
# Cartão / Paciente / Nodo
class Patient:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None  # Referência para o próximo paciente na lista

# Lista encadeada simples para pacientes
class PatientList:
    def __init__(self):
        self.head = None
        self.number_card_green = 1
        self.number_card_yellow = 201

    # Exigência de código 2 de 7
    # função para add pacientes sem prioridade à lista
    # inserir no final da lista
    def insert_without_priority(self, patient):
        if not self.head:
            self.head = patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = patient

    # Exigência de código 3 de 7
    # função para add pacientes com prioridade a lista
    # inserir após todos os nodos(pacientes) com prioridade( cartão amarelo - A ) mas sempre antes dos pacientes sem prioridade (cartão verde - V)
    def insert_with_priority(self, patient):
        if not self.head or self.head.color == 'V':
            patient.next = self.head
            self.head = patient
        else:
            current = self.head
            while current.next and current.next.color == 'A':
                current = current.next
            patient.next = current.next
            current.next = patient

    # Exigêmncia de código 4 de 7
    # função para inserir pacientes/cartão/nodo
    # Solicita a cor, atribui número automaticamente, cria nodo(Paciente) e chama a inserção apropriada
    def insert_patient(self):
        color = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
        if color not in ['A', 'V']:
            print("Cor inválida. Use 'A' para amarelo ou 'V' para verde.")
            return
        if color == 'A':
            patient = Patient(self.number_card_yellow, color)
            self.number_card_yellow += 1
            self.insert_with_priority(patient)
        else:
            patient = Patient(self.number_card_green, color)
            self.number_card_green += 1
            self.insert_without_priority(patient)
        print(f"Paciente {patient.number} com cartão {color} inserido na lista.")

    # Exigência de código 5 de 7
    # função para imprimir a lista de pacientes
    # Imprimir os cartões e seus respectivos números da cabeça(head) até o final
    def print_waiting_list(self):
        current = self.head
        if not current:
            print("A lista de espera está vazia.")
            return
        while current:
            print(f"Cartão {current.color} - Número {current.number}")
            current = current.next

    # Exigência de código 6 de 7
    # função para atender pacientes
    # Remove o primeiro paciente da lista e imprime o cartão e número do paciente atendido
    def attend_patient(self):
        if not self.head:
            print("Nenhum paciente na lista de espera")
            return
        patient = self.head
        self.head = self.head.next
        print(f"Atendendo paciente com cartão {patient.color} - Número {patient.number}")

# Exigência de código 7 de 7
# função principal para executar o sistema de triagem(MENU)
def main():
    patient_list = PatientList()
    while True:
        print("\nMENU")
        print("\nSistema de Triagem Hospitalar")
        print("1. Adicionar Paciente")
        print("2. Imprimir Lista de Espera")
        print("3. Atender Paciente")
        print("4. Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == '1':
            patient_list.insert_patient()
        elif choice == '2':
            patient_list.print_waiting_list()
        elif choice == '3':
            patient_list.attend_patient()
        elif choice == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
