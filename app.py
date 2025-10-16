# app.py
# -*- coding: utf-8 -*-
import sys, requests
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

win = QMainWindow()
win.setWindowTitle("App Remoto (PySide6)")

central = QWidget()
layout = QVBoxLayout(central)

lbl = QLabel("✅ App remoto carregado do vVercel")
lbl.setAlignment(Qt.AlignCenter)

btn = QPushButton("Testar HTTP")
def do_http():
    try:
        r = requests.get("https://httpbin.org/get", timeout=10)
        QMessageBox.information(win, "OK", f"HTTP {r.status_code}")
    except Exception as e:
        QMessageBox.critical(win, "Erro", str(e))
btn.clicked.connect(do_http)

layout.addWidget(lbl)
layout.addWidget(btn)

win.setCentralWidget(central)
win.resize(520, 260)
win.show()

sys.exit(app.exec())  # mantém a GUI viva
