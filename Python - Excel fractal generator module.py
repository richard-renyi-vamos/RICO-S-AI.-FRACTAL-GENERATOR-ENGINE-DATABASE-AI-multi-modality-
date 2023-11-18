import openpyxl
import matplotlib.pyplot as plt

# Load Excel file
file_path = 'your_excel_file.xlsx'  # Replace 'your_excel_file.xlsx' with your file path
workbook = openpyxl.load_workbook(file_path)
sheet = workbook.active

# Extract data from Excel
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(row)

# Use the data to generate a Mandelbrot set fractal (or any other fractal)
# Replace this with your fractal generation algorithm using the 'data'

# Example: Plot a simple Mandelbrot set using the first two columns of data
x = [row[0] for row in data]
y = [row[1] for row in data]

plt.scatter(x, y, s=1)  # Adjust 's' (size) as needed
plt.title('Fractal Based on Excel Data')
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.show()
