from interface.ui import Ui
from install import  install
from database.missao_repository import MissaoRepository
from services.missao_service import MissaoService

def main():
    install()
    ui = Ui(missao_service=MissaoService(MissaoRepository()))
    ui.show()

if __name__ == "__main__":
    main()