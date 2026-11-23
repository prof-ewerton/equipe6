from interface.ui import Ui
from install import  install

def main():
    install()
    ui = Ui()
    ui.show()

if __name__ == "__main__":
    main()