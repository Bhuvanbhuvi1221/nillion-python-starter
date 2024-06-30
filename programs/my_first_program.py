
from nada_dsl import *

def nada_main():
    # Define two parties: Alice and Bob
    alice = Party(name="Alice")
    bob = Party(name="Bob")

    # Define two secret integers: x and y
    x = SecretInteger(Input(name="x", party=alice))
    y = SecretInteger(Input(name="y", party=bob))

    # Compute the product of x and y securely
    product = x * y

    # Compute the square of the product
    square = product * product

    # Return the square as the output
    return [Output(square, "square_xy", alice)]