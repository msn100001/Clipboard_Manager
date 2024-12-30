import logging
import os

# Log file configuration
LOG_FILE = "clipboard_manager_errors.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Custom Exceptions
class ClipboardManagerError(Exception):
    """Base exception for all clipboard manager errors."""
    pass


class FileOperationError(ClipboardManagerError):
    """Exception raised for errors during file operations."""
    def __init__(self, message="An error occurred during a file operation."):
        super().__init__(message)


class JSONDecodeError(ClipboardManagerError):
    """Exception raised for invalid JSON decoding."""
    def __init__(self, message="Failed to decode JSON data."):
        super().__init__(message)


class ClipboardOperationError(ClipboardManagerError):
    """Exception raised for clipboard-related operations."""
    def __init__(self, message="An error occurred during a clipboard operation."):
        super().__init__(message)


# Centralized exception handling
def handle_exception(exception, custom_message=None):
    """
    Centralized exception handler.
    Logs the error to a file and optionally displays a message.

    :param exception: The exception to handle.
    :param custom_message: A custom error message to log/display.
    """
    error_message = custom_message or str(exception)
    logging.error(error_message)
    print(f"Error: {error_message}")


def create_log_file_if_not_exists():
    """
    Ensure the log file exists. Creates an empty file if it doesn't exist.
    """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as log_file:
            log_file.write("")  # Create an empty log file

