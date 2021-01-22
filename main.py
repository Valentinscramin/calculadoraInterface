from calculadora_factories import make_root, make_display, make_label, \
    make_buttons
from calculadora_gui import CalculatorGui
from calculadora_actions import calculate


def main():
    root = make_root()
    display = make_display(root, row=1, column=0, columnspan=5, sticky='news')
    display.grid_configure(pady=(0, 10))
    label = make_label(root, row=0, column=0, columnspan=5, sticky='news')
    buttons = make_buttons(root, starting_row=2)

    calculadora_gui = CalculatorGui(root, label, display, buttons, calculate)
    calculadora_gui.start()


if __name__ == '__main__':
    main()