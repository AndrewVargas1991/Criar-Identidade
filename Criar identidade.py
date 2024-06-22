import random
import datetime

with open(r'listas\Lista de nomes.txt', 'r') as arquivo_nomes:
    nomes = arquivo_nomes.read().split()

with open(r'listas\Lista de sobrenomes.txt', 'r') as arquivo_sobrenomes:
    sobrenomes = arquivo_sobrenomes.read().split()

with open(r'listas\Lista de emails.txt', 'r') as arquivo_emails:
    emails = arquivo_emails.read().split()

nome = random.choice(nomes)
sobrenome = random.choice(sobrenomes)
email = f'{nome}{sobrenome}@{random.choice(emails)}.com'.lower()
idade = random.randint(18, 100)
ano = 2024 - idade
dia_do_ano = random.randint(1, 365)
data_nascimento = datetime.date(ano, 1, 1) + datetime.timedelta(days=dia_do_ano - 1)

print(f'Nome: {nome}')
print(f'Sobrenome: {sobrenome}')
print(f'Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}')
print(f'Idade: {idade}')
print(f'Email: {email}')

input('\nAperte ENTER para sair...')
