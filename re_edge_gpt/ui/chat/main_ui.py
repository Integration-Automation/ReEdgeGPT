import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from qt_material import QtStyleTools, apply_stylesheet

from re_edge_gpt.ui.chat.main_widget import ChatWidget


class ChatMainUI(QMainWindow, QtStyleTools):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(ChatWidget())


def start_chat_ui() -> None:
    main_app = QApplication(sys.argv)
    window = ChatMainUI()
    apply_stylesheet(main_app, theme='dark_amber.xml')
    window.showMaximized()
    sys.exit(main_app.exec())
