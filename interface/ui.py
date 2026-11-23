from services.missao_service import MissaoService

class Ui:

    def __init__(self, missao_service: MissaoService):

        self.MENU_OPTIONS = [
            (3, "Missão", self.menu_entity_three),
        ]
        
        self.missao_service = missao_service

    def show(self):
        while True:
            print("\n===== Império dos Robôs =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== TEMA DA EQUIPE =====")
        print("= Entidade do Estudante ==")
        
    def menu_entity_three(self):
        while True:
            print("\n===== Império dos Robôs =====")
            print("= Missão ==")
            
            print("""
1. Cadastrar Missão
0. Voltar
            """)
            opc = int(input("Escolha uma opção (digite o número): "))
            
            match opc:
                case 1:
                    nome = input("Insira o nome: ")
                    duracao = int(input("Insira a duração: "))
                    concluida = True if input("A missão foi concluída? (s/N): ").lower() == "s" else False
                    print("\nEscreva exatamente como mostrado, sem acentos ou caracteres especiais (ç)")
                    categoria = input("Insira a categoria (combate, exploracao, resgate): ").lower()
                    
                    res = self.missao_service.criar(
                        nome=nome,
                        duracao=duracao,
                        concluida=concluida,
                        categoria=categoria
                    )
                    
                    print("[RESULTADO]: " + res)
                case 0:
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
