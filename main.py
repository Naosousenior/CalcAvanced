import tests as t
import os
import help as hp

cls = lambda : os.system("cls") or None


print('Welcome to my favorite calculator')
print('Here you can make advanced calcs')

print('Type "help" to access the menu help')

while True:

    command = input('>> ')

    if command == 'exit':
        break

    if command == 'clear':
        cls()
        continue

    if command == 'help':
        hp.help()
        continue

    t.test_evaluate(command)