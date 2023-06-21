import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class FlashcardApp(QMainWindow):
    """Main application window for the flashcard app."""

    def __init__(self):
        """Initialize the flashcard app."""
        super().__init__()
        self.setWindowTitle("Flashcard App")
        self.setFixedSize(800, 600)

        self.label = QLabel("Hello, Flashcards!", self)
        self.label.move(400, 200)

        self.button = QPushButton("Show Card", self)
        self.button.move(400, 300)
        self.button.clicked.connect(self.show_flashcard)

    def show_flashcard(self):
        """Display a flashcard."""
        # Implement the logic to display a flashcard here
        print("Displaying flashcard...")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    flashcard_app = FlashcardApp()
    flashcard_app.show()
    sys.exit(app.exec_())
