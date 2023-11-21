import sys

from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QApplication
from qt_material import apply_stylesheet

from GPT_EXE.browser.browser_widget import JEBrowser


class JustOpenGPTBrowser(QMainWindow):

    def __init__(self):
        super().__init__()
        self.browser_widget = JEBrowser()
        self.setCentralWidget(self.browser_widget)


if __name__ == "__main__":
    new_editor = QCoreApplication.instance()
    if new_editor is None:
        new_editor = QApplication(sys.argv)
    window = JustOpenGPTBrowser()
    apply_stylesheet(new_editor, theme='dark_amber.xml')
    window.showMaximized()
    sys.exit(new_editor.exec())
