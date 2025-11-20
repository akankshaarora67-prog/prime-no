import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext # For the scrollable results box

# --- Your modified logic ---
def find_primes(start, end):
    """
    Finds all prime numbers in a given range.
    
    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        
    Returns:
        list: A list of prime numbers found.
    """
    primes_found = []
    # Start checking from 2 if the range includes negative numbers or 0/1
    for number in range(max(2, start), end + 1):
        is_prime = True
        # Optimized loop up to the square root of the number
        for divisor in range(2, int(number**0.5) + 1):
            if number % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            primes_found.append(number)
            
    return primes_found

# --- GUI Application ---

def create_app():
    """Creates and runs the Tkinter application."""
    
    def on_find_primes_click():
        """
        Event handler for the "Find Primes" button.
        Validates input, calls find_primes, and displays the result.
        """
        # 1. Clear the results box
        result_box.config(state=tk.NORMAL) # Must be normal to edit
        result_box.delete("1.0", tk.END)
        
        try:
            # 2. Get and validate input
            a = int(start_var.get())
            b = int(end_var.get())
            
            if a > b:
                result_box.insert(tk.END, "Error: Starting number must be smaller than the ending number.")
                return

            if a < 0 or b < 0:
                result_box.insert(tk.END, "Info: Checking for positive primes only (starting from 2).\n\n")

            # 3. Call the logic function
            primes_list = find_primes(a, b)
            
            # 4. Display the results
            if not primes_list:
                result_box.insert(tk.END, f"No prime numbers found between {a} and {b}.")
            else:
                result_box.insert(tk.END, f"Prime numbers between {a} and {b}:\n\n")
                # Format the list with commas for readability
                result_string = ", ".join(map(str, primes_list))
                result_box.insert(tk.END, result_string)

        except ValueError:
            # Handle cases where input is not an integer
            result_box.insert(tk.END, "Error: Start and End numbers must be valid integers.")
        
        finally:
            # Set result box back to read-only
            result_box.config(state=tk.DISABLED)


    
    root = tk.Tk()
    root.title("Prime Number Finder")
    
    
    mainframe = ttk.Frame(root, padding="12 12 12 12")
    mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    
    start_var = tk.StringVar(value="2") 
    end_var = tk.StringVar(value="100") 
    ttk.Label(mainframe, text="Start Number:").grid(row=0, column=0, sticky=tk.W)
    start_entry = ttk.Entry(mainframe, width=15, textvariable=start_var)
    start_entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

    
    ttk.Label(mainframe, text="End Number:").grid(row=1, column=0, sticky=tk.W)
    end_entry = ttk.Entry(mainframe, width=15, textvariable=end_var)
    end_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

  
    find_button = ttk.Button(mainframe, text="Find Primes", command=on_find_primes_click)
    find_button.grid(row=2, column=1, sticky=tk.E, pady=10)

    
    ttk.Label(mainframe, text="Results:").grid(row=3, column=0, sticky=tk.W)
    result_box = scrolledtext.ScrolledText(mainframe, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
    result_box.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))
    
    
    mainframe.columnconfigure(1, weight=1)
    mainframe.rowconfigure(4, weight=1)

    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
        
    
    start_entry.focus()
    
    
    root.mainloop()


if __name__ == "__main__":
    create_app()
