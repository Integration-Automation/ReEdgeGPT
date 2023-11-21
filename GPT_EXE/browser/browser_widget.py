from PySide6.QtGui import QAction, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QInputDialog

from .browser_view import BrowserView


class JEBrowser(QWidget):

    def __init__(self, start_url: str = "https://www.bing.com/chat"):
        super().__init__()
        # Browser setting
        self.browser = BrowserView(start_url)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        # Action
        self.find_action = QAction()
        self.find_action.setShortcut("Ctrl+f")
        self.find_action.triggered.connect(self.find_text)
        self.addAction(self.find_action)
        # Layout
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.browser, 0, 0, -1, -1)
        self.setLayout(self.grid_layout)

    def find_text(self):
        search_box = QInputDialog(self)
        search_text, press_ok = search_box.getText(self, "Find text", "Find text")
        if press_ok:
            self.browser.findText(search_text)
        else:
            self.browser.findText("")
