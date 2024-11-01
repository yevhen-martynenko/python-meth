import math
import argparse
from random import randrange, choice, uniform

from utils import configure_parser, validate_all_inputs
from exceptions import MistakeLimitReachedError


def create_problem(
    range_: list[int | float], 
    sign: str, 
    operations: int, 
    precision: int
) -> str:
    """
    Generate a math problem with the given range, sign, number of operations, and precision.

    Args:
        range_      (list[int | float])  Start and end values of the number range.
        sign        (str)               Allowed mathematical operators as a string ("+-*/" or "+-" or "+", etc)
        operations  (int)               Number of operations to include in the problem.
        precision   (int)               Decimal precision for float numbers.

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

        if float(number) == 0 and operation == "/":
            operation = "+"

        problem += f"{operation} {number} "

    return problem


def check_answer(
    user_answer: int | float, 
    correct_answer: int | float, 
    precision: int, 
    quiet: bool, 
    verbose: bool
) -> tuple[str, bool]:
    """
    Check the user's answer and return string message based on the mode (quiet, verbose, default).

    Args:
        user_answer     (int | float)   The answer provided by the user.
        correct_answer  (int | float)   The correct answer to the problem.
        precision       (int)           Decimal precision for comprasion.
        quiet           (bool)          Quiet mode for minimal output.
        verbose         (bool)          Verbose mode for detailed output.

    Returns:
        tuple[str, bool]: A tuple containing the result message and a boolean value of correctness.
    """
    
    # TODO check if -d or -f is used

    correct_answer: float = round(correct_answer, precision)
    user_answer: float = round(user_answer, precision) 
    is_correct: bool = correct_answer == user_answer
    result: str

    if quiet:
        result = "Correct" if is_correct else f"Incorrect, the answer is: {correct_answer}"
    elif verbose:
        # TODO: Implement verbose output logic
        result = "verbose output"
    else:
        result = f"{user_answer} == {correct_answer} = {is_correct}"

    return result, is_correct


def main():
    parser = configure_parser()
    args = parser.parse_args()

    validate_all_inputs(args)

    if args.decimal == False and isinstance(args.range_[0], float):
        for _ in range(len(args.range_)):
            args.range_[_] = int(args.range_[_])
    
    max_mistakes: int | None = args.max_mistakes
    if args.exit_on_mistake and max_mistakes is None:
        max_mistakes = 1

    print(args)

    for i in range(args.problems):
        problem = create_problem(
            range_ = args.range_, 
            sign = args.sign, 
            operations = args.operations, 
            precision = args.precision
        )
        print(problem)
 
        # TODO check -d -f
        correct_answer = eval(problem)

        while True:
            user_answer = float(input("Your answer: "))
        
            result_message, is_correct = check_answer(
                user_answer = user_answer, 
                correct_answer = correct_answer, 
                precision = args.precision, 
                quiet = args.quiet, 
                verbose = args.verbose
            )

            if is_correct:
                print(result_message)
                break

            if args.exit_on_mistake:
                if max_mistakes > 1:
                    max_mistakes -= 1
                    print(f"Wrong. You have {max_mistakes} attempts left")
                else:
                    correct_answer = round(correct_answer, args.precision)
                    raise MistakeLimitReachedError(correct_answer)


if __name__ == "__main__":
    main()

