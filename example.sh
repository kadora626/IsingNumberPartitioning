#!/bin/bash

# Make a qubo from .txt file
python txt2qubo.py -t input.txt -o partion.qubo

# Execute qbsolv
./qbsolv -i partion.qubo -o partion.qbout -v1 -n 8

# Output result of problem
python result.py -i input.txt -s partion.qbout
