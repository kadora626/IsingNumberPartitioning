#!/bin/bash

# Make a qubo from .txt file
python txt2qubo.py -t input.txt -o partition.qubo

# Execute qbsolv
qbsolv -i partition.qubo -o partition.qbout -v1 -n 8

# Output result of problem
python result.py -i input.txt -s partition.qbout
