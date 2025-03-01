import sort_algos

import random
import time
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib import animation
from tkinter import * 
from tkinter.ttk import *
import numpy as np

# generate random data 
def random_list(size):
    return [random.randint(1, 9999) for _ in range(size)]

def get_input(): 
    # we need to call it back for linear search
    global sorted_data

    # ensures that the entries are only integers greater than 0
    try:
        num_data_points = int(array_size_entry.get())

        # prompt error if entered value is less than zero
        if num_data_points < 0:
            raise ValueError
        
        # generate random values
        data = random_list(num_data_points)

    # prompts error if a letter is detected 
    except ValueError:
        result.insert("1.0", "Please only enter positive values.\n")
        return

    # Check which sorting algorithm is selected
    selected_algorithms = [algo for algo, var in check_vars.items() if var.get()]

    data_results = f"Data before sorting: {data}\n\n" # print unsorted data 

    # store all execution times and selected algos since we want to make a bar graph later on
    execution_times = []
    algorithms = []

    # for selected algos, sort data and print results
    for algo in selected_algorithms:
        start_time = time.time_ns()
        if algo == "Bubble Sort":
            sorted_data = sort_algos.bubble_sort(data)  
        elif algo == "Merge Sort":
            sorted_data = sort_algos.merge_sort(data)  
        elif algo == "Quick Sort":
            sorted_data = sort_algos.quick_sort(data)  
        elif algo == "Radix Sort":
            sorted_data = sort_algos.lsd_radix_sort(data)
       
        end_time = time.time_ns()

        # calculate effiency of each search algo
        execution_time = end_time - start_time

        execution_times.append(execution_time)
        algorithms.append(algo)
        data_results += f"Sorted Data for {algo}: {sorted_data}\n"
        data_results += f"Execution time: {execution_time:.6f} nano seconds\n\n"

    current_text = result.get("1.0", "end")
    result.insert("1.0", current_text + data_results)

    # create bar graph of all execution times
    fig = plt.figure(figsize=(8, 5)) 
    colors = [f"#{random.randint(0, 0xFFFFFF):06x}" for _ in algorithms]
    axes = fig.add_subplot(1,1,1)
    plt.ticklabel_format(style='sci', scilimits=(0, 0))
    axes.set_ylim(0, max(execution_times) * 0.2)  
    bars = [plt.bar(algorithms, [0] * len(algorithms), color=colors)]
    num_frames = 500
    nanoseconds_lists = [np.linspace(0, time, num_frames) for time in execution_times]
    def animate(i):
        
        # update the height of each bar based on the current frame
        for j, bar in enumerate(bars[0]):

            # update bar height for each algorith
            bar.set_height(nanoseconds_lists[j][i])
        
    plt.xlabel("Sorting Algorithm")
    plt.ylabel("Execution Time (nanoseconds)")
    plt.title("Sorting Algorithm Execution Times")
    anim=animation.FuncAnimation(fig,animate,repeat=False,blit=False,frames=100,
                             interval=0.02)
    
    plt.show()

def lin_search():
    try:
        # take user entry for linear search
        user_search = int(search_entry.get())

        # checks that the search value is positive only
        if user_search < 0:
            raise ValueError
    except ValueError:
        result.insert("1.0", "Please enter a positive integer.\n")
        return
    search_result = sort_algos.linear_search(sorted_data, user_search)

    if search_result != -1:
        result.insert("1.0", f"{user_search} is found at index {search_result}\n")
    else:
        result.insert("1.0", f"{user_search} is not found in the data\n")
        
# clears everything
def reset_data():
    array_size_entry.delete(0, 'end')
    search_entry.delete(0, 'end')
    input_entry.delete(0, 'end')

    for clear_checkbox in checkbox_frame.winfo_children():
        clear_checkbox.deselect()
    result.delete("1.0", "end")
    plt.close()

# selects all the algos
def select_all():
    for all_checkbox in checkbox_frame.winfo_children():
        all_checkbox.select()
 
root = tk.Tk()
root.title("Group Project # 1 Algorithm Analyzer Tool")

# generates an n-sized array of random number based on the array size entered
array_size = tk.Label(root, text="Enter array size:")
array_size.grid(row = 2, column = 0, rowspan=1)

# creates text box for n-sized array entry
array_size_entry = tk.Entry(root, width=30)
array_size_entry.grid(row = 3, column = 0, padx = 25)

# frame to hold the checkboxes
checkbox_frame = tk.Frame(root)
checkbox_frame.grid(row = 4, column = 0)

# sorting algorithms options
algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Radix Sort"]
check_vars = {algo: tk.BooleanVar() for algo in algorithms}
print(check_vars)

# select all button
select_all_button = tk.Button(root, text="Select All", command=select_all)
select_all_button.grid(row=5, column=0)

# submit button
submit_data_button = tk.Button(root, text="Submit", command=get_input)
submit_data_button.grid(row = 6, column = 0)

# reset button
reset_data_button = tk.Button(root, text="Reset", command=reset_data)
reset_data_button.grid(row = 7, column = 0)

# label prompting user search
user_search = tk.Label(root, text="Search for: (Linear Search)")
user_search.grid(row = 8, column = 0)

# creates text box for search input
search_entry = tk.Entry(root, width=30)
search_entry.grid(row = 9, column = 0)

# linear search submit button
search_button = tk.Button(root, text="Submit", command=lin_search)
search_button.grid(row = 10, column = 0, pady=15)

# create checkboxes
for algo, var in check_vars.items():
    chk = tk.Checkbutton(checkbox_frame, text=algo, variable=var)
    chk.pack(anchor="w")

# label to display results
result = tk.Text(root, height=30, width=60)
result.grid(row = 0, column = 1, rowspan = 8, pady = 40, padx = 25)

# run the Tkinter event loop
root.mainloop()

# tkinter