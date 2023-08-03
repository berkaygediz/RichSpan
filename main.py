import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.default_values = {
            'font_family': 'Arial',
            'font_size': 10,
            'bold': False,
            'italic': False,
            'underline': False,
            'alignment': Qt.AlignLeft,
        }

        self.is_saved = False
        self.file_name = None
        self.default_directory = QDir().homePath()

        self.text_editor = QTextEdit()
        self.text_editor.setFontFamily(self.default_values['font_family'])
        self.text_editor.setFontPointSize(self.default_values['font_size'])

        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Loading...", 2000)

        self.dock_widget = QDockWidget("Docked Window", self)
        self.statistics_label = QLabel()
        self.dock_widget.setWidget(self.statistics_label)
        self.dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.dock_widget.setObjectName("Docked Window")
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_widget)
        self.setCentralWidget(self.text_editor)

        self.update_statistics()
        self.text_editor.textChanged.connect(self.update_statistics)

        action = QAction('&Action Text', self)
        action.setStatusTip('Status Bar Text')
        action.triggered.connect(self.action_triggered)
        action.setShortcut('Ctrl+K')
        self.addAction(action)

    def update_window_title(self):
        file = self.file_name if self.file_name else "New File"
        asterisk = "*" if self.is_saved else ""
        self.setWindowTitle(f"{file}{asterisk} - BG Text Editor")

    def update_statistics(self):
        text = self.text_editor.toPlainText()
        character_count = len(text)
        word_count = len(text.split())
        line_count = text.count(chr(10)) + 1
        statistics = f"<table><tr><td><b>Character Count:</b></td><td>{character_count}</td></tr><tr><td><b>Word Count:</b></td><td>{word_count}</td></tr><tr><td><b>Line Count:</b></td><td>{line_count}</td></tr></table>"
        self.statistics_label.setText(statistics)
        self.is_saved = False
        self.update_window_title()

    def action_triggered(self):
        self.status_bar.showMessage("Shortcut triggered.", 2000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.setOrganizationName("BG")
    app.setApplicationName("BG Text Editor")
    app.setApplicationVersion("0.1")
    main_window.show()
    sys.exit(app.exec_())
