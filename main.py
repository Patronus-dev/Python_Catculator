import tkinter as tk

window = tk.Tk()

# calculator title
tk.Label(
    master=window,
    text='CAT🐈CULATOR',
    font=("Comic Sans MS", 16),
    height=2
).grid(row=0, column=0, columnspan=3)

# C buttons style
btn_clear = tk.Button(
    master=window,
    text='C',
    command=lambda: insert_number_in_calc_result('C'),
    height=2,
    bg="orange"
)
btn_clear.grid(row=0, column=3, sticky="nsew")

# Show result
lbl_calc_result = tk.Label(
    master=window,
    text='0',
    width=35,
    height=2,
    anchor='e',
    font=("Arial", 20),
    bg="white",
    relief="sunken"
)
lbl_calc_result.grid(row=1, column=0, columnspan=4)

# buttons
calc_keys = [
    {'text': '7', 'command': lambda: insert_number_in_calc_result('7')},
    {'text': '8', 'command': lambda: insert_number_in_calc_result('8')},
    {'text': '9', 'command': lambda: insert_number_in_calc_result('9')},
    {'text': '+', 'command': lambda: insert_number_in_calc_result('+')},
    {'text': '4', 'command': lambda: insert_number_in_calc_result('4')},
    {'text': '5', 'command': lambda: insert_number_in_calc_result('5')},
    {'text': '6', 'command': lambda: insert_number_in_calc_result('6')},
    {'text': '-', 'command': lambda: insert_number_in_calc_result('-')},
    {'text': '1', 'command': lambda: insert_number_in_calc_result('1')},
    {'text': '2', 'command': lambda: insert_number_in_calc_result('2')},
    {'text': '3', 'command': lambda: insert_number_in_calc_result('3')},
    {'text': '*', 'command': lambda: insert_number_in_calc_result('*')},
    {'text': '.', 'command': lambda: insert_number_in_calc_result('.')},
    {'text': '0', 'command': lambda: insert_number_in_calc_result('0')},
    {'text': '/', 'command': lambda: insert_number_in_calc_result('/')},
    {'text': '=', 'command': lambda: insert_number_in_calc_result('=')},
]


def check_last_number_is_decimal(current):
    for char in current[::-1]:
        if char == '.':
            return True
        if char in ['+', '-', '*', '/']:
            return False
    return False


def insert_number_in_calc_result(btn_text):
    current = lbl_calc_result['text']
    if btn_text == 'C':
        lbl_calc_result['text'] = '0'
    elif current == '0':
        lbl_calc_result['text'] = btn_text
    elif btn_text == '=':
        try:
            result = str(eval(current))
            lbl_calc_result['text'] = result
        except:
            lbl_calc_result['text'] = 'Error'
    elif btn_text == '.':
        if not check_last_number_is_decimal(current):
            lbl_calc_result['text'] += btn_text
    elif btn_text in ['+', '-', '*', '/'] and current[-1] in ['+', '-', '*', '/']:
        lbl_calc_result['text'] = current[:-1] + btn_text
    else:
        lbl_calc_result['text'] += btn_text


# buttons from row 2 onwards
for i, calc_key in enumerate(calc_keys):
    btn = tk.Button(
        master=window,
        text=calc_key['text'],
        command=calc_key['command'],
        height=2
    )
    row = (i // 4) + 2  # چون از ردیف ۲ شروع می‌کنیم
    col = i % 4
    btn.grid(row=row, column=col, sticky="nsew")

window.mainloop()
