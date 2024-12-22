from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

class Employee:
    def __init__(self, id, name, designation, salary, age, mobile_number):
        self.id = id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.age = age
        self.mobile_number = mobile_number

employees = [
    {'employeeID': 'E006', 'name': 'Nina Sharma', 'age': 30, 'salary': 75000, 'designation': 'Marketing Manager', 'mobile_number': '9876543210', 'email': 'nina.sharma@gmail.com', 'department': 'Marketing', 'address': 'Park Street, Kolkata'},
    {'employeeID': 'E007', 'name': 'Raj Patel', 'age': 42, 'salary': 68000, 'designation': 'UX Designer', 'mobile_number': '1234567890', 'email': 'raj.patel@gmail.com', 'department': 'Design', 'address': 'Churchgate, Mumbai'},
    {'employeeID': 'E008', 'name': 'Sita Verma', 'age': 29, 'salary': 62000, 'designation': 'Content Writer', 'mobile_number': '2345678901', 'email': 'sita.verma@gmail.com', 'department': 'Content', 'address': 'Connaught Place, Delhi'},
    {'employeeID': 'E009', 'name': 'Arjun Reddy', 'age': 38, 'salary': 71000, 'designation': 'HR Specialist', 'mobile_number': '3456789012', 'email': 'arjun.reddy@gmail.com', 'department': 'HR', 'address': 'Bengaluru East, Bengaluru'},
    {'employeeID': 'E010', 'name': 'Meera Joshi', 'age': 33, 'salary': 80000, 'designation': 'Project Coordinator', 'mobile_number': '4567890123', 'email': 'meera.joshi@gmail.com', 'department': 'Coordination', 'address': 'Salt Lake City, Kolkata'}
]


def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            count += 1
            return count
    return count

def binary_search(arr, target):
    count = 0
    start = 0
    end = len(arr) - 1
    while start <= end:
        count += 1
        mid = (start + end) // 2
        if arr[mid] == target:
            count += 1
            return count
        elif arr[mid] < target:
            count += 1
            start = mid + 1
        else:
            count += 1
            end = mid - 1
    return count

def find_highest_salary_designation(employees):
    if not employees:
        return None
    highest_salary_employee = max(employees, key=lambda emp: emp['salary'])
    return highest_salary_employee['designation']

def find_lowest_salary_employee(employees):
    if not employees:
        return None
    lowest_salary_employee = min(employees, key=lambda emp: emp['salary'])
    return lowest_salary_employee['name']

def find_youngest_employee_mobile(employees):
    if not employees:
        return None
    youngest_employee = min(employees, key=lambda emp: emp['age'])
    return youngest_employee['mobile_number']

def find_oldest_employee_salary(employees):
    if not employees:
        return None
    oldest_employee = max(employees, key=lambda emp: emp['age'])
    return oldest_employee['salary']

@app.route('/')
def home():
    return render_template('p41.html', results={})

@app.route('/submit', methods=['POST'])
def submit():
    numbers = list(map(int, request.form['numbers'].split(',')))
    linear_search_counts = []
    binary_search_counts = []
    for num in numbers:
        number_list = list(range(1, num + 1))
        linear_search_counts.append(linear_search(number_list.copy(), num))
        binary_search_counts.append(binary_search(number_list.copy(), num))

    # Plotting the graph
    plt.figure()
    plt.plot(numbers, linear_search_counts, label='Linear Search')
    plt.plot(numbers, binary_search_counts, label='Binary Search')
    plt.xlabel('Number of Elements')
    plt.ylabel('Operations Count')
    plt.title('Time Complexity Analysis of Linear and Binary Search')
    plt.legend()

    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph_url = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()

    # Find employee details
    highest_salary_designation = find_highest_salary_designation(employees)
    lowest_salary_employee_name = find_lowest_salary_employee(employees)
    youngest_employee_mobile = find_youngest_employee_mobile(employees)
    oldest_employee_salary = find_oldest_employee_salary(employees)

    results = {
        'numbers': numbers,
        'linear_search_counts': linear_search_counts,
        'binary_search_counts': binary_search_counts,
        'employees': employees,
        'highest_salary_designation': highest_salary_designation,
        'lowest_salary_employee_name': lowest_salary_employee_name,
        'youngest_employee_mobile': youngest_employee_mobile,
        'oldest_employee_salary': oldest_employee_salary
    }

    return render_template('p41.html', results=results, graph_url=graph_url)

if __name__ == '__main__':
    app.run(debug=True)
