from PySide6.QtCore import Qt, QRect, QTimer
from PySide6.QtGui import QPainter, QFontDatabase, QColor
from PySide6.QtWidgets import QWidget


class ChatToast(QWidget):

    def __init__(self, text: str, close_time: int = 10000, font_size: int = 16):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.setWindowFlag(
            Qt.WindowType.WindowTransparentForInput |
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.Tool |
            Qt.WindowType.WindowStaysOnTopHint
        )
        self.text = text
        self.font_size = font_size
        self.draw_font = QFontDatabase.font(self.font().family(), "", self.font_size)
        self.draw_font.setBold(True)
        self.close_timer = QTimer()
        self.close_timer.setInterval(close_time)
        self.close_timer.timeout.connect(self.close)
        self.close_timer.start()

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.save()
        painter.setFont(
            self.draw_font
        )
        painter.setPen(QColor(0, 255, 0))
        painter.drawText(
            QRect(self.x(), self.y(), self.width(), self.height()),
            Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
            self.text
        )
        if not self.close_timer.isActive():
            self.close_timer.start()
        painter.restore()

    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)

    def mouseDoubleClickEvent(self, event) -> None:
        super().mouseDoubleClickEvent(event)

    def mouseGrabber(self) -> None:
        super().mouseGrabber()

    def close(self) -> bool:
        self.close_timer.stop()
        self.deleteLater()
        return super().close()
