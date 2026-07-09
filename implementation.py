import numpy as np
import torch

# Define a function to compute the tensor product of two vectors
def tensor_product(vec1, vec2):
    """
    Compute the tensor product of two vectors.
    Args:
        vec1 (torch.Tensor): First vector.
        vec2 (torch.Tensor): Second vector.
    Returns:
        torch.Tensor: Tensor product of vec1 and vec2.
    """
    return torch.ger(vec1, vec2)

# Define a function to compute the density matrix
def density_matrix(vec):
    """
    Compute the density matrix of a vector.
    Args:
        vec (torch.Tensor): Input vector.
    Returns:
        torch.Tensor: Density matrix.
    """
    return torch.outer(vec, vec)

# Define a function for orthogonal projection
def orthogonal_projection(vec, basis):
    """
    Project a vector onto a subspace defined by a basis.
    Args:
        vec (torch.Tensor): Input vector.
        basis (torch.Tensor): Basis vectors (columns of the matrix).
    Returns:
        torch.Tensor: Projected vector.
    """
    basis_t = torch.transpose(basis, 0, 1)
    projection_matrix = torch.matmul(basis, torch.linalg.pinv(basis_t @ basis) @ basis_t)
    return torch.matmul(projection_matrix, vec)

# Define a function for scalar product
def scalar_product(vec1, vec2):
    """
    Compute the scalar product of two vectors.
    Args:
        vec1 (torch.Tensor): First vector.
        vec2 (torch.Tensor): Second vector.
    Returns:
        float: Scalar product of vec1 and vec2.
    """
    return torch.dot(vec1, vec2).item()

# Define a function for negation (orthogonal complement)
def negation(vec, basis):
    """
    Compute the orthogonal complement of a vector with respect to a basis.
    Args:
        vec (torch.Tensor): Input vector.
        basis (torch.Tensor): Basis vectors (columns of the matrix).
    Returns:
        torch.Tensor: Orthogonal complement vector.
    """
    projection = orthogonal_projection(vec, basis)
    return vec - projection

if __name__ == '__main__':
    # Dummy data for testing
    vec1 = torch.tensor([1.0, 2.0, 3.0])
    vec2 = torch.tensor([4.0, 5.0, 6.0])
    basis = torch.tensor([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    # Compute tensor product
    tp = tensor_product(vec1, vec2)
    print("Tensor Product:\n", tp)

    # Compute density matrix
    dm = density_matrix(vec1)
    print("Density Matrix:\n", dm)

    # Compute orthogonal projection
    proj = orthogonal_projection(vec1, basis)
    print("Orthogonal Projection:\n", proj)

    # Compute scalar product
    sp = scalar_product(vec1, vec2)
    print("Scalar Product:", sp)

    # Compute negation (orthogonal complement)
    neg = negation(vec1, basis)
    print("Negation (Orthogonal Complement):\n", neg)