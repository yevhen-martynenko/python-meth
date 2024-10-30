import argparse


def configure_parser():
    parser = argparse.ArgumentParser(
        prog="meth",  # MEntal MAth
        description="A simple terminal program for mental math."
    )

    parser.add_argument(
        "problems", 
        type=int,
        nargs="?",
        default=1, 
        help="Number of math problems to solve (default: 1)"
    )
    
    verbosity_group = parser.add_argument_group("Verbosity level")
    verbosity = verbosity_group.add_mutually_exclusive_group()
    verbosity.add_argument(
        "-v", "--verbose", 
        action="store_true",
        help="Enable verbose output"
    )
    verbosity.add_argument(
        "-q", "--quiet", 
        action="store_true",
        help="Suppress output (even results)"
    )

    number_range = parser.add_argument_group("Number range arguments")
    number_range.add_argument(
        "-r", "--range_", 
        type=float, 
        nargs=2, 
        metavar=("START", "END"), 
        default=[0, 10], 
        help="Number range: -r START END (default: [0, 10])"
    )
    number_range.add_argument(
        "-p", "--precision",
        type=int,
        default=2,
        choices=range(1, 6),
        help="Number of decimal places for decimal numbers (1 to 5, default: 2)"
    ) 
    
    decimal_group = parser.add_argument_group("Decimal arguments")
    decimal = decimal_group.add_mutually_exclusive_group()
    decimal.add_argument(
        "-d", "--decimal", 
        action="store_true", 
        help="Use decimal numbers in the range (default: integer)"
    )
    decimal.add_argument(
        "-f", "--fractions",
        action="store_true",
        help="Use fractions in the range"
    )

    parser.add_argument(
        "-s", "--sign", 
        type=str, 
        default="+-*/", 
        help="Mathematical signs for operations (example: -s +-*/)"
    )
    parser.add_argument(
        "-o", "--operations", 
        type=int,
        default=1, 
        help="The number of operations per problem (e.g., 1 for A + B, 2 for A + B - C)"
    )
    parser.add_argument(
        "-b", "--brackets", 
        action="store_true", 
        help="Allow operations within brackets (e.g., (A + B) * C)"
    )
   
    error_handling = parser.add_argument_group("Error handling arguments")
    error_handling.add_argument(
        "-g", "--go-on-error",
        action="store_true",
        help="Continue solving after an error, instead of exiting"
    )
    error_handling.add_argument(
        "-e", "--max-errors",
        type=int,
        help="Maximum number of errors before exiting (requires --go-on-error)"
    )

    parser.add_argument(
        "-t", "--time-limit",
        type=int,
        default=30,
        help="Time limit for solving problems in seconds (default: 30)"
    )


    return parser

