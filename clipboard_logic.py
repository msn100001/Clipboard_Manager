import json
import os
import io
from PIL import Image


class ClipboardLogic:
    """Logic for managing clipboard history and persistence."""

    def __init__(self, json_file="clipboard_history.json"):
        """
        Initialize ClipboardLogic with a JSON file for persistence.

        :param json_file: File to store clipboard history persistently.
        """
        self.json_file = json_file
        self.saved_items = []  # List to store clipboard history
        self.separator = "---ENTRY---"  # Delimiter for export/import

    def load_from_json(self):
        """
        Load clipboard history from a JSON file.
        Initializes an empty list if the file is missing or invalid.
        """
        if os.path.exists(self.json_file):
            try:
                with open(self.json_file, "r", encoding="utf-8") as file:
                    self.saved_items = json.load(file)
            except json.JSONDecodeError:
                print("Invalid JSON file format. Starting with an empty history.")
                self.saved_items = []
            except Exception as e:
                print(f"Error loading JSON file: {e}")
        else:
            print("No existing clipboard history found. Starting fresh.")
            self.saved_items = []

    def save_to_json(self):
        """
        Save clipboard history to a JSON file.
        Handles exceptions gracefully and logs errors.
        """
        try:
            with open(self.json_file, "w", encoding="utf-8") as file:
                json.dump(self.saved_items, file)
        except Exception as e:
            print(f"Error saving to JSON file: {e}")

    def total_items(self):
        """
        Return the total number of items in the clipboard history.

        :return: Number of items in saved_items.
        """
        return len(self.saved_items)

    def add_item(self, content, data_type):
        """
        Add a new item to the clipboard history.

        :param content: The content to add (text or image data).
        :param data_type: The type of the content ("Text" or "Image").
        """
        self.saved_items.append({"type": data_type, "content": content})
        self.save_to_json()

    def delete_item(self, index):
        """
        Delete an item from the clipboard history by index.

        :param index: The index of the item to delete.
        """
        if 0 <= index < len(self.saved_items):
            del self.saved_items[index]
            self.save_to_json()
        else:
            print(f"Invalid index: {index}. Unable to delete item.")

    def get_item(self, index):
        """
        Retrieve an item from the clipboard history by index.

        :param index: The index of the item to retrieve.
        :return: The item at the specified index, or None if out of bounds.
        """
        if 0 <= index < len(self.saved_items):
            return self.saved_items[index]
        else:
            print(f"Invalid index: {index}. No item to retrieve.")
            return None

    def is_duplicate(self, content, data_type):
        """
        Check if the given content is a duplicate in the clipboard history.

        :param content: The content to check (text or image data).
        :param data_type: The type of the content ("Text" or "Image").
        :return: True if the content already exists in the history, False otherwise.
        """
        return any(item["content"] == content and item["type"] == data_type for item in self.saved_items)

    def add_image(self, image):
        """
        Convert an image to bytes and add it to the clipboard history.

        :param image: The PIL Image object to add.
        """
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_data = buffer.getvalue()
        if not self.is_duplicate(image_data, "Image"):
            self.add_item(image_data, "Image")
        else:
            print("Duplicate image not added.")

    def export_to_file(self, file_name):
        """
        Export the clipboard history to a text file with a separator.

        :param file_name: The name of the file to export to.
        """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                for item in self.saved_items:
                    # Write text content or image placeholder
                    if item["type"] == "Text":
                        file.write(item["content"])
                    elif item["type"] == "Image":
                        file.write("[Image]")
                    # Add separator after each entry
                    file.write(f"\n{self.separator}\n")
            print(f"Clipboard history exported successfully to {file_name}.")
        except Exception as e:
            print(f"Error exporting to file: {e}")

    def import_from_file(self, file_name):
        """
        Import clipboard history from a text file, handling multiline entries.

        :param file_name: The name of the file to import from.
        """
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                content = file.read()
                # Split content by the separator
                entries = content.split(f"\n{self.separator}\n")
                for entry in entries:
                    entry = entry.strip()
                    if entry == "[Image]":
                        # Skip importing images for now
                        continue
                    if entry and not self.is_duplicate(entry, "Text"):
                        self.add_item(entry, "Text")
            print(f"Clipboard history imported successfully from {file_name}.")
        except Exception as e:
            print(f"Error importing from file: {e}")
