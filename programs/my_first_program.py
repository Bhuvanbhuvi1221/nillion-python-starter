
from nada_dsl import *

def nada_main():
    # Define three parties: Alice, Bob, and Charlie
    alice = Party(name="Alice")
    bob = Party(name="Bob")
    charlie = Party(name="Charlie")

    # Define three secret integers: x, y, and z
    x = SecretInteger(Input(name="x", party=alice))
    y = SecretInteger(Input(name="y", party=bob))
    z = SecretInteger(Input(name="z", party=charlie))

    # Compute the product of x, y, and z securely
    product_xyz = x * y * z

    # Compute the sum of squares of x, y, and z securely
    square_x = x * x
    square_y = y * y
    square_z = z * z
    sum_squares = square_x + square_y + square_z

    # Compute the average of the sum of squares and the product of x, y, and z
    average = (sum_squares + product_xyz) / 3

    # Return the average as the output
    return [Output(average, "average_xyz", alice)]