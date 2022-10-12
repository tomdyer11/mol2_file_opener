from sys import argv

script, filename = argv

with open(filename, 'r') as mol2_file:

    mol2_lines = (mol2_file.readlines())

    first_item = mol2_lines.index('@<TRIPOS>ATOM\n')
    last_item = mol2_lines.index('@<TRIPOS>BOND\n')

    print(first_item)
    print(last_item)

    print(mol2_lines[first_item + 1:last_item])

    i = first_item + 1
    numbers = []

    element_line1 = (mol2_lines[first_item + 1])
    element1 = element_line1.split(' ')

    print(element1)

    print(element1[7])
    print(element1[44])

chargedic = {'element1[7]': 'element1[44]'}

chargedic[element_i[7]] = charge






