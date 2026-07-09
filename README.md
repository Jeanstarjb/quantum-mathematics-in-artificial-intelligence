# Quantum Mathematics in Artificial Intelligence

## Overview

This repository hosts a Python/PyTorch implementation of the core concepts discussed in the paper [Quantum Mathematics in Artificial Intelligence](https://arxiv.org/pdf/2101.04255v6) by Dominic Widdows, Kirsty Kitto, and Trevor Cohen. The paper explores the intersection of quantum mathematics and artificial intelligence (AI), with a particular focus on vector space models and their applications in natural language processing (NLP), automated reasoning, and more.

The provided code aims to make these abstract mathematical concepts concrete by implementing key operations and demonstrating their utility in AI tasks. This repository is intended for researchers, students, and practitioners interested in learning how quantum-inspired mathematical techniques can be utilized within AI workflows.

---

## Core Concepts

The paper highlights the mathematical parallels between quantum mechanics and AI, particularly in the context of vector spaces. Below are some of the core concepts addressed, along with their relevance:

1. **Vector Spaces**:
   - Central to both quantum mechanics and AI, vector spaces are used to represent data points, such as word embeddings in NLP.

2. **Scalar Products and Orthogonal Projection**:
   - Scalar (dot) products measure similarity between vectors, while orthogonal projection is used for negation and filtering irrelevant information.

3. **Tensor Products**:
   - Tensor products model complex systems by combining multiple vector spaces, commonly used in neural networks and quantum interactions.

4. **Density Matrices and Positive Operators**:
   - These mathematical tools are useful for encoding probabilities and modeling uncertainty, with applications in knowledge representation.

5. **Applications**:
   - The paper discusses various applications, including:
     - Information Retrieval
     - Semantic Composition
     - Word-Sense Disambiguation
     - Knowledge Base Inference

The overlap between quantum mathematics and AI opens up opportunities for leveraging quantum hardware and designing novel AI algorithms.

---

## Repository Contents

This repository contains Python code (using PyTorch) that implements the mathematical operations and concepts discussed in the paper. Below is a breakdown of the key components:

### 1. **Vector Space Operations**
   - Implements basic vector space operations like scalar products, orthogonal projections, and subspace calculations.
   - Demonstrates these operations in the context of NLP (e.g., similarity between word embeddings).

### 2. **Tensor Products**
   - Implements tensor product operations to combine multiple vector spaces.
   - Illustrates their application in semantic composition and modeling interactions between entities.

### 3. **Density Matrices and Positive Operators**
   - Provides tools for constructing and manipulating density matrices.
   - Demonstrates their use in encoding probabilities and handling uncertainty in AI models.

### 4. **Applications**
   - Includes examples of:
     - Information retrieval using vector space models.
     - Word-sense disambiguation with orthogonal projections.
     - Semantic composition with tensor products.
     - Knowledge inference using density matrices.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- PyTorch 1.10 or higher
- NumPy

To install the dependencies, run:
```bash
pip install -r requirements.txt
```

### Running the Examples
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/quantum-math-ai.git
   cd quantum-math-ai
   ```

2. Run the example scripts:
   ```bash
   python examples/vector_space_operations.py
   python examples/tensor_products.py
   ```

Each script includes detailed comments to explain the implementation and its connection to the concepts discussed in the paper.

---

## How to Use

### Core Modules
- `vector_operations.py`: Contains functions for vector space operations (e.g., scalar product, projection).
- `tensor_operations.py`: Implements tensor product calculations.
- `density_matrices.py`: Provides tools for constructing and applying density matrices.

### Example Workflows
- **Information Retrieval**: Demonstrates how scalar products can be used to rank documents based on query relevance.
- **Word-Sense Disambiguation**: Uses orthogonal projection to separate word senses in a vector space.
- **Semantic Composition**: Combines word embeddings using tensor products to form phrase-level representations.

---

## Contributions

Contributions are welcome! If you have ideas for extending this implementation or improving the existing code, feel free to open an issue or submit a pull request.

---

## References

1. Dominic Widdows, Kirsty Kitto, Trevor Cohen. "Quantum Mathematics in Artificial Intelligence." [arXiv:2101.04255v6](https://arxiv.org/pdf/2101.04255v6)
2. PyTorch Documentation: [https://pytorch.org](https://pytorch.org)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.