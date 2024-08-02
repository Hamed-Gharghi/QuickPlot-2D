# QuickPlot-2D

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15.7-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Description

**QuickPlot-2D** is a PyQt5 application designed for plotting and saving 2D data visualizations from CSV or TXT files. The application offers customization options for plot color, background color, and line thickness. It also supports a dark theme to enhance visual comfort. The GUI is intuitive and includes functionality to export plots as PNG images.

## Features

- **2D Data Plotting**: Visualize data from CSV or TXT files.
- **Customizable Plot Colors**: Select plot and background colors.
- **Adjustable Line Thickness**: Set the thickness of the plot line.
- **Dark Theme**: Modern dark theme for improved visual comfort.
- **Save Plots**: Export plots as PNG images.
- **Example Data Format**: View an example of the required data format.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Hamed-Gharghi/QuickPlot-2D.git
   ```

2. **Navigate to the Project Directory**:
   ```sh
   cd QuickPlot-2D
   ```

3. **Install Required Packages**:
   ```sh
   pip install PyQt5 pyqtgraph numpy
   ```

## Usage

1. **Run the Application**:
   ```sh
   QuickPlot-2D.exe
   ```
   or, if running from source:
   ```sh
   python QuickPlot-2D.py
   ```

2. **Select a Data File**: Click "Browse" to choose a CSV or TXT file with data.

3. **Customize Plot Settings**:
   - **Plot Color**: Click "Pick Plot Color" to choose the color for the plot line.
   - **Background Color**: Click "Pick Background Color" to choose the plot background color.
   - **Line Thickness**: Set the thickness of the plot line.

4. **Show Plot**: Click "Show Plot" to visualize the data.

5. **Save Plot**: Click "Save Plot" to export the plot as a PNG image.

6. **View Example Data Format**: Click "Show Example Data Format" to see how the data should be structured.

### Example Data Format

The application expects a file with the following format (CSV or TXT):

```
X,Y
0.0,0.0
0.1,0.09983
0.2,0.19867
0.3,0.29552
0.4,0.38942
0.5,0.47942
0.6,0.56464
0.7,0.64422
0.8,0.71736
0.9,0.78328
1.0,0.84147
```

- The first row contains headers (`X` and `Y`).
- Each subsequent row contains data points for the X and Y axes.

## Files

- `QuickPlot-2D.py`: The main Python script for the application.
- `icon.png`: The icon file for the application.
- `QuickPlot-2D.exe`: The executable file for the application (if provided).

## Author

**Hamed Gharghi**  
[GitHub: Hamed-Gharghi](https://github.com/Hamed-Gharghi)  
Email: [Hamedgharghi1@gmail.com](mailto:Hamedgharghi1@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- PyQt5 Documentation: [https://www.riverbankcomputing.com/static/Docs/PyQt5/](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- PyQtGraph Documentation: [http://www.pyqtgraph.org/](http://www.pyqtgraph.org/)

## Tags

- `Python`
- `PyQt5`
- `Data Visualization`
- `2D Plot`
- `CSV`
- `TXT`
- `Dark Theme`
- `Plotting Tool`
- `Open Source`
- `MIT License`

---

> **Stickers:**
> 
> ![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
> ![PyQt5](https://img.shields.io/badge/PyQt5-5.15.7-green)
> ![License](https://img.shields.io/badge/License-MIT-yellow)
