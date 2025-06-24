# Sistemas de Triagem Hospitalar e Emplacamento de Veículos em Python


## Visão Geral

Este repositório contém dois projetos em Python desenvolvidos para uma tarefa da faculdade com foco em estruturas de dados:

1. **Sistema de Triagem Hospitalar**  
   Implementação de uma fila de prioridade usando lista encadeada simples para gerenciar a triagem de pacientes com base na cor e número do cartão.

2. **Tabela Hash para Emplacamento de Veículos**  
   Implementação de uma tabela hash com tratamento de colisões por encadeamento separado usando listas encadeadas simples para mapear estados de registro de veículos com base no último número da placa.

---

# Sistema de Triagem Hospitalar

### Exigência de código 1 de 7
- Implementar lista encadeada simples.
- O Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo paciente.
- A lista é não circular ( o último elemento aponta para None).

### Cartão / Paciente / Nodo

```python
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
  ```


- Aqui temos a definição do *Nodo* com três atributos obrigatórios e o inicio da *ListaEncadeada* com o ponteiro para a cabeça(head).

- **Nodo(nó):** Representa um elemento (Paciente) da lista, em estrutura de dados um *nodo* é uma célula de uma estrutura encadeada que guarda um valor e também uma referência para outro(próximo)nodo.



### Exigência de código 2 de 7
- Implementar método para adicionar pacientes sem prioridade à lista.
- O paciente deve ser inserido no **final da lista**.

### Função `insertWithoutPriority`

```python
def insertWithoutPriority(self, patient):
    if not self.head:
        self.head = patient
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = patient
```