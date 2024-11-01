class InvalidDataError(Exception):
    """
    Exception raised when the input data is not valid.

    Attributes:
        message (str): Explanation of the error.
        invalid_data_option (str): Specific data or option that caused the error.
    """
    
    def __init__(self, message, invalid_data_option=None):
        super().__init__(message)
        self.invalid_data_option = invalid_data_option

