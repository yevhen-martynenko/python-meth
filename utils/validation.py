import inspect
from exceptions.InvalidDataErrors import InvalidDataError


def validate_range(range_: list[int | float]):
    if range_[0] >= range_[1]:
        raise InvalidDataError("Invalid range: Start value should be less than end value", range_)


def validate_signs(signs: str):
    allowed_signs = "+-*/"
    if not all(char in allowed_signs for char in signs):
        raise InvalidDataError(f"Invalid signs: '{signs}'. Allowed signs are any combination of: {allowed_signs}", signs)


def validate_positive_integer(value: int):
    frame = inspect.currentframe().f_back
    source_line = inspect.getframeinfo(frame).code_context[0]
    start = source_line.find('(') + 1
    end = source_line.find(')')
    arg_name = source_line[start:end].strip()

    if value <= 0:
        raise InvalidDataError(f"{arg_name} must be greater than zero", value)


def validate_all_inputs(args):
    validate_positive_integer(args.problems)
    validate_range(args.range_)
    validate_signs(args.sign)
    validate_positive_integer(args.operations)
    validate_positive_integer(args.time_limit)

