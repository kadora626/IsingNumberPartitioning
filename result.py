def print_result(p_input, qsolv_out):
    res_a = []
    res_b = []
    enegy = 0
    index_to_number = {}
    qbsolv = open(qsolv_out, "r")
    lines = qbsolv.read()
    lines = lines.split('\n')
    qbits = lines[0].split()
    nqbits = int(qbits[0])
    result_bits = lines[1]
    idx = 0
    with open(p_input, "r") as text:
        for line in text:
            if line[0] == 'c' or line[0] == '#':
                continue

            number = int(line.strip('\n'))
            index_to_number[idx] = number
            idx += 1
            enegy += number * number

    for i in range(nqbits-1):
        for j in range(i + 1 ,nqbits):
            enegy += 2 * index_to_number[i] * index_to_number[j]

    sol_enegy_str = lines[2].split()
    sol_enegy = 4.0 * float(sol_enegy_str[0])
    if sol_enegy + float(enegy) != 0:
        print("This set of numbers cannot partition.")
        return

    for i in range(nqbits):
        if result_bits[i] == '1':
            res_a.append(index_to_number[i])
        else:
            res_b.append(index_to_number[i])

    print("Partitioning result\n")
    print("GroupA:" + str(res_a) + "\n")
    print("GroupB:" + str(res_b) + "\n")


if __name__ == "__main__":
    import argparse
    import os
    parser = argparse.ArgumentParser(description='Read .qubo.out files and print partition result')
    parser.add_argument("-i", "--input", help="Problem input file", required=True)
    parser.add_argument("-s", "--sol", help="Input solution file from qbsolv ", required=True)
    parser.add_argument("-v", "--verbosity", action="store_true", help="Verbosity level", default=0)

    args = parser.parse_args()

    p_input = args.input
    qsolv_out = args.sol
    print_result(p_input, qsolv_out)
