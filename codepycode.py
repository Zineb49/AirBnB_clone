def calculate_square_area(side_length):
    """
    Calculate the area of a square.
    Parameters:
    - side_length (float or int): The length of one side of the square.
    Returns:
    float or int: The area of the square.
    """
    area = side_length ** 2
    return area


if __name__ == "__main__":
    # Example usage
    side_length = 5
    square_area = calculate_square_area(side_length)
    print(f"The area of a square {side_length} is: {square_area}")
