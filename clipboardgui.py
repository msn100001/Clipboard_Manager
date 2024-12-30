from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QCheckBox, QMenu, QListWidgetItem, QLabel, QFileDialog
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QBrush, QColor
from error_handling import handle_exception, ClipboardOperationError
import io
from PIL import Image


class ClipboardGUI(QWidget):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic  # Instance of ClipboardLogic
        self.auto_save_enabled = False  # Auto-save toggle state

        self.init_ui()

        # Timer for auto-save functionality
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self.auto_save_clipboard)

    def init_ui(self):
        """Initialize the GUI."""
        self.setWindowTitle("Clipboard Manager")
        self.resize(600, 400)

        # Layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Widgets
        self.item_count_label = QLabel(f"Total Items: {self.logic.total_items()}")  # Item count label
        self.list_widget = QListWidget()
        self.list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_widget.customContextMenuRequested.connect(self.show_context_menu)
        self.list_widget.setStyleSheet(
            """
            QListWidget::item {
                border-bottom: 1px solid #d3d3d3;
                padding: 8px;
                color: #333333;
            }
            QListWidget::item:selected {
                background: #b0e0e6;
                color: red;
            }
            """
        )
        self.list_widget.setVerticalScrollMode(QListWidget.ScrollPerPixel)

        save_btn = QPushButton("Save Clipboard")
        export_btn = QPushButton("Export List")
        import_btn = QPushButton("Import List")
        clear_btn = QPushButton("Clear All")
        self.auto_save_toggle = QCheckBox("Enable Auto-Save")

        # Add widgets to layouts
        main_layout.addWidget(self.item_count_label)  # Add the label to the main layout
        main_layout.addWidget(self.list_widget)
        button_layout.addWidget(save_btn)
        button_layout.addWidget(export_btn)
        button_layout.addWidget(import_btn)
        button_layout.addWidget(clear_btn)
        button_layout.addWidget(self.auto_save_toggle)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Signals
        save_btn.clicked.connect(self.save_clipboard)
        export_btn.clicked.connect(self.export_list)
        import_btn.clicked.connect(self.import_list)
        clear_btn.clicked.connect(self.clear_all_items)
        self.auto_save_toggle.stateChanged.connect(self.toggle_auto_save)

    def save_clipboard(self):
        """Save the current clipboard content."""
        from PyQt5.QtGui import QGuiApplication
        clipboard = QGuiApplication.clipboard()

        try:
            if clipboard.mimeData().hasText():
                text = clipboard.text()
                if not self.logic.is_duplicate(text, "Text"):
                    self.logic.add_item(text, "Text")
                    self.update_list()
            elif clipboard.mimeData().hasImage():
                image = clipboard.image()
                self.logic.add_image(image)
                self.update_list()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to save clipboard content."), str(e))

    def update_list(self):
        """Update the GUI list widget with clipboard history."""
        try:
            self.list_widget.clear()
            for item in self.logic.saved_items:
                content = item["content"] if item["type"] == "Text" else "[Image]"
                list_item = QListWidgetItem(content)
                list_item.setForeground(QBrush(QColor("#333333")))
                self.list_widget.addItem(list_item)

            # Update the item count label
            self.item_count_label.setText(f"Total Items: {self.logic.total_items()}")
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to update the clipboard list."), str(e))

    def show_context_menu(self, position):
        """Show the right-click context menu."""
        try:
            menu = QMenu()

            copy_action = menu.addAction("Copy")
            delete_action = menu.addAction("Delete")

            action = menu.exec_(self.list_widget.mapToGlobal(position))
            if action == copy_action:
                self.copy_selected()
            elif action == delete_action:
                self.delete_selected()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to display context menu."), str(e))

    def copy_selected(self):
        """Copy the selected item to the clipboard."""
        from PyQt5.QtGui import QGuiApplication
        clipboard = QGuiApplication.clipboard()

        try:
            selected = self.list_widget.currentRow()
            if selected == -1:
                return

            selected_item = self.logic.get_item(selected)
            if selected_item["type"] == "Text":
                clipboard.setText(selected_item["content"])
            elif selected_item["type"] == "Image":
                image_data = selected_item["content"]
                image = Image.open(io.BytesIO(image_data))
                clipboard.setImage(image)
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to copy selected item to clipboard."), str(e))

    def delete_selected(self):
        """Delete the selected item from the clipboard history."""
        try:
            selected = self.list_widget.currentRow()
            if selected == -1:
                return

            self.logic.delete_item(selected)
            self.update_list()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to delete selected item."), str(e))

    def clear_all_items(self):
        """Clear all items from the clipboard history."""
        try:
            self.logic.saved_items.clear()
            self.update_list()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to clear all items."), str(e))

    def toggle_auto_save(self, state):
        """Enable or disable auto-save."""
        try:
            if state:
                self.auto_save_timer.start(1000)  # Check clipboard every second
            else:
                self.auto_save_timer.stop()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to toggle auto-save."), str(e))

    def auto_save_clipboard(self):
        """Automatically save clipboard content."""
        try:
            self.save_clipboard()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed during auto-save operation."), str(e))

    def export_list(self):
        """Export the clipboard history to a text file."""
        try:
            file_name, _ = QFileDialog.getSaveFileName(self, "Export Clipboard History", "", "Text Files (*.txt)")
            if file_name:
                self.logic.export_to_file(file_name)
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to export clipboard history."), str(e))

    def import_list(self):
        """Import clipboard history from a text file."""
        try:
            file_name, _ = QFileDialog.getOpenFileName(self, "Import Clipboard History", "", "Text Files (*.txt)")
            if file_name:
                self.logic.import_from_file(file_name)
                self.update_list()
        except Exception as e:
            handle_exception(ClipboardOperationError("Failed to import clipboard history."), str(e))
