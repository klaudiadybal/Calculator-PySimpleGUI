import PySimpleGUI as sg
import cli as calculator

sg.theme("Black")

label1 = sg.Text("Enter first number:")
input1 = sg.Input(tooltip="Enter first number:", key="first_number")

label2 = sg.Text("Enter second number:")
input2 = sg.Input(tooltip="Enter second number:", key="second_number")

add_button = sg.Button(" +  ", key="add")
sub_button = sg.Button("  -  ", key="sub")
mul_button = sg.Button("  *  ", key="mul")
div_button = sg.Button("  /  ", key="div")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
output_label = sg.Text("", key="output")

window = sg.Window("Calculator", layout=[[col1, col2],
                                         [add_button, sub_button, mul_button, div_button],
                                         [output_label]])

while True:

    event, values = window.read()
    print(event)
    print(values)

    try:
        first_number = int(values['first_number'])
        second_number = int(values['second_number'])
        match event:

            case "add":
                result = calculator.addition(first_number, second_number)
                window['output'].update(value=result)

            case "sub":
                result = calculator.subtraction(first_number, second_number)
                window['output'].update(value=result)

            case "mul":
                result = calculator.multiplication(first_number, second_number)
                window['output'].update(value=result)

            case "div":
                result = calculator.division(first_number, second_number)
                window['output'].update(value=result)

            case sg.WIN_CLOSED:
                break
    except ValueError:
        sg.popup("Provide two numbers first.")
    except TypeError:
        break

window.close()




