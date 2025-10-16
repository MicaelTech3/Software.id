# app.py
# -*- coding: utf-8 -*-
import sys, os, requests
from pathlib import Path

# >>>> FIX PySide6 quando instalado em --target:
def _ensure_qt_plugin_path():
    try:
        import PySide6
        pkg_dir = Path(PySide6.__file__).parent
        plugins = pkg_dir / "Qt" / "plugins"
        if plugins.exists():
            os.environ.setdefault("QT_PLUGIN_PATH", str(plugins))
            # Ajuda o Windows a achar as DLLs do Qt e do plugin 'platforms'
            os.add_dll_directory(str(pkg_dir))                 # .../sitepackages/PySide6
            os.add_dll_directory(str(pkg_dir / "Qt" / "bin"))  # .../sitepackages/PySide6/Qt/bin
    except Exception:
        pass

_ensure_qt_plugin_path()

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import Qt

def main():
    app = QApplication(sys.argv)

    win = QMainWindow()
    win.setWindowTitle("App Remoto (PySide6)")

    central = QWidget()
    layout = QVBoxLayout(central)

    lbl = QLabel("✅ App remoto carregado do Vercel")
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

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
