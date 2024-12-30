import sys
from PyQt5.QtWidgets import QApplication
from clipboard_logic import ClipboardLogic
from clipboardgui import ClipboardGUI
from error_handling import handle_exception, ClipboardManagerError, create_log_file_if_not_exists


def main():
    try:
        # Ensure the log file exists
        create_log_file_if_not_exists()
        print("Log file initialized successfully.")

        # Initialize the PyQt application
        app = QApplication(sys.argv)

        # Initialize the logic for managing clipboard data
        clipboard_logic = ClipboardLogic()
        print("ClipboardLogic initialized.")

        try:
            clipboard_logic.load_from_json()  # Load clipboard history
            print("Clipboard history loaded successfully.")
        except ClipboardManagerError as e:
            handle_exception(e, "Failed to load clipboard history. Starting with an empty list.")

        # Initialize the GUI and pass the logic to it
        clipboard_gui = ClipboardGUI(clipboard_logic)
        clipboard_gui.update_list()  # Populate the GUI with saved clipboard history
        print("ClipboardGUI initialized and list updated.")

        # Show the GUI
        clipboard_gui.show()
        print("GUI displayed. Application running...")

        # Run the application loop
        sys.exit(app.exec_())

    except Exception as e:
        # Catch any unexpected errors and log them
        handle_exception(e, "An unexpected error occurred. Please check the log file for details.")


if __name__ == "__main__":
    main()

