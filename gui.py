import search_algos

import random
import time
import tkinter as tk

def run_search_algos(): # I couldn't get the code to run in the terminal so to make it work with the algos file I had to run it like this
    search_algos.run_search_algos()

# generate random data 
def random_list(size):
    return [random.randint(1, 9999) for _ in range(size)]


def get_input():    # allow user to enter how many data points they want to generate
    user_text = entry.get()  
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
        data_results += f"Sorted Data for {algo}: {sorted_data}\n"
        data_results += f"Execution time: {end_time - start_time:.6f} seconds\n\n"

    result.config(text=data_results)

root = tk.Tk()
root.title("Select Sorting Method")

# Create a label for user input
label = tk.Label(root, text="Enter number of data points:")
label.pack(pady=5)

# Create an entry box for user input
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Frame to hold the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=5)

# Sorting algorithms options
algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Linear Search"]
check_vars = {algo: tk.BooleanVar() for algo in algorithms}

# Create checkboxes
for algo, var in check_vars.items():
    chk = tk.Checkbutton(checkbox_frame, text=algo, variable=var)
    chk.pack(anchor="w")  # Align to the left

# Submit button
button = tk.Button(root, text="Submit", command=get_input)
button.pack(pady=10)

# Label to display results
result = tk.Label(root, text="", wraplength=250)
result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
