lista = [[], [], []]
cont = 0
while True:
    lista[0].append(input('Nome: '))
    nota1 = float(input(f'Nota 1: '))
    nota2 = float(input(f'Nota 2: '))
    media = (nota1 + nota2) / 2
    lista[1].append(media)
    lista[2].append([nota1, nota2])
    cont += 1
    sn = input('Você quer continuar? [S/N] ').strip().lower()[0]
    if sn == 'n':
        break
print('-='*30)

print(f"{'N°.':<4}{' NOME':<10}{'MÉDIA':>8}")
for i, v in enumerate(lista[0]):
    print(f'{i:<4}{lista[0][i].title():<18}{lista[1][i]:.1f}')
print('-='*30)

while True:
    chamada = int(input('Mostrar notas de qual aluno? [999 para Interromper] '))
    if chamada == 999:
        break
    print(f'As notas de {lista[0][chamada]} são: {lista[2][chamada]}')
    print('-='*30)
print("<<<< Volte sempre! >>>>")
