import queue
import sys
import time

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QWidget, QPushButton, QBoxLayout, QLineEdit
from speech_recognition import Microphone
from speech_recognition import Recognizer
from speech_recognition import RequestError, UnknownValueError
from threading import Thread

LISTENER_QUEUE = queue.Queue()


def callback(recognizer: Recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        LISTENER_QUEUE.put_nowait(text)
    except (RequestError, UnknownValueError) as error:
        print(repr(error), file=sys.stderr)


class ChatSpeechToText(QWidget):

    def __init__(self):
        super().__init__()
        # UI
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.box_layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        self.voice_text_edit = QLineEdit()
        self.start_listen_button = QPushButton("Start voice input")
        self.start_listen_button.clicked.connect(self.start_listener_thread)
        self.send_text_button = QPushButton("Send prompt")
        self.box_layout.addWidget(self.voice_text_edit)
        self.box_layout.addWidget(self.start_listen_button)
        self.box_layout.addWidget(self.send_text_button)
        self.setLayout(self.box_layout)
        # Listener Timer
        self.listener_timer = QTimer()
        self.listener_timer.setInterval(100)
        self.listener_timer.timeout.connect(self.update_voice_edit)
        self.listener_timer.start()

    def start_listener_thread(self):
        listener_thread = Thread(target=self.start_listener)
        listener_thread.daemon = True
        listener_thread.start()

    @classmethod
    def start_listener(cls):
        recognizer = Recognizer()
        microphone = Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.1)
        stop_listening = recognizer.listen_in_background(microphone, callback)
        for receive_sound_time in range(50):
            time.sleep(0.1)
        stop_listening(wait_for_stop=False)

    def update_voice_edit(self):
        if not LISTENER_QUEUE.empty():
            self.voice_text_edit.setText(str(LISTENER_QUEUE.get_nowait()))

    def close(self) -> bool:
        self.listener_timer.stop()
        return super().close()