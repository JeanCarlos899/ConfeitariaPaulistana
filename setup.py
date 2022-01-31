import os
import sys

try:
    import PySimpleGUI as sg

    from Scripts.insert_dados import InsertDados
    from Scripts.finalize_order import FinalizeOrder
    from Scripts.new_chart import NewChart
    from Scripts.reports import Relatorios
    from Scripts.edit_order import EditDados
    from Scripts.sqlite import SQLite

    from Design.menu_principal import MenuPrincipal
    from Design.nova_encomenda import NovaEncomenda
    from Design.listar_encomendas import ListarEncomendas
    from Design.baixa_encomenda import BaixaEncomenda
    from Design.graficos import Graficos
    from Design.relatorios import FrontRelatorio
    from Design.deletar_encomenda import DeletarEncomenda
    from Design.editar_encomenda import EditarEncomenda
    from Design.faturamento import Faturamento
    from Scripts.revenues import Revenues
    from Design.lucro_mes import Lucromensal
    from Scripts.pronfit_in_the_month import Gasto
    from Scripts.sicronizar import Sicronizar
    from Scripts.cadastrar_caminho import Criar
    from Scripts.cadastrar_caminho import Editar
    from Design.criar_caminho import FrtCam
    from Design.recuperar import Recuperar
    from Design.login import Login
except ImportError:
    os.system("pip3 install -r requirements.txt")
    print("Bibliotecas instaladas com sucesso!")
    print("Reabra o programa.")
    sys.exit()

class Program:

    def __init__(self) -> object:

        self.login = Login()

        if self.login():

            # Menu initializes next to the class
            self.menu = MenuPrincipal.menu_principal()

            # Definition of windows in the builder
            self.nova_encomenda = None
            self.dados_cliente = None
            self.lista_encomenda = None
            self.menu_encomenda = None
            self.dar_baixa_encomenda = None
            self.salgadinhos = None
            self.mais_informacoes = None
            self.graficos = None
            self.relatorios = None
            self.deletar_encomenda = None 
            self.editar_encomenda = None
            self.faturamento = None
            self.lucro_do_mes = None
            self.local = None
            self.recuperar = None

            # window values
            self._window = None
            self._event = None
            self._value = None

            # id
            self._id = None

            # Program startup run method
            self.__run()
    

    # deactivate buttons
    def buttons(self, on_off) -> None:
        keys = {
            1: "-NOVA_ENCOMENDA-", 
            2: "-LISTAR_ENCOMENDAS-",
            3: "-DAR_BAIXA_ENCOMENDA-",
            4: "-EDITAR_ENCOMENDA-",
            5: "-GRAFICOS-",
            6: "-RELATORIOS-",
            7: "-FATURAMENTO-",
            8: "-DELETAR_ENCOMENDA-",
            9: "-LUCRO_MENSAL-",
            10: "-LOCAL-",
            11: "-RECUPERAR-",
            12: "-SAIR-"
        }

        if on_off == "on":
            for key in range(len(keys)):
                self.menu[keys[key+1]].update(disabled=False)
        else: 
            for key in range(len(keys)):
                self.menu[keys[key+1]].update(disabled=True)
    
    # update the list of orders
    def update_list(self, concluded, pending) -> None:
        if concluded == True:
            self._window["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Concluído"'
                    )
                )
            self.menu_encomenda["-STATUS_CONCLUIDO-"].update(True)
        elif pending == True:
            self._window["-INDEX_ENCOMENDA-"].update(
                values=SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                    )
                )
            self.menu_encomenda["-STATUS_PENDENTE-"].update(True)
    
    # functions menu
    def functionsMenu(self, event) -> object:

        if event == sg.WIN_CLOSED or event == "-SAIR-":
            local = './Config/caminhos.csv'
        
            try:    
                if os.path.getsize(local) == 0:
                    sg.popup_ok("Não há caminhos cadastrados no sistema", "Cadastre um para que possa ser feito o backup" )
                    return False 
                else:
                    localOriginal = 'dados.db'
                    file = local

                    if os.path.exists('backup_dados.db'):
                        os.remove('backup_dados.db')

                    with open(file, 'r') as f:
                        caminhos = f.readlines() 
                    
                    novolocal = caminhos[0].strip()          
                    sincronizar = Sicronizar(localOriginal, novolocal)
                    sincronizar.sincronizar()

                    return False

            except FileNotFoundError:
                sg.popup_ok("Caminho inválido, edite-o. Para que o backup possa ser feito.")
                Editar.editar()

                return False

        elif event == "-NOVA_ENCOMENDA-":
            self.nova_encomenda = NovaEncomenda.nova_encomenda("Nova Encomenda")
            self.buttons("off")

        elif event == "-LISTAR_ENCOMENDAS-":
            self.menu_encomenda = ListarEncomendas.listar_encomendas("Pendente")
            self.buttons("off")

        elif event == "-DAR_BAIXA_ENCOMENDA-":
            self.dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()
            self.buttons("off")

        elif event == "-GRAFICOS-":
            self.graficos = Graficos.menu_graficos()
            self.buttons("off")

        elif event == "-RELATORIOS-":
            self.relatorios = FrontRelatorio.menu_relatorios()
            self.buttons("off")

        elif event == "-FATURAMENTO-":
            self.faturamento = Faturamento.faturamento()
            self.buttons("off")

        elif event == "-EDITAR_ENCOMENDA-":
            self.editar_encomenda = EditarEncomenda.listar_encomendas("Pendente")
            self.buttons("off")

        elif event == "-DELETAR_ENCOMENDA-":
            self.deletar_encomenda = DeletarEncomenda.deletar_encomenda("Pendente")
            self.buttons("off")

        elif event == "-LUCRO_MENSAL-":
            self.lucro_do_mes = Lucromensal.lucro()
            self.buttons("off")

        elif event == "-LOCAL-":
            self.local = FrtCam.tela()
            self.buttons("off")

        elif event == "-RECUPERAR-":
            self.recuperar = Recuperar.escolher_arquivo()
    
    # insert new order into the database
    def newOrder(self, event, value) -> None:

        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.nova_encomenda.hide()
            self.buttons("on")
            return

        elif event == "-CONFIRMAR-":
            status_menssage = InsertDados([
                str(value["-NOME_CLIENTE-"]), 
                str(value["-DATA_ENTREGA-"]), 
                str(value["-HORA_ENTREGA-"]), 
                int(value["-BOLO_ANIVERSARIO-"]),
                int(value["-BOLO_CASAMENTO-"]), 
                int(value["-QTD_MINI-"]), 
                int(value["-QTD_NORMAL-"]), 
                str(value["-INFO_COMPLEMENTARES-"]) 
            ])

            msg = status_menssage()

            if msg == True:
                sg.popup("Dados inseridos com sucesso!", title="Sucesso!")
                self.nova_encomenda.hide()
                self.buttons("on")
                return
            else:
                sg.popup(msg, title="Erro!")
                return
    
    # llist orders in database
    def listOrder(self, event, value) -> object:
        
        status_concluido = value["-STATUS_CONCLUIDO-"] 
        status_pendente = value["-STATUS_PENDENTE-"]

        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.menu_encomenda.hide()
            self.buttons("on")
            return

        elif event == "-FILTRAR-":
            self.update_list(status_concluido, status_pendente)
            return
            
        elif event == "-MAIS_INFORMACOES-":
            try:
                index = int(value["-INDEX_ENCOMENDA-"][0])

                if status_concluido == True:
                    self.mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Concluído", index
                        )
                    self.menu_encomenda.hide()
                    return
    
                elif status_pendente == True:
                    self.mais_informacoes = ListarEncomendas.mais_informacoes(
                        "Pendente", index
                        )
                    self.menu_encomenda.hide()
                return
            except:
                sg.popup("Selecione uma encomenda para mais informações!")
                return
    
    # low the order in the database
    def lowOrder(self, event, value) -> float:

        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.dar_baixa_encomenda.hide()
            self.buttons("on")
            return

        elif event == "-FINALIZAR_ENCOMENDA-":
            try:
                index_encomenda = value["-TABLE_LISTAR_ENCOMENDA-"]
                kg_aniversario = value["-BOLO_ANIVERSARIO-"]
                kg_casamento = value["-BOLO_CASAMENTO-"]
                lista_encomendas = SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                    )

                preco_final = FinalizeOrder(
                    lista_encomendas, index_encomenda, 
                    kg_aniversario, kg_casamento
                    ).get_preco_final()

                self.dar_baixa_encomenda["-VALOR_FINAL-"].update("R$" + str(preco_final))
                self.dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=True)
                return
            except:
                sg.popup("Selecione uma encomenda para finalizar!")
                return

        elif event == "-ATUALIZAR_LISTA-":
            self.dar_baixa_encomenda["-TABLE_LISTAR_ENCOMENDA-"].update(
                SQLite('dados.db').select(
                    'dados', '*', 'status = "Pendente"'
                )
            )

            self.dar_baixa_encomenda["-FINALIZAR_ENCOMENDA-"].update(disabled=False)
            self.dar_baixa_encomenda["-VALOR_FINAL-"].update("R$0,00")
            self.dar_baixa_encomenda["-BOLO_ANIVERSARIO-"].update(0)
            self.dar_baixa_encomenda["-BOLO_CASAMENTO-"].update(0)
            return
    
    # graphics 
    def graphics(self, event) -> object:

        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.graficos.hide() 
            self.buttons("on")

        elif event == "-STATUS_PEDIDO-":
            NewChart.graficoPizza()

        elif event == "-TIPO_BOLO-":
            NewChart.graficoTipoBolo()

        elif event == "-TIPO_SALGADO-":
            NewChart.graficoTipoSalgados()

        elif event == "-MENSAIS-":
            NewChart.graficoBarrasPedidos()

        elif event == "-LUCRO_MENSAL-":
            NewChart.graficoganho()
    
        elif event == "-LUCRO_POR_TIPO_DE_FESTAS-":
            NewChart.lucroporfesta()
    
    # reports
    def reports(self, event) -> object:      
        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.relatorios.hide()
            self.buttons("on")
        
        elif event == "-PEDIDOS_ENTREGUES-":
            Relatorios.historico_pedidos_concluido()
            sg.popup("Relatório gerado com sucesso!")

        elif event == "-PEDIDOS_NAO_ENTREGUES-":
            Relatorios.historico_pedidos_naoentregues()
            sg.popup("Relatório gerado com sucesso!")

        elif event == "-PEDIDOS_PENDENTES-":
            Relatorios.pedidos_pendentes()
            sg.popup("Relatório gerado com sucesso!")

        elif event == "-TODOS_PEDIDOS-":
            Relatorios.historico_todos_pedidos()
            sg.popup("Relatório gerado com sucesso!")
    
    # delete order from database
    def delOrder(self, event, value) -> None:

        status_concluido = value["-STATUS_CONCLUIDO-"] 
        status_pendente = value["-STATUS_PENDENTE-"]
            
        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.deletar_encomenda.hide()
            self.buttons("on")
            return
        
        elif event == "-FILTRAR-":
            self.update_list(status_concluido, status_pendente)
            return

        ##########################DELETAR ENCOMENDA###############################

        elif event == "-DELETAR_ENCOMENDA-":
            try:
                index = int(value["-INDEX_ENCOMENDA-"][0])

                if status_pendente == True:
                    lista_encomendas = SQLite('dados.db').select(
                        'dados', 'id', 'status = "Pendente"'
                    )
                elif status_concluido == True:
                    lista_encomendas = SQLite('dados.db').select(
                        'dados', 'id', 'status = "Concluído"'
                    )

                id = lista_encomendas[index][0]
                SQLite('dados.db').delete('dados', f'id={id}')

                self.update_list(status_concluido, status_pendente)

            except:
                sg.popup("Nenhuma encomenda selecionada!")
                return
    
    # edit data order from database
    def editOrder(self, event, value) -> object:

        try:
            status_concluido = value["-STATUS_CONCLUIDO-"] 
            status_pendente = value["-STATUS_PENDENTE-"]
        except:
            pass

        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.editar_encomenda.hide()
            self.buttons("on")
            return

        elif event == "-FILTRAR-":
            self.update_list(status_concluido, status_pendente)
            return

        ###############################EDITAR ENCOMENDA###########################

        elif event == "-EDITAR-":
            try:
                index = int(value["-INDEX_ENCOMENDA-"][0])

                if status_pendente == True:
                    lista_encomendas = SQLite('dados.db').select(
                        'dados', '*', 'status = "Pendente"'
                    )
                elif status_concluido == True:
                    lista_encomendas = SQLite('dados.db').select(
                        'dados', '*', 'status = "Concluído"'
                    )
                dados = lista_encomendas[index]
                self._id = dados[0]

                self.editar_encomenda.close()
                self.editar_encomenda = EditarEncomenda.edit_info()

                self.editar_encomenda["-NOME_CLIENTE-"].update(dados[1])
                self.editar_encomenda["-DATA_ENTREGA-"].update(dados[2])
                self.editar_encomenda["-HORA_ENTREGA-"].update(dados[3])
                self.editar_encomenda["-BOLO_ANIVERSARIO-"].update(dados[4])
                self.editar_encomenda["-BOLO_CASAMENTO-"].update(dados[5])
                self.editar_encomenda["-QTD_MINI-"].update(dados[6])
                self.editar_encomenda["-QTD_NORMAL-"].update(dados[7])
                self.editar_encomenda["-INFO_COMPLEMENTARES-"].update(dados[9])
            
            except:
                sg.popup("Nenhuma encomenda selecionada!")
                

        elif event == "-CONFIRMAR-":
            status_menssage = EditDados([
                str(value["-NOME_CLIENTE-"]), 
                str(value["-DATA_ENTREGA-"]), 
                str(value["-HORA_ENTREGA-"]), 
                int(value["-BOLO_ANIVERSARIO-"]),
                int(value["-BOLO_CASAMENTO-"]), 
                int(value["-QTD_MINI-"]), 
                int(value["-QTD_NORMAL-"]), 
                str(value["-INFO_COMPLEMENTARES-"]) 
            ], self._id)

            msg = status_menssage()

            if msg == True:
                sg.popup("Dados atualizados com sucesso!", title="Sucesso!")
                self.editar_encomenda.hide()
                self.buttons("on")
                return
            else:
                sg.popup(msg, title="Erro!")
                return
    
    # show full value of revenue
    def revenues(self, event, value) -> float:
        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.faturamento.close()
            self.buttons("on")

        elif event == "-FILTRAR-":
            data_inicial = value["-DATA_INICIAL-"]
            data_final = value["-DATA_FINAL-"]
            
            full_value = Revenues(data_inicial, data_final).get_value()
            self.faturamento["-VALOR_FATURAMENTO-"].update(full_value)
    
    # monthly earnings calculator
    def monthlyPronfit(self, event, value) -> float:
        if event == sg.WIN_CLOSED or event == "-EXIT-":
            self.lucro_do_mes.close()
            self.buttons("on")
        
        elif event == "-ENVIAR-":
            try:
                funcionarios = float(value['-INPUT_FUNCIONARIOS-'])
                mercadorias = float(value['-INPUT_MERCADORIAS-'])
                impostos = float(value['-INPUT_IMPOSTOS-'])
                outros = float(value['-INPUT_OUTROS-'])

                total = Gasto.descobrirGanhoMes() - (funcionarios + mercadorias + impostos + outros) 
                self.lucro_do_mes['-OUTPUT-'].update(total)
                self.lucro_do_mes['-OUTPUT-'].update(f'O lucro mensal será {total} reais')

            except ValueError:
                self.lucro_do_mes['-OUTPUT-'].update('Por favor, digite apenas números.')
    
    # register new path to database backup
    def registerPath(self, event) -> object:
        if event == sg.WIN_CLOSED or event == "-VOLTAR-":
            self.local.close()
            self.buttons("on")

        elif event == "-PROCURAR-":
            Criar.criar()

        elif event == "-EDITAR-":
            Editar.editar()
    
    # run method
    def __run(self):

        self.menu.maximize()

        while True:
            # get event
            self._window, self._event, self._value = sg.read_all_windows()

            # check if window is menu
            if self._window == self.menu:
                sair = self.functionsMenu(self._event)

                # if user want to exit                    
                if sair == False:
                    break

            # check if window is new order
            elif self._window == self.nova_encomenda:
                # call method to create new order
                self.newOrder(self._event, self._value)

            # check if window is list of orders
            elif self._window == self.menu_encomenda:
                # call method to list orders
                self.listOrder(self._event, self._value)

            # check if window is more information and exit
            elif (self._window == self.mais_informacoes and self._event == sg.WIN_CLOSED 
                or self._window == self.mais_informacoes and self._event == "-VOLTAR-"):
                # hide more information
                self.mais_informacoes.hide()
                # show list of orders
                self.menu_encomenda.un_hide()

            # check if window is low order
            elif self._window == self.dar_baixa_encomenda:
                # call method to low order
                self.lowOrder(self._event, self._value)

            # check if window graph
            elif self._window == self.graficos:
                # call method to graph
                self.graphics(self._event)

            # check if window is reports
            elif self._window == self.relatorios:
                # call method to reports
                self.reports(self._event)

            # check if window is del order
            elif self._window == self.deletar_encomenda:
                # call method to delete order
                self.delOrder(self._event, self._value)

            # check if window is edit order
            elif self._window == self.editar_encomenda:
                # call method to edit order
                self.editOrder(self._event, self._value)

            # check if window is revenues
            elif self._window == self.faturamento:
                # call method to revenues
                self.revenues(self._event, self._value)

            # check if window is monthly profit
            elif self._window == self.lucro_do_mes:
                # call method to monthly profit
                self.monthlyPronfit(self._event, self._value)

            # check if window is register path
            elif self._window == self.local:
                # call method to register path
                self.registerPath(self._event)

# run program
if __name__ == "__main__":
    # create object, this object will run the program automaticly with __run method
    program = Program()