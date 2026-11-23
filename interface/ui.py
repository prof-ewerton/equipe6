from service.serviceRobo import serviceRobo

class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Robôs", self.menu_entity_one),
        ]

    def show(self):
        while True:
            print("\n===== IMPÉRIO DOS ROBÔS =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break
            
            if option == "1":
                print("\n=== Seja bem-vindo(a) ao cadastro de robôs ===")
                nome = input("Digite o nome do robô: ")
                anoFabricante = int(input("Digite o ano de Fabricação do robô: "))
                ligar = ("Esse robô está ligado? [s/n]").strip().lower()
                if ligar == "s":
                    ligado = True
                    
                elif ligar == "n":
                    ligado = False
                else:
                    return ValueError("Digito inválido")
                modelo = input("Digite o modelo do robô (opcional): ")
                
                try:
                    robo_id = self.service.create(
                        nome=nome,
                        anoFabricacao=anoFabricacao,
                        ligado=ligado,
                        modelo=modelo
                        )
                except ValueError as erro:
                    print(erro)
                    return
                

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== IMPÉRIO DOS ROBÔS =====")
        print("= Entidade do Estudante ==")
