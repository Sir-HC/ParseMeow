import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, QMenu,
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QTabWidget,
    )
from PyQt6.QtCore import QSize, Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setMouseTracking(True)
        self.label = QLabel()
        
        self.input = QLineEdit()
        widgets = [
            QTabWidget
        ]
        
        #self.input.textChanged.connect(self.label.setText)
        #self.button = QPushButton("Press Me")
        #self.button.setCheckable(False)
        
        #self.button.clicked.connect(self.button_click)
        
        layout = QVBoxLayout()
        for w in widgets:
            layout.addWidget(w())
        container = QWidget()
        
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        #self.setMinimumSize(QSize(400,300))
    
    
    '''
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.exec(e.globalPos())
    
    def mouseMoveEvent(self, e):
        self.label.setText('mousemove')
        
    def mousePressEvent(self, e):
        self.label.setText(str(e.button()))
        
    def mouseReleaseEvent(self, e):
        self.label.setText('mouserel')
        
        
    def button_click(self):
        print("click")
        self.button.setText('click')
        self.button.setEnabled(False)
        
        self.setWindowTitle('apap')
    '''
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()