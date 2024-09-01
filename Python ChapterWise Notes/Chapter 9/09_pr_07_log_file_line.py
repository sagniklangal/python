content = True
i = 1
with open("log.txt","r") as a:
    while content:
        content = a.readline()
        if "python" in content.lower():
            print(content)
            print(f"Yes python is present on line no {i}")
        i+=1
'''This Python code reads a file named "log.txt" and searches for the word "python" (case-insensitive) in each line of the file. If it finds the word "python" in a line, it prints that line and the line number where "python" was found.

Here's a step-by-step explanation of the code:

1. `content = True`: This line initializes a variable named `content` to `True`. This variable is used to control the loop, and it will be set to `False` when the end of the file is reached.

2. `i = 1`: This line initializes a variable named `i` to 1. `i` will be used to keep track of the line number in the file.

3. `with open("log.txt", "r") as a:`: This line opens the file "log.txt" in read-only mode using a context manager. It assigns the file object to the variable `a`. Using a context manager ensures that the file is properly closed after it's no longer needed.

4. `while content:`: This line starts a `while` loop that continues as long as the `content` variable is `True`. Initially, `content` is set to `True`, so the loop begins.

5. `content = a.readline()`: Inside the loop, this line reads the next line from the file using the `readline()` method and assigns it to the `content` variable. If the end of the file is reached, `readline()` will return an empty string, which will set `content` to `False` and exit the loop.

6. `if "python" in content.lower():`: This line checks if the word "python" (case-insensitive) is present in the current line. To make it case-insensitive, it converts the line to lowercase using the `lower()` method.

7. If the word "python" is found in the line, it enters the `if` block:
   - `print(content)`: This line prints the line from the file that contains the word "python."
   - `print(f"Yes python is present on line no {i}")`: This line prints a message indicating that "python" is present on the current line, along with the line number `i`.

8. `i += 1`: Regardless of whether "python" is found or not, this line increments the line number `i` by 1.

9. The loop continues to the next iteration to read the next line from the file.

10. When the end of the file is reached, and there are no more lines to read, the `readline()` method will return an empty string, which sets `content` to `False`, and the loop exits.

In summary, this code reads a file line by line, checks if the word "python" (case-insensitive) is present in each line, and prints the lines containing "python" along with their line numbers.'''