import search_algos

import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# generate random data 
def random_list(size):
    return [random.randint(1, 9999) for _ in range(size)]


def get_input(): 
    global sorted_data
    user_text = data_entry.get()  
    try:
        num_data_points = int(user_text)

        if num_data_points < 0: # prompt error if entered value is less than zero
            raise ValueError
        
        data = random_list(num_data_points)  # generate random values
    except ValueError:  # prompts error if a letter is deteccted 
        result.config(text="Please only enter numbers greater than zero")
        return

    # Check which sorting algorithm is selected
    selected_algorithms = [algo for algo, var in check_vars.items() if var.get()]

    data_results = f"Data before sorting: {data}\n\n" # print unsorted data 

    execution_times = []
    algorithms = []

    for algo in selected_algorithms:    # for selected algos, sort data and print results
        start_time = time.time()
        if algo == "Bubble Sort":
            sorted_data = search_algos.bubble_sort(data)  
        elif algo == "Merge Sort":
            sorted_data = search_algos.merge_sort(data)  
        elif algo == "Quick Sort":
            sorted_data = search_algos.quick_sort(data)  
        elif algo == "Radix Sort":
            sorted_data = search_algos.lsd_radix_sort(data)  
        
        end_time = time.time()
        execution_time = end_time - start_time

        execution_times.append(execution_time)
        algorithms.append(algo)
        data_results += f"Sorted Data for {algo}: {sorted_data}\n"
        data_results += f"Execution time: {execution_time:.6f} seconds\n\n"

    current_text = result.cget("text")
    result.config(text=current_text + data_results)

    plt.figure(figsize=(8, 5))
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in algorithms]
    plt.bar(algorithms, execution_times, color=colors)
    plt.xlabel("Sorting Algorithm")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Execution Times")
    plt.xticks(rotation=45)
    plt.ylim(0, max(execution_times) * 1.2)    
    plt.show()

def lin_search():
    user_input = search_entry.get()
    user_search = int(user_input)

    current_text = result.cget("text")

    search_result = search_algos.linear_search(sorted_data, user_search)
    if search_result != -1:
        result.config(text=current_text + f"{user_search} found at index {search_result}")
    else:
        result.config(text=current_text + f"{user_search} not found in the data")

root = tk.Tk()
root.title("Select Sorting Method")

# Create a label for user input
data_points = tk.Label(root, text="Enter number of data points:")
data_points.pack(pady=5)

# Create an entry box for user input
data_entry = tk.Entry(root, width=30)
data_entry.pack(pady=5)

# Frame to hold the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=5)

# Sorting algorithms options
algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort"]
check_vars = {algo: tk.BooleanVar() for algo in algorithms}

# Submit button
submit_data_button = tk.Button(root, text="Submit", command=get_input)
submit_data_button.pack(pady=10)

# Create checkboxes
for algo, var in check_vars.items():
    chk = tk.Checkbutton(checkbox_frame, text=algo, variable=var)
    chk.pack(anchor="w")  # Align to the left

user_search = tk.Label(root, text="Search for: ")
user_search.pack(pady=5)

search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

submit_search_button = tk.Button(root, text="Submit", command=lin_search)
submit_search_button.pack(pady=10)

# Label to display results
result = tk.Label(root, text="", wraplength=250)
result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
