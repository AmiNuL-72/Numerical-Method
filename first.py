import csv
import sympy as sp

def read_csv(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append([float(x) if x else None for x in row])
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    return data

def evaluate_expression(expr, x_values):
    x = sp.symbols('x')
    y_values = [float(expr.subs(x, val)) for val in x_values]
    return y_values

def forward_difference(y_values):
    n = len(y_values)
    fd_table = [y_values[:]]
    for i in range(1, n):
        diff = [fd_table[i - 1][j + 1] - fd_table[i - 1][j] for j in range(n - i)]
        fd_table.append(diff)
    return fd_table

def backward_difference(y_values):
    n = len(y_values)
    bd_table = [y_values[:]]
    for i in range(1, n):
        diff = [bd_table[i - 1][j] - bd_table[i - 1][j - 1] for j in range(i, n)][::-1]
        bd_table.append(diff[::-1])  # Reverse the order to match backward difference table
    return bd_table

def central_difference(y_values):
    n = len(y_values)
    cd_table = [(y_values[i + 1] - y_values[i - 1]) / 2 for i in range(1, n - 1)]
    return cd_table

def pascal_triangle(levels):
    triangle = [[1]]
    for i in range(1, levels):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle

def write_csv(file_name, data):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        max_len = max(len(row) for row in data)
        # Pad rows to make them the same length
        padded_data = [row + ["" ] * (max_len - len(row)) for row in data]
        # Transpose data to write column-wise
        transposed_data = list(zip(*padded_data))
        writer.writerows(transposed_data)

def main():
    print("Numerical Method Assignment")
    print("1. Forward Difference")
    print("2. Backward Difference")
    print("3. Central Difference")
    print("4. Pascal Triangle")

    choice = int(input("Choose an option (1-4): "))
    if choice in [1, 2, 3]:
        expr_input = input("Enter the expression in terms of x (e.g., x**2 + 3*x + 2): ")
        x_values = list(map(float, input("Enter x values separated by commas: ").split(',')))
        expr = sp.sympify(expr_input)
        y_values = evaluate_expression(expr, x_values)

        if choice == 1:
            result = forward_difference(y_values)
        elif choice == 2:
            result = backward_difference(y_values)
        elif choice == 3:
            result = central_difference(y_values)
    elif choice == 4:
        levels = int(input("Enter number of levels for Pascal Triangle: "))
        result = pascal_triangle(levels)
    else:
        print("Invalid choice!")
        return

    print("Output:")
    for row in result:
        print(row)

    output_file = input("Enter output CSV file name: ")
    write_csv(output_file, result)
    print(f"Output written to '{output_file}'")

if __name__ == "__main__":
    main()
