
import sys
import socket
import requests
from PySide6.QtCore import (Qt, QThread, Signal, Slot, QObject, QPropertyAnimation,
                          QEasingCurve, QTimer)
from PySide6.QtGui import QIcon, QColor, QPixmap
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QLineEdit, QTableWidget,
                               QTableWidgetItem, QHeaderView, QLabel, QProgressBar,
                               QCheckBox, QFrame)

import resources_rc


COMMON_SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    993: "IMAPS", 995: "POP3S", 1433: "MSSQL", 1521: "Oracle",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 5900: "VNC",
    8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
}


class ScannerWorker(QObject):
  
    port_scanned = Signal(tuple)
    scan_finished = Signal(str)
    
    def __init__(self, target_ip, port_range, timeout):
        super().__init__()
        self.target_ip = target_ip
        self.ports = list(range(port_range[0], port_range[1] + 1))
        self.timeout = timeout
        self._is_running = True

    @Slot()
    def run(self):
        for port in self.ports:
            if not self._is_running:
                break
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            try:
               
                resolved_ip = socket.gethostbyname(self.target_ip)
                result = s.connect_ex((resolved_ip, port))
                if result == 0:
                    service = COMMON_SERVICES.get(port, "Desconocido")
                    self.port_scanned.emit((port, True, service))
                else:
                    
                    pass
            except socket.gaierror:
               
                self.scan_finished.emit(f"Error: No se pudo resolver el host '{self.target_ip}'")
                return
            except socket.error:
                
                pass
            finally:
                s.close()
        
        status_message = "Cancelado" if not self._is_running else "Completado"
        self.scan_finished.emit(status_message)

    def stop(self):
        self._is_running = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.thread = None
        self.worker = None
        self._setup_ui()
        self._apply_styles()
        self._run_intro_animation()

    def _setup_ui(self):
        self.setWindowTitle("CyberScan v1.0")
        self.setWindowIcon(QIcon(":/icons/scan.svg"))
        self.setMinimumSize(700, 600)

        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)

     
        controls_frame = QFrame()
        controls_layout = QHBoxLayout(controls_frame)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        
     
        target_icon_label = QLabel()
      
        target_icon_label.setPixmap(QIcon(":/icons/target.svg").pixmap(24, 24))
      

        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Introduce IP o dominio...")
        
        self.get_ip_button = QPushButton(QIcon(":/icons/ip.svg"), " Mi IP")
        
        self.common_ports_check = QCheckBox("Puertos Comunes")
        self.common_ports_check.setChecked(True)
        
        self.port_range_input = QLineEdit("1-1024")
        self.port_range_input.setVisible(False)

        
        controls_layout.addWidget(target_icon_label) 
        controls_layout.addWidget(self.ip_input, 3)
        controls_layout.addWidget(self.get_ip_button)
        controls_layout.addWidget(self.common_ports_check)
        controls_layout.addWidget(self.port_range_input, 1)

        
        action_layout = QHBoxLayout()
        self.scan_button = QPushButton(QIcon(":/icons/scan.svg"), " Iniciar Escaneo")
        self.scan_button.setObjectName("scanButton") 
        self.stop_button = QPushButton(QIcon(":/icons/stop.svg"), " Detener")
        self.stop_button.setEnabled(False)
        action_layout.addWidget(self.scan_button)
        action_layout.addWidget(self.stop_button)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["Puerto", "Estado", "Servicio Probable"])
        self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.results_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.results_table.setAlternatingRowColors(True)
       
        status_layout = QHBoxLayout()
        self.status_label = QLabel("Listo")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 0)
        self.progress_bar.setVisible(False)
        status_layout.addWidget(self.status_label)
        status_layout.addStretch()
        status_layout.addWidget(self.progress_bar, 1)

        
        main_layout.addWidget(controls_frame)
        main_layout.addLayout(action_layout)
        main_layout.addWidget(self.results_table)
        main_layout.addLayout(status_layout)
        
       
        self.scan_button.clicked.connect(self.start_scan)
        self.stop_button.clicked.connect(self.stop_scan)
        self.get_ip_button.clicked.connect(self.fetch_public_ip)
        self.common_ports_check.stateChanged.connect(self.toggle_port_range_input)

    def _apply_styles(self):
        try:
            with open("style.qss", "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print("Advertencia: No se encontró 'style.qss'. Se usará el estilo por defecto.")

    def _run_intro_animation(self):
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setDuration(500)
        self.anim.setStartValue(0.0)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutCubic)
        self.anim.start()

    @Slot()
    def start_scan(self):
        target_ip = self.ip_input.text().strip()
        if not target_ip:
            self.status_label.setText("Error: La IP no puede estar vacía.")
            return

        if self.common_ports_check.isChecked():
            ports_to_scan = sorted(COMMON_SERVICES.keys())
        else:
            try:
                start, end = map(int, self.port_range_input.text().split('-'))
                if not 0 < start <= end <= 65535:
                    raise ValueError("Rango de puertos fuera de límites válidos.")
                ports_to_scan = list(range(start, end + 1))
            except ValueError as e:
                self.status_label.setText(f"Error: Rango inválido. {e}")
                return

        self._set_ui_state(is_scanning=True)
        self.results_table.setRowCount(0) 
        self.status_label.setText(f"Escaneando {target_ip}...")
        
    
        class CustomScannerWorker(ScannerWorker):
             def __init__(self, target_ip, ports_to_scan, timeout):
                 super().__init__(target_ip, (0,0), timeout)
                 self.ports = ports_to_scan

        self.thread = QThread()
        self.worker = CustomScannerWorker(target_ip, ports_to_scan, timeout=0.5)
        self.worker.moveToThread(self.thread)

        self.worker.port_scanned.connect(self.add_result_to_table)
        self.worker.scan_finished.connect(self.scan_finished)
        self.thread.started.connect(self.worker.run)
        self.thread.start()
        
    @Slot()
    def stop_scan(self):
        if self.worker:
            self.worker.stop()
        
    
    @Slot(tuple)
    def add_result_to_table(self, result):
        port, is_open, service = result
        if is_open:
            row_position = self.results_table.rowCount()
            self.results_table.insertRow(row_position)
            
            port_item = QTableWidgetItem(str(port))
            status_item = QTableWidgetItem("ABIERTO")
            status_item.setForeground(QColor("#1abc9c")) 
            service_item = QTableWidgetItem(service)
            
            self.results_table.setItem(row_position, 0, port_item)
            self.results_table.setItem(row_position, 1, status_item)
            self.results_table.setItem(row_position, 2, service_item)

    @Slot(str)
    def scan_finished(self, status):
      
        if status.startswith("Error:"):
            self.status_label.setText(status)
        else:
            self.status_label.setText(f"Escaneo {status.lower()} en {self.ip_input.text()}.")
        
        self._set_ui_state(is_scanning=False)
        if self.thread:
            self.thread.quit()
            self.thread.wait()
            self.thread = None
        self.worker = None

    @Slot()
    def fetch_public_ip(self):
        self.status_label.setText("Obteniendo IP pública...")
       
        QTimer.singleShot(10, self._do_fetch_ip)

    def _do_fetch_ip(self):
        try:
            ip = requests.get('https://api.ipify.org?format=json', timeout=5).json()['ip']
            self.ip_input.setText(ip)
            self.status_label.setText(f"IP pública obtenida: {ip}")
        except requests.RequestException:
            self.status_label.setText("Error al obtener la IP pública.")

    @Slot(int)
    def toggle_port_range_input(self, state):
        self.port_range_input.setVisible(state != Qt.CheckState.Checked.value)

    def _set_ui_state(self, is_scanning):
        self.ip_input.setEnabled(not is_scanning)
        self.get_ip_button.setEnabled(not is_scanning)
        self.common_ports_check.setEnabled(not is_scanning)
        self.port_range_input.setEnabled(not is_scanning)
        self.scan_button.setEnabled(not is_scanning)
        self.stop_button.setEnabled(is_scanning)
        self.progress_bar.setVisible(is_scanning)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())