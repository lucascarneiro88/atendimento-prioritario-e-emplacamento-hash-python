# Exigencia de código 1 de 7
# Implementar lista encadeada simples para pacientes

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
# Implementar função para add pacientes sem prioridade à lista
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
# Implementar função para add pacientes com prioridade a lista
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
# Implementar função para inserir pacientes/cartão/nodo
# Solicita a cor, atruibui número automaticamente, cria nodo(Paciente) e chama a inserção apropriada

def  insert_patient(self):
    color = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
    if color not in [ 'A', 'V']:
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



  
    

   