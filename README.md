# IsingNumberPartitioning
This is the example of solving number partitioning problem using qbsolv.

# Example
To run example, you only execute `example.sh`.
```bash
$ ./example.sh
```

# Requrements
To run example, you have to install [qbsolv](https://github.com/dwavesystems/qbsolv) in your PATH.

# Files
input.txt: Input of the number partitioning problem. This example partition numbers which are written in this file. Input file has one number per line.

partition.qubo: Qubo file which is translated from input of the problem. txt2qubo.py translates input.txt to this qubo file.

partition.qbout: Output file of qbsolv execution. result.py prints problem result based on this file.
