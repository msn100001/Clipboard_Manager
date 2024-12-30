
# Clipboard Manager

A Python-based clipboard management application with a graphical user interface (GUI) built using PyQt5. This application allows users to save, view, manage, and export/import clipboard history, including both text and images.

## Features

- **Save Clipboard Content**: Manually or automatically save text and image content from the clipboard.
- **View Clipboard History**: Display previously saved clipboard entries in an organized GUI.
- **Export/Import History**: Export clipboard history to a text file and import it back.
- **Delete Entries**: Delete individual or all entries from the clipboard history.
- **Auto-Save Feature**: Automatically save clipboard content periodically.
- **JSON Persistence**: Clipboard history is saved persistently using a JSON file.
- **Error Handling**: Comprehensive error handling with logs written to `clipboard_manager_errors.log`.

## Requirements

- Python 3.7+
- PyQt5
- Pillow (PIL for image handling)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd clipboard_manager
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python main.py
   ```

## Usage

- **Saving Clipboard Content**: Click "Save Clipboard" to manually save the current clipboard content.
- **Auto-Save**: Enable "Auto-Save" to periodically save clipboard content automatically.
- **Export**: Use the "Export List" button to save clipboard history to a text file.
- **Import**: Use the "Import List" button to load clipboard history from a file.
- **Delete Entries**: Right-click an entry in the list to delete it, or use the "Clear All" button to delete all entries.

## File Structure

```
clipboard_manager/
├── clipboard_logic.py        # Backend logic for managing clipboard history
├── clipboardgui.py           # PyQt5-based GUI implementation
├── error_handling.py         # Error handling and logging utilities
├── main.py                   # Entry point for the application
├── requirements.txt          # Python dependencies
├── clipboard_history.json    # JSON file for storing clipboard history (auto-generated)
├── clipboard_manager_errors.log  # Log file for error tracking (auto-generated)
```

## Error Logging

All errors are logged to `clipboard_manager_errors.log`. Ensure this file exists or will be created by the application in the current directory.

## Contributing

Feel free to fork this project and submit pull requests. For major changes, please open an issue to discuss the changes first.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- **PyQt5** for GUI development
- **Pillow** for image processing
- Python community for tools and libraries
