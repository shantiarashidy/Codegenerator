import openai
import tkinter as tk
from tkinter import scrolledtext

# Set your OpenAI API key here
openai.api_key = 'your-api-key'

# Function to generate Python code based on the prompt
def generate_code(prompt):
    # Send the prompt to OpenAI to generate Python code using the old API
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate model for this version
        prompt=prompt,  # The prompt describing the code you want to generate
        max_tokens=150,  # Maximum number of tokens (words or pieces of words)
        temperature=0.5  # Controls creativity (higher values lead to more creative outputs)
    )
    
    # Return the generated code as a string
    return response['choices'][0]['text'].strip()

# Function to be triggered when the "Generate Code" button is clicked
def on_generate_code():
    prompt = prompt_entry.get()  # Get the user input (prompt)
    generated_code = generate_code(prompt)  # Generate code based on the prompt
    output_text.delete(1.0, tk.END)  # Clear any previous code
    output_text.insert(tk.END, generated_code)  # Insert the newly generated code into the output area

# Create the main window for the Tkinter GUI
root = tk.Tk()
root.title("Python Code Generator")

# Label explaining the purpose of the input field
label = tk.Label(root, text="Enter a prompt to generate Python code:")
label.pack(pady=10)

# Input field for the user to enter their prompt
prompt_entry = tk.Entry(root, width=50)
prompt_entry.pack(pady=10)

# Button that triggers code generation
generate_button = tk.Button(root, text="Generate Code", command=on_generate_code)
generate_button.pack(pady=10)

# Output area to display the generated code (scrollable text widget)
output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
