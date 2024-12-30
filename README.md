
# 📋 Clipboard Manager

A Python-based clipboard management application with a graphical user interface (GUI) built using PyQt5. This application allows users to save, view, manage, and export/import clipboard history, including both text and images.

---

## ✨ Features

- 📋 **Save Clipboard Content**: Manually or automatically save text and image content from the clipboard.
- 🗂️ **Persistent Clipboard History**: Entries are saved in a JSON file and persist across sessions.
- 🖼️ **Multimedia Support**: Handles both text and images.
- 📤 **Export/Import History**: Export clipboard history to a text file and import it back seamlessly.
- 🗑️ **Easy Management**: Delete individual entries or clear the entire history with a single click.
- ⚙️ **Error Handling and Logging**: Robust error handling with logs saved to `clipboard_manager_errors.log`.

---

## 🖥️ Screenshot

Below is a screenshot of the Clipboard Manager GUI:

![Clipboard Manager GUI](https://github.com/msn100001/Clipboard_Manager/raw/main/images/GUI_Image.png)

---

## 🛠️ Requirements

- Python 3.7+
- PyQt5
- Pillow (PIL for image handling)

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone git@github.com:msn100001/Clipboard_Manager.git
   cd Clipboard_Manager
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

---

## 📋 Usage

- **Saving Clipboard Content**: Click "Save Clipboard" to manually save the current clipboard content.
- **Auto-Save**: Enable "Auto-Save" to periodically save clipboard content automatically.
- **Export**: Use the "Export List" button to save clipboard history to a text file.
- **Import**: Use the "Import List" button to load clipboard history from a file.
- **Delete Entries**: Right-click an entry in the list to delete it, or use the "Clear All" button to delete all entries.

---

## 📁 File Structure

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

---

## 📂 Export/Import File Format

- **Export**: Clipboard entries are exported to a text file with a delimiter (`---ENTRY---`) to distinguish between entries.
- **Import**: The application automatically parses imported files and restores clipboard entries.

---

## 🛡️ Error Logging

All errors are logged to `clipboard_manager_errors.log`. Ensure this file exists or is created in the current directory by the application.

---

## 🤝 Contributing

Contributions are welcome! Fork this repository, make your changes, and submit a pull request. For major changes, please open an issue to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙌 Acknowledgments

- **PyQt5** for GUI development
- **Pillow** for image processing
- The Python community for tools and libraries
