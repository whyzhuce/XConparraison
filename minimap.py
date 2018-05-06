"""
http://ninja-ide.github.io/ninja-ide/listings/ninja_ide/gui/editor/
"""
import sys

from PyQt4.QtGui import QApplication, QFrame, QPlainTextEdit, QTextOption, QGraphicsOpacityEffect, QFontMetrics
from PyQt4.QtCore import Qt, SIGNAL, QPropertyAnimation

MINIMAP_MIN_OPACITY = 0.1
MINIMAP_MAX_OPACITY = 0.8
MARGIN_LINE = 80
SIZE_PROPORTION = 0.17


class MiniMap(QPlainTextEdit):

    def __init__(self, parent):
        super(MiniMap, self).__init__(parent)
        self.setWordWrapMode(QTextOption.NoWrap)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setReadOnly(True)
        self.setCenterOnScroll(True)
        self.setMouseTracking(True)
        self.viewport().setCursor(Qt.PointingHandCursor)
        self.setTextInteractionFlags(Qt.NoTextInteraction)

        self._parent = parent
        self.highlighter = None
        self.lines_count = 0

        self.connect(self._parent, SIGNAL("updateRequest(const QRect&, int)"),
                self.update_visible_area)

        self.goe = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.goe)
        self.goe.setOpacity(MINIMAP_MIN_OPACITY)
        self.animation = QPropertyAnimation(self.goe, "opacity")

        self.slider = SliderArea(self)
        self.slider.show()

    def __calculate_max(self):
        line_height = self._parent.cursorRect().height()
        if line_height > 0:
            self.lines_count = self._parent.viewport().height() / line_height
        self.slider.update_position()
        self.update_visible_area()

    def set_code(self, source):
        self.setPlainText(source)
        self.__calculate_max()

    def adjust_to_parent(self):
        self.setFixedHeight(self._parent.height())
        self.setFixedWidth(self._parent.width() * SIZE_PROPORTION)
        x = self._parent.width() - self.width()
        self.move(x, 0)
        fontsize = int(self.width() / MARGIN_LINE)
        if fontsize < 1:
            fontsize = 1
        font = self.document().defaultFont()
        font.setPointSize(fontsize)
        self.setFont(font)
        self.__calculate_max()

    def update_visible_area(self):
        if not self.slider.pressed:
            line_number = self._parent.firstVisibleBlock().blockNumber()
            block = self.document().findBlockByLineNumber(line_number)
            cursor = self.textCursor()
            cursor.setPosition(block.position())
            rect = self.cursorRect(cursor)
            self.setTextCursor(cursor)
            self.slider.move_slider(rect.y())

    def enterEvent(self, event):
        self.animation.setDuration(300)
        self.animation.setStartValue(MINIMAP_MIN_OPACITY)
        self.animation.setEndValue(MINIMAP_MAX_OPACITY)
        self.animation.start()

    def leaveEvent(self, event):
        self.animation.setDuration(300)
        self.animation.setStartValue(MINIMAP_MAX_OPACITY)
        self.animation.setEndValue(MINIMAP_MIN_OPACITY)
        self.animation.start()

    def mousePressEvent(self, event):
        super(MiniMap, self).mousePressEvent(event)
        cursor = self.cursorForPosition(event.pos())
        self._parent.jump_to_line(cursor.blockNumber())

    def resizeEvent(self, event):
        super(MiniMap, self).resizeEvent(event)
        x = self._parent.width() - self.width()
        self.move(x, 0)
        self.slider.update_position()

    def scroll_area(self, pos_parent, pos_slider):
        pos_parent.setY(pos_parent.y() - pos_slider.y())
        cursor = self.cursorForPosition(pos_parent)
        self._parent.verticalScrollBar().setValue(cursor.blockNumber())

    def wheelEvent(self, event):
        super(MiniMap, self).wheelEvent(event)
        self._parent.wheelEvent(event)


class SliderArea(QFrame):

    def __init__(self, parent):
        super(SliderArea, self).__init__(parent)
        self._parent = parent
        self.setMouseTracking(True)
        self.setCursor(Qt.OpenHandCursor)
        color = "#858585"
        self.setStyleSheet("background: %s;" % color)
        self.goe = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.goe)
        self.goe.setOpacity(MINIMAP_MAX_OPACITY / 2)

        self.pressed = False
        self.__scroll_margins = None

    def paintEvent(self, event):
        """Paint over the widget to overlay its content."""
        super(SliderArea, self).paintEvent(event)

    def update_position(self):
        font_size = QFontMetrics(self._parent.font()).height()
        height = self._parent.lines_count * font_size
        self.setFixedHeight(height)
        self.setFixedWidth(self._parent.width())
        self.__scroll_margins = (height, self._parent.height() - height)

    def move_slider(self, y):
        self.move(0, y)

    def mousePressEvent(self, event):
        super(SliderArea, self).mousePressEvent(event)
        self.pressed = True
        self.setCursor(Qt.ClosedHandCursor)

    def mouseReleaseEvent(self, event):
        super(SliderArea, self).mouseReleaseEvent(event)
        self.pressed = False
        self.setCursor(Qt.OpenHandCursor)

    def mouseMoveEvent(self, event):
        super(SliderArea, self).mouseMoveEvent(event)
        if self.pressed:
            pos = self.mapToParent(event.pos())
            y = pos.y() - (self.height() / 2)
            if y < 0:
                y = 0
            if y < self.__scroll_margins[0]:
                self._parent.verticalScrollBar().setSliderPosition(
                    self._parent.verticalScrollBar().sliderPosition() - 2)
            elif y > self.__scroll_margins[1]:
                self._parent.verticalScrollBar().setSliderPosition(
                    self._parent.verticalScrollBar().sliderPosition() + 2)
            self.move(0, y)
            self._parent.scroll_area(pos, event.pos())


class Editor(QPlainTextEdit):
    def __init__(self):
        super(Editor, self).__init__()
        self.minimap = MiniMap(self)

    def resizeEvent(self, event):
        super(Editor, self).resizeEvent(event)
        self.minimap.adjust_to_parent()

    def jump_to_line(self, lineno):
        self.emit(SIGNAL("addBackItemNavigation()"))
        self.go_to_line(lineno)
        return

    def go_to_line(self, lineno):
        # self._unfold_blocks_for_jump(lineno)
        cursor = self.textCursor()
        cursor.setPosition(self.document().findBlockByLineNumber(
            lineno).position())
        self.setTextCursor(cursor)


app = QApplication(sys.argv)
w = Editor()
w.show()
sys.exit(app.exec_())
