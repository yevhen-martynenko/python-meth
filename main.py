import math
import argparse
from random import randrange, choice, uniform

from utils import configure_parser


"""
powers of 0,1,2,3,4,5
square roots
1,2,3,4 roots

negative numbers range
() in exercises

translate number in different number systems 16, 8, 2 hex oct 

fractions problems

different exercises 

log

factorial

equations with x
equations with x, y, z 

matrix 

SUM
"""



def create_problem(range_: list[int, float], sign: str, operations: int, precision: int) -> str:
    """
    Generate a math problem with the given range, sign, number of operations, and precision.

    Args:
        range_ (list[int, float]): Start and end values of the number range.
        sign (str): Allowed mathematical operators as a string ("+-*/" or "+-" or "+", etc)
        operations (int): Number of operations to include in the problem.
        precision (int): Decimal precision for float numbers.

    Returns:
        str: A string representation of the math problem.
    """


    def generate_number() -> str:
        """Generate a number based on the range type."""
        if isinstance(range_[0], int):
            return str(randrange(*range_))
        elif isinstance(range_[0], float):
            return str(round(uniform(*range_), precision))


    problem: str = generate_number() + " "

    for _ in range(operations):
        operation: str = choice(sign)
        number: str = generate_number()
        problem += f"{operation} {number} "

    return problem


def main():
    parser = configure_parser()
    args = parser.parse_args()

    if args.decimal == True and isinstance(args.range_[0], int):
        for _ in range(len(args.range_)):
            args.range_[_] = float(args.range_[_])

    print(args)
    print(type(args.range_[0]))

    for i in range(args.problems):
        problem = create_problem(args.range_, args.sign, args.operations, args.precision)
        print(problem)
        x = int(input("Answer: "))
        print(x)
        print(eval(problem))
        assert x == eval(problem)


if __name__ == "__main__":
    main()

