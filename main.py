from sys import argv

script, filename = argv

with open(filename, 'r') as mol2_file:

    mol2_lines = (mol2_file.readlines())

    first_item = mol2_lines.index('@<TRIPOS>ATOM\n')
    last_item = mol2_lines.index('@<TRIPOS>BOND\n')

    charges = {}
    for line in mol2_lines[first_item + 1:last_item]:
        elements = line.split()
        print(elements[1], elements[-1])

        charges[elements[1]] = float(elements[-1])

    print(charges)

print(charges['H5'])

