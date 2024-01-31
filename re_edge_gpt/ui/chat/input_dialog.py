from typing import Union

import pyttsx3
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QBoxLayout, QWidget, QPushButton, QHBoxLayout, QTextEdit, QMessageBox

from re_edge_gpt.ui.chat.toast import ChatToast
from re_edge_gpt.ui.chat.chat_thread import MESSAGE_QUEUE, EXCEPTION_QUEUE


class ChatInputDialog(QWidget):
    def __init__(self, close_time: int = 10000, font_size: int = 16, show_toast: bool = True):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.box_layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)
        self.chat_input = QTextEdit()
        self.send_text_button = QPushButton()
        self.send_text_button.setText("Send prompt")
        self.box_h_layout = QHBoxLayout()
        self.box_h_layout.addWidget(self.send_text_button)
        self.box_layout.addWidget(self.chat_input)
        self.box_layout.addLayout(self.box_h_layout)
        self.setWindowTitle("Please input prompt")
        self.setLayout(self.box_layout)
        # Show toast?
        self.show_toast = show_toast
        # Get message timer
        self.get_message_timer = QTimer()
        self.get_message_timer.setInterval(1000)
        self.get_message_timer.timeout.connect(self.get_message)
        self.get_message_timer.start()
        # Check error timer
        self.check_error_timer = QTimer()
        self.check_error_timer.setInterval(1000)
        self.check_error_timer.timeout.connect(self.check_error)
        self.check_error_timer.start()
        # Toast
        self.close_time = close_time
        self.font_size = font_size
        self.toast_widget: Union[ChatToast, None] = None
        # Text to speech
        self.engine = pyttsx3.init()

    def get_message(self):
        if not MESSAGE_QUEUE.empty():
            text = MESSAGE_QUEUE.get_nowait()
            if self.show_toast:
                self.toast_widget = ChatToast(
                    text=text, close_time=self.close_time, font_size=self.font_size)
                self.toast_widget.showFullScreen()
            # self.engine.say(text)

    def show_text(self):
        if self.toast_widget is not None and self.toast_widget.isVisible() is False:
            self.get_message()
        elif self.toast_widget is None:
            self.get_message()

    def check_error(self):
        if not EXCEPTION_QUEUE.empty():
            gpt_error_messagebox = QMessageBox(self)
            gpt_error_messagebox.setText(
                "Catch exception" + "\n"
                + EXCEPTION_QUEUE.get_nowait()
            )
            gpt_error_messagebox.show()

    def close(self) -> bool:
        self.get_message_timer.stop()
        self.check_error_timer.stop()
        self.destroy()
        return False