from PySide6.QtCore import QTimer
from PySide6.QtGui import QFontDatabase, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QScrollArea, QComboBox, QLabel, \
    QPlainTextEdit, QLineEdit, QBoxLayout, QCheckBox

from re_edge_gpt.ui.chat.input_dialog import ChatInputDialog
from re_edge_gpt.ui.chat.chat_thread import ChatThread, DELEGATE_CHAT, PANEL_MESSAGE_QUEUE
from re_edge_gpt.ui.chat.speech_to_text import ChatSpeechToText


class ChatWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.voice_input = None
        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        # Init
        self.chat_input = ChatInputDialog()
        self.choose_style_combobox = QComboBox()
        self.choose_style_combobox.addItems(["creative", "precise", "balanced"])
        self.choose_style_combobox.currentTextChanged.connect(self.change_style)
        # New topic button
        self.new_topic_button = QPushButton("New topic")
        self.new_topic_button.clicked.connect(self.new_topic)
        # Start button
        self.start_button = QPushButton("Start chat")
        self.start_button.clicked.connect(self.start_chat)
        # Chat panel
        self.chat_panel = QPlainTextEdit()
        self.chat_panel.setLineWrapMode(self.chat_panel.LineWrapMode.NoWrap)
        self.chat_panel.setReadOnly(True)
        self.chat_panel_scroll_area = QScrollArea()
        self.chat_panel_scroll_area.setWidgetResizable(True)
        self.chat_panel_scroll_area.setViewportMargins(0, 0, 0, 0)
        self.chat_panel_scroll_area.setWidget(self.chat_panel)
        self.chat_panel.setFont(QFontDatabase.font(self.font().family(), "", 16))
        # Font size combobox
        self.font_size_label = QLabel("Font size")
        self.font_size_combobox = QComboBox()
        for font_size in range(2, 101, 2):
            self.font_size_combobox.addItem(str(font_size))
        self.font_size_combobox.setCurrentText("16")
        self.font_size_combobox.currentTextChanged.connect(self.update_panel_text_size)
        # Close delay combobox
        self.close_delay_label = QLabel("Toast close delay")
        self.close_delay_combobox = QComboBox()
        for sec in range(1, 101, 1):
            self.close_delay_combobox.addItem(str(sec))
        self.close_delay_combobox.setCurrentText("10")
        # Locale box
        self.locale_label = QLabel("Country code")
        self.locale_input = QLineEdit()
        self.locale_input.setText("zh-tw")
        self.local_box = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        self.local_box.addWidget(self.locale_label)
        self.local_box.addWidget(self.locale_input)
        # Start voice input
        self.start_voice_input_button = QPushButton("Start voice input")
        self.start_voice_input_button.clicked.connect(self.start_voice_input)
        # Show toast checkbox
        self.show_toast_checkbox_label = QLabel("Show toast?")
        self.show_toast_checkbox = QCheckBox()
        # Add to layout
        self.grid_layout.addWidget(self.choose_style_combobox, 0, 0)
        self.grid_layout.addWidget(self.close_delay_label, 0, 1)
        self.grid_layout.addWidget(self.close_delay_combobox, 0, 2)
        self.grid_layout.addWidget(self.font_size_label, 0, 3)
        self.grid_layout.addWidget(self.font_size_combobox, 0, 4)
        self.grid_layout.addLayout(self.local_box, 0, 5)
        self.grid_layout.addWidget(self.show_toast_checkbox_label, 0, 6)
        self.grid_layout.addWidget(self.show_toast_checkbox, 0, 7)
        self.grid_layout.addWidget(self.new_topic_button, 0, 8)
        self.grid_layout.addWidget(self.start_voice_input_button, 0, 9)
        self.grid_layout.addWidget(self.start_button, 0, 10)
        self.grid_layout.addWidget(self.chat_panel_scroll_area, 1, 0, -1, -1)
        # update panel timer
        self.update_panel_timer = QTimer()
        self.update_panel_timer.setInterval(10)
        self.update_panel_timer.timeout.connect(self.update_panel)
        self.update_panel_timer.start()
        self.setLayout(self.grid_layout)

    def update_panel(self):
        if not PANEL_MESSAGE_QUEUE.empty():
            text = PANEL_MESSAGE_QUEUE.get_nowait()
            self.chat_panel.appendPlainText(text)
            self.chat_panel.appendPlainText("\n")

    def update_panel_text_size(self):
        self.chat_panel.setFont(
            QFontDatabase.font(self.font().family(), "", int(self.font_size_combobox.currentText())))

    def start_chat(self) -> None:
        self.chat_input = ChatInputDialog(
            close_time=int(self.close_delay_combobox.currentText()) * 1000,
            font_size=int(self.font_size_combobox.currentText()),
            show_toast=self.show_toast_checkbox.isChecked()
        )
        self.chat_input.show()
        self.chat_input.send_text_button.clicked.connect(self.send_chat)

    def start_voice_input(self):
        self.voice_input = ChatSpeechToText()
        self.voice_input.show()
        self.voice_input.send_text_button.clicked.connect(self.send_voice_chat)

    def send_voice_chat(self):
        chat_thread = ChatThread(self.voice_input.voice_text_edit.text(), self.locale_input.text())
        chat_thread.start()

    def send_chat(self):
        chat_thread = ChatThread(self.chat_input.chat_input.toPlainText(), self.locale_input.text())
        chat_thread.start()

    def change_style(self):
        DELEGATE_CHAT.change_style(self.choose_style_combobox.currentText())

    def new_topic(self):
        DELEGATE_CHAT.new_topic(self.chat_panel)
        self.chat_input.close()

    def close_chat_ui(self):
        if self.chat_input.isVisible():
            self.chat_input.close()
        self.chat_input = None


    def close(self) -> bool:
        self.close_chat_ui()
        return super().close()
