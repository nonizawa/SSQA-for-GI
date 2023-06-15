# SSQA-for-GI (Stochastic simulated quantum annelinag for graph isomophism)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

SSQA-for-GI is a Python project that utilizes Structured Synthesizer Quality Assessment (SSQA) for Graph Isomorphism (GI) tasks. The project aims to develop a robust algorithm to assess the quality of synthesizers, by evaluating their performance in solving Graph Isomorphism problems.

The Graph Isomorphism problem is a classical computational problem in which two given graphs, G and H, are determined to be isomorphic if there exists a bijective mapping between their vertex sets that preserves adjacency.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have Python 3.6 or later installed on your machine. You can download it from [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/nonizawa/SSQA-for-GI.git
    cd SSQA-for-GI
    ```

2. The dataset used for evaluating graphs is located at `./graph/`. Make sure that it's in place before running the program.

### Running

To run the main script, simply execute the `sa.py` file using Python:

```sh
python sa.py
```

You can modify the script to perform specific tests or evaluations by editing the parameters within the script.

## Structure

- `./graph/`: This directory contains the dataset of graphs used for evaluation.
- `sa.py`: This is the main Python script that runs the SSQA for GI algorithm.
- `requirements.txt`: This file contains the Python dependencies necessary for the project.
- `LICENSE`: The MIT License file for this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions, issues, or inquiries, feel free to create an issue in the repository or contact the repository owner [@nonizawa](https://github.com/nonizawa).

--- 

Please note that this README.md is a general guide, and the specifics of the project may vary. It's important to review the repository for the most up-to-date information.