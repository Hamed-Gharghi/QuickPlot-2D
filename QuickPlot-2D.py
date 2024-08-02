"""
Author: Hamed Gharghi
Date: 8/2/2024
Description: This script provides a PyQt5 application for plotting data from a CSV file. Users can select data files, choose plot colors and background colors, set line thickness, and save the plots as images.
"""

import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QLineEdit, QFileDialog, QColorDialog, QMessageBox
)
from PyQt5.QtGui import QColor, QIcon
from pyqtgraph import GraphicsLayoutWidget, mkPen

class PlotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.plot_window = None  # Keep a reference to the plot window
        self.selected_color = QColor('black')  # Default plot color
        self.background_color = None  # No custom background color by default
        self.line_thickness = 1  # Default line thickness

    def initUI(self):
        # Set Fusion style
        QApplication.setStyle('Fusion')

        self.setWindowTitle('2D Plot')
        self.setWindowIcon(QIcon('icon.png'))  # Add your icon file here
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background for the main window

        # Main layout
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # File selection
        file_layout = QHBoxLayout()
        self.file_label = QLabel('No file selected')
        self.file_button = QPushButton('Browse')
        self.file_button.setStyleSheet("background-color: #007BFF; color: white;")  # Blue button
        self.file_button.clicked.connect(self.browse_file)

        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_button)
        main_layout.addLayout(file_layout)

        # Example data format
        example_button = QPushButton('Show Example Data Format')
        example_button.setStyleSheet("background-color: #28a745; color: white;")  # Green button
        example_button.clicked.connect(self.show_example)
        main_layout.addWidget(example_button)

        # Title inputs
        title_layout = QVBoxLayout()

        # X-axis title
        x_layout = QHBoxLayout()
        x_label = QLabel("X-axis Title:")
        self.x_title_edit = QLineEdit(self)
        self.x_title_edit.setPlaceholderText("X-axis title")
        x_layout.addWidget(x_label)
        x_layout.addWidget(self.x_title_edit)
        title_layout.addLayout(x_layout)

        # Y-axis title
        y_layout = QHBoxLayout()
        y_label = QLabel("Y-axis Title:")
        self.y_title_edit = QLineEdit(self)
        self.y_title_edit.setPlaceholderText("Y-axis title")
        y_layout.addWidget(y_label)
        y_layout.addWidget(self.y_title_edit)
        title_layout.addLayout(y_layout)

        main_layout.addLayout(title_layout)

        # Line thickness input
        thickness_layout = QHBoxLayout()
        thickness_label = QLabel("Line Thickness (Optional):")
        self.thickness_edit = QLineEdit(self)
        self.thickness_edit.setPlaceholderText("Line thickness (default: 1)")
        thickness_layout.addWidget(thickness_label)
        thickness_layout.addWidget(self.thickness_edit)
        main_layout.addLayout(thickness_layout)

        # Plot color selection
        color_layout = QHBoxLayout()
        self.color_button = QPushButton("Pick Plot Color")
        self.color_button.setStyleSheet("background-color: #6c757d; color: white;")  # Gray button
        self.color_button.clicked.connect(self.pick_color)
        color_layout.addWidget(self.color_button)
        main_layout.addLayout(color_layout)

        # Background color selection
        bg_color_layout = QHBoxLayout()
        self.bg_color_button = QPushButton("Pick Background Color")
        self.bg_color_button.setStyleSheet("background-color: #6c757d; color: white;")  # Gray button
        self.bg_color_button.clicked.connect(self.pick_background_color)
        bg_color_layout.addWidget(self.bg_color_button)
        main_layout.addLayout(bg_color_layout)

        # Plot button
        self.plot_button = QPushButton('Show Plot')
        self.plot_button.setStyleSheet("background-color: #007BFF; color: white;")  # Blue button
        self.plot_button.clicked.connect(self.plot_data)
        main_layout.addWidget(self.plot_button)

        # Save button
        self.save_button = QPushButton('Save Plot')
        self.save_button.setStyleSheet("background-color: #28a745; color: white;")  # Green button
        self.save_button.clicked.connect(self.save_plot)
        main_layout.addWidget(self.save_button)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # Set window size to a smaller dimension
        self.resize(400, 300)  # Adjust window size to be smaller

    def browse_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select Data File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_name:
            self.file_label.setText(file_name)
            self.data_file = file_name

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.selected_color = color
            self.color_button.setStyleSheet(f'background-color: {color.name()}; color: white;')

    def pick_background_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.background_color = color
            self.bg_color_button.setStyleSheet(f'background-color: {color.name()}; color: white;')

    def calculate_brightness(self, color):
        # Convert to grayscale using the luminance formula
        return 0.299 * color.red() + 0.587 * color.green() + 0.114 * color.blue()

    def show_example(self):
        example_text = (
            "Example Data Format:\n\n"
            "X,Y\n"
            "0.0,0.0\n"
            "0.1,0.09983\n"
            "0.2,0.19867\n"
            "...\n"
            "10.0,-0.54402\n\n"
            "Ensure the data is in txt or CSV format with the first row as headers."
        )
        QMessageBox.information(self, "Example Data Format", example_text)

    def plot_data(self):
        if not hasattr(self, 'data_file') or not self.data_file:
            QMessageBox.warning(self, "Error", "No data file selected. Please select a file before plotting.")
            return

        try:
            data = np.loadtxt(self.data_file, delimiter=',', skiprows=1)
            x_data = data[:, 0]
            y_data = data[:, 1]

            # Apply line thickness if provided
            try:
                self.line_thickness = float(self.thickness_edit.text()) if self.thickness_edit.text() else 1
            except ValueError:
                QMessageBox.warning(self, "Error", "Invalid line thickness value. Using default thickness of 1.")
                self.line_thickness = 1

            x_title = self.x_title_edit.text()
            y_title = self.y_title_edit.text()

            # Determine if the plot color is light or dark
            brightness = self.calculate_brightness(self.selected_color)
            default_bg_color = QColor('white') if brightness < 128 else QColor('black')

            # Use custom background color if provided
            final_bg_color = self.background_color if self.background_color else default_bg_color

            # Create the plot window and keep a reference to it
            self.plot_window = GraphicsLayoutWidget(show=True)
            plot = self.plot_window.addPlot()
            plot.plot(x_data, y_data, pen=mkPen(self.selected_color.name(), width=self.line_thickness))
            plot.setLabel('bottom', x_title)
            plot.setLabel('left', y_title)
            plot.setTitle("2D Plot")

            # Set background color
            self.plot_window.setBackground(final_bg_color)

            self.plot_window.show()

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while plotting data: {e}")

    def save_plot(self):
        if not self.plot_window:
            QMessageBox.warning(self, "Error", "No plot available to save. Please plot data first.")
            return

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Plot As", "", "PNG Files (*.png);;All Files (*)", options=options)
        if file_name:
            try:
                # Capture the plot area as a QPixmap
                exporter = self.plot_window.grab()
                exporter.save(file_name)
                QMessageBox.information(self, "Success", f"Plot saved successfully as {file_name}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while saving the plot: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plotter = PlotApp()
    plotter.show()
    sys.exit(app.exec_())
