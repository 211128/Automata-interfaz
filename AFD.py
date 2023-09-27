import tkinter as tk
from tkinter import scrolledtext

states = {
    'q0': {"1": 'q1', "2": 'q1'},
    'q1': {'-':'q2'},
    'q2': {'V':'q3', 'W':'q3'},
    'q3': {'C':'q4', 'D':'q4', 'F':'q4','G':'q4','H':'q4','I':'q4','J':'q4'
           ,'K':'q4','L':'q4','M':'q4','N':'q4','Ñ':'q4','O':'q4','P':'q4'
           ,'Q':'q4','R':'q4','S':'q4','T':'q4','U':'q4','V':'q4','W':'q4'
           ,'X':'q4'},
    'q4':{'-':'q5'},
    'q5':{"0":'q6',"1":'q6',"2":'q6',"3":'q6',"4":'q6',"5":'q6',"6":'q6',"7":'q6',"8":'q6',"9":'q6',},
    'q6':{"1":'q7',"2":'q7',"3":'q7',"4":'q7',"5":'q7',"6":'q7',"7":'q7',"8":'q7',"9":'q7'},
    'q7':{'R':'q8', 'Q':'q8', 'P':'q8', 'O':'q8', 'N':'q8', 'M':'q8', 
    'L':'q8', 'K':'q8', 'J':'q8', 'I':'q8', 'H':'q8',},
    'q8':{}

    # ...
}
def validar_automata(input_string, states, output_text):
    input_string = input_string.upper()  # Convertir a mayúsculas
    current_state = "q0"
    final_state = "q8"

    for char in input_string:
        try:
            if states[current_state][char]:
                output_text.insert(tk.END, f'Estado actual: {current_state} --> Entrada: {char}\n', 'state_info')
                current_state = states[current_state][char]
                output_text.insert(tk.END, f'Pasa A: {current_state}\n\n', 'state_info')
            else:
                error_message = f'Autómata no válido, error en el estado {current_state}'
                output_text.insert(tk.END, error_message, 'error_message')
                return {'success': False, 'message': error_message}
        except KeyError:
            error_message = f'Autómata no válido, error en el estado {current_state}'
            output_text.insert(tk.END, error_message, 'error_message')
            return {'success': False, 'message': error_message}
    
    if current_state == final_state:
        success_message = "Cadena válida"
        output_text.insert(tk.END, success_message, 'success_message')
        return {'success': True, 'message': success_message}
    else:
        failure_message = "Cadena no válida"
        output_text.insert(tk.END, failure_message, 'failure_message')
        return {'success': False, 'message': failure_message}

def validate_input():
    input_string = input_entry.get()
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)  # Limpiar salida anterior
    resultado = validar_automata(input_string, states, output_text)
    output_text.config(state=tk.DISABLED)  # Deshabilitar edición de salida
    result_label.config(text=resultado['message'])

# Crear la ventana de la aplicación principal
app = tk.Tk()
app.title("Validador de Autómata")

# Establecer el tamaño de la ventana principal y centrarlo
window_width = 800
window_height = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Aumentar el tamaño de fuente para etiquetas y campo de entrada
font_size = 16

# Crear una etiqueta y campo de entrada para la entrada
input_label = tk.Label(app, text="Entrada:", font=("Arial", font_size))
input_label.pack(pady=10)
input_entry = tk.Entry(app, font=("Arial", font_size))
input_entry.pack(padx=10, pady=10, ipadx=20, ipady=10)  # Aumentar tamaño

# Crear un botón para activar la validación
validate_button = tk.Button(app, text="Validar", font=("Arial", font_size), command=validate_input)
validate_button.pack(pady=10)

# Crear un widget de texto con desplazamiento para la salida detallada y decorada
output_text = scrolledtext.ScrolledText(app, font=("Courier", font_size), wrap=tk.WORD)
output_text.pack(fill=tk.BOTH, expand=True)
output_text.config(state=tk.DISABLED)  # Deshabilitar edición de la salida
output_text.tag_configure('state_info', foreground='green')
output_text.tag_configure('error_message', foreground='red')
output_text.tag_configure('success_message', foreground='blue')
output_text.tag_configure('failure_message', foreground='red')

# Crear una etiqueta para mostrar el resultado con un tamaño de texto más grande
result_label = tk.Label(app, text="", font=("Arial", font_size))
result_label.pack()

# Iniciar la aplicación GUI
app.mainloop()