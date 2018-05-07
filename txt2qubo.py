import argparse
import os

def txt2_qubo(qubo_out, text_in):
    index_to_number = {}
    number_to_index = {}
    idx = 0
    with open(text_in, "r") as text:
        for line in text:
            if line[0] == 'c' or line[0] == '#':
                # skip the comment lines
                continue

            # in each line, there is a list of numbers.
            numbers = int(line.strip('\n'))

            # each number has an integer label, so we record the mapping in both
            # directions
            number_to_index[numbers] = idx
            index_to_number[idx] = numbers
            idx += 1
    # we need some information in advance for the qubo, specifically the number of nodes,
    # the number of couplers and sum of numbers
    num_nodes = len(index_to_number)
    num_couplers = int(num_nodes * (num_nodes - 1 ) / 2)
    sum_numbers = 0
    for num in range(len(index_to_number)):
        sum_numbers += index_to_number[num]

    # now time to write the qubo
    # nodes first
    with open(qubo_out, "w") as qubo:
        qubo.write("c" + "\n")
        qubo.write("c  this qubo was created by txt2qubo.py for number separate encoding" + "\n")
        qubo.write("c" + "\n")
        qubo.write("p  qubo  0  {} {} {}\n".format(num_nodes, num_nodes, num_couplers))

        for id in range(len(index_to_number)):
            number = index_to_number[id]
            n = number * (sum_numbers - number) * (-1)
            qubo.write("c " + str(number) + "'s qubo \n")
            qubo.write("  " + str(id) + " " + str(id) + " " + str(n) +  " \n")
            # qubo.write("  " + str(st * 4 + 1) + " " + str(st * 4 + 1) + " -1 " + "\n")
            # qubo.write("  " + str(st * 4 + 2) + " " + str(st * 4 + 2) + " -1 " + "\n")
            # qubo.write("  " + str(st * 4 + 3) + " " + str(st * 4 + 3) + " -1 " + "\n")

        qubo.write("c" + "\n")
        qubo.write("c  Couplers " + "\n")
        qubo.write("c" + "\n")

        for idxi in range(len(index_to_number) - 1):
            for idxj in range(idxi + 1, len(index_to_number)):
                numberi = index_to_number[idxi]
                numberj = index_to_number[idxj]
                n = numberi * numberj * 2
                qubo.write("  " + str(idxi) + "   " + str(idxj) + " " + str(n) + " \n")
            # qubo.write("c " + state + "   " + str(len(neighbors)) + " neighbors  " +
            #            str(len(neighbors) * 4) + " external couplers\n")
            # qubo.write("  " + str(st * 4) + " " + str(st * 4 + 1) + " 2 " + "\n")
            #     qubo.write("  " + str(st * 4 + 3) + " " + str(ext_coup * 4 + 3) + " 1 " + "\n")
            

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read txt files and create a qubo number patitioning problem.')
    parser.add_argument("-t", "--text", help="Input txt file ", required=True)
    parser.add_argument("-o", "--qubo", type=str, help="output .qubo file", required="True")
    parser.add_argument("-v", "--verbosity", action="store_true", help="Verbosity level", default=0)

    args = parser.parse_args()

    txt_in = args.text
    qubo_out = args.qubo
    txt2_qubo(qubo_out, txt_in)
