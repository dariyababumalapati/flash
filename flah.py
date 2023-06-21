import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtCore import Qt

class FlashcardApp(QMainWindow):
    # ... your existing code ...

    def __init__(self):
        
        super().__init__()

        self.setWindowTitle("Flashcard App")
        self.resize(800, 600)

        self.label = QLabel("Hello", self)
        self.label.setAlignment(Qt.AlignCenter)  # Center-align the text
        self.label.setWordWrap(True)  # Enable word wrapping for long texts

        # Call adjustSize() after setting the text to resize the label
        self.label.setText("This is a long text that will automatically wrap to fit within the label's dimensions.")
        self.label.adjustSize()
        
        self.button = QPushButton("Show Card", self)
        self.button.setGeometry(400, 500, 100, 50)
        self.button.clicked.connect(self.show_flashcard)

        self.flashcards = [
            ("What is the capital of France?", "Paris"),
            ("What is the largest planet in our solar system?", "Jupiter"),
            ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
            # Add more flashcards as needed
        ]

        self.current_flashcard_index = 0

    def show_flashcard(self):
        """Display a flashcard."""
        if self.current_flashcard_index < len(self.flashcards):
            flashcard = self.flashcards[self.current_flashcard_index]
            question = flashcard[0]
            self.label.setText(question)  # Display the question on the label
            self.button.setText("Show Answer")  # Update button text

            # Reconnect the button's clicked signal to a new method
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.show_answer)
        else:
            self.label.setText("No more flashcards.")  # Display a message if all flashcards have been shown

    def show_answer(self):
        """Display the answer to the flashcard."""
        flashcard = self.flashcards[self.current_flashcard_index]
        answer = flashcard[1]
        self.label.setText(answer)  # Display the answer on the label

        self.current_flashcard_index += 1  # Move to the next flashcard

        if self.current_flashcard_index < len(self.flashcards):
            self.button.setText("Show Card")  # Update button text for the next flashcard
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.show_flashcard)
        else:
            self.button.setText("No more flashcards")
            self.button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    flashcard_app = FlashcardApp()
    flashcard_app.show()
    sys.exit(app.exec_())
