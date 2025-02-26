import sort_algos

import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

# generate random data 
def random_list(size):
    return [random.randint(1, 9999) for _ in range(size)]

def get_input(): 
    global sorted_data # we need to call it back for linear search
    try:
        num_data_points = int(data_entry.get())

        if num_data_points < 0: # prompt error if entered value is less than zero
            raise ValueError
        
        data = random_list(num_data_points)  # generate random values
    except ValueError:  # prompts error if a letter is deteccted 
        result.config(text="Please only enter numbers greater than zero")
        return

    # Check which sorting algorithm is selected
    selected_algorithms = [algo for algo, var in check_vars.items() if var.get()]

    data_results = f"Data before sorting: {data}\n\n" # print unsorted data 

    # store all execution times and selected algos since we want to make a bar graph later on
    execution_times = []
    algorithms = []

    for algo in selected_algorithms:    # for selected algos, sort data and print results
        start_time = time.time()
        if algo == "Bubble Sort":
            sorted_data = sort_algos.bubble_sort(data)  
        elif algo == "Merge Sort":
            sorted_data = sort_algos.merge_sort(data)  
        elif algo == "Quick Sort":
            sorted_data = sort_algos.quick_sort(data)  
        elif algo == "Radix Sort":
            sorted_data = sort_algos.lsd_radix_sort(data)

        end_time = time.time()
        execution_time = end_time - start_time # calculate effiency of each search algo

        execution_times.append(execution_time)
        algorithms.append(algo)
        data_results += f"Sorted Data for {algo}: {sorted_data}\n"
        data_results += f"Execution time: {execution_time:.6f} seconds\n\n"

    current_text = result.cget("text")
    result.config(text=current_text + data_results)

    # create bar graph of all execution times
    fig = plt.figure(figsize=(8, 5)) 
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in algorithms]
    axes = fig.add_subplot(1,1,1)
    axes.set_ylim(0, max(execution_times) * 1.2)  
    bars = [plt.bar(algorithms, [0] * len(algorithms), color=colors)]
    num_frames = 100
    nanoseconds_lists = [np.linspace(0, time, num_frames) for time in execution_times]
    def animate(i):
        # Update the height of each bar based on the current frame
        for j, bar in enumerate(bars[0]):
            bar.set_height(nanoseconds_lists[j][i])  # Update bar height for each algorithm
    plt.xlabel("Sorting Algorithm")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Sorting Algorithm Execution Times")
    anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=100,
                             interval=0.10)
    plt.show()

def lin_search():
    try:
        user_search = int(search_entry.get()) # take user entry for linear search
    except ValueError:
        result.config(text="Please enter a valid integer")
        return

    current_text = result.cget("text")

    search_result = sort_algos.linear_search(sorted_data, user_search)

    if search_result != -1:
        result.config(text=current_text + f"{user_search} found at index {search_result}")
    else:
        result.config(text=current_text + f"{user_search} not found in the data")

def reset_data():
    data_entry.delete(0, 'end')
    search_entry.delete(0, 'end')

    for clear_checkbox in checkbox_frame.winfo_children():
        clear_checkbox.deselect()

root = tk.Tk()
root.title("Group Project # 1 Algorithm Analyzer Tool")

# label for data points input
data_points = tk.Label(root, text="Enter number of data points:")
data_points.pack(pady=5)

# creates text box for data points input
data_entry = tk.Entry(root, width=30)
data_entry.pack(pady=5)

# frame to hold the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=5)

# sorting algorithms options
algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort", "Select All"]
check_vars = {algo: tk.BooleanVar() for algo in algorithms}

# first submit button
submit_data_button = tk.Button(root, text="Submit", command=get_input)
submit_data_button.pack(pady=10)

# reset button
reset_data_button = tk.Button(root, text="Reset", command=reset_data)
reset_data_button.pack(pady=5)

# create checkboxes
for algo, var in check_vars.items():
    chk = tk.Checkbutton(checkbox_frame, text=algo, variable=var)
    chk.pack(anchor="w")

# label prompting user search
user_search = tk.Label(root, text="Search for: ")
user_search.pack(pady=5)

# creates text box for search input
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=5)

# second submit button
submit_search_button = tk.Button(root, text="Submit", command=lin_search)
submit_search_button.pack(pady=10)

# Label to display results
result = tk.Label(root, text="", wraplength=250)
result.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

# tkinter