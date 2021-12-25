import PySimpleGUI as sg
from Scripts.insert_dados import InsertDados
from Scripts.price_end import PrecoFinal

from Design.menu_principal import MenuPrincipal
from Design.nova_encomenda import NovaEncomenda
from Design.listar_encomendas import ListarEncomendas
from Design.baixa_encomenda import BaixaEncomenda

menu, nova_encomenda, lista_encomenda = MenuPrincipal.menu_principal(), None, None
menu_encomenda, dar_baixa_encomenda, dados_cliente = None, None, None
popup_baixa, menu_encomenda_atalho, salgadinhos = None, None, None


while True:
    janela, evento, valor = sg.read_all_windows()

    ##########################################################################
    ##########################################################################
    ###########################JANELA PRINCIPAL###############################
    ##########################################################################
    ##########################################################################

    #verificar se F1 foi pressionado
    

    if janela == menu and evento == sg.WIN_CLOSED:
        break

    if janela == menu:
        if evento == 'Nova encomenda':
            nova_encomenda = NovaEncomenda.nova_encomenda()
            nova_encomenda.un_hide()
            
        elif evento == 'Listar encomendas':
            menu_encomenda = ListarEncomendas.menu_encomendas()

        elif evento == 'Dar baixa em encomenda':
            dar_baixa_encomenda = BaixaEncomenda.baixa_encomenda()

        elif evento == 'Sair':
            break
    ##########################################################################
    ##########################################################################
    ###########################NOVA ENCOMENDA#################################
    ##########################################################################
    ##########################################################################
    if janela == nova_encomenda and evento == sg.WIN_CLOSED or janela == nova_encomenda and evento == 'Voltar':
        nova_encomenda.hide()


    if janela == nova_encomenda and evento == 'Confirmar':
        InsertDados(
            valor["nome_cliente"], 
            valor["data_entrega"],
            valor["bolo_aniversario"],
            valor["bolo_casamento"],
            valor["qtd_mini"],
            valor["qtd_normal"],
        ).inserir_dados()

        sg.popup("Encomenda cadastrada com sucesso!")
        nova_encomenda.hide()

        
    ##########################################################################
    ##########################################################################
    ###########################LISTAR ENCOMENDAS##############################
    ##########################################################################
    ##########################################################################

    if janela == menu_encomenda and evento == sg.WIN_CLOSED or janela == menu_encomenda and evento == 'Voltar':
        menu_encomenda.hide()


    if janela == lista_encomenda and evento == sg.WIN_CLOSED or janela == lista_encomenda and evento == 'Voltar':
        lista_encomenda.hide()
        menu_encomenda.un_hide()
    
    if janela == menu_encomenda and evento == 'Encomendas em aberto':
        lista_encomenda = ListarEncomendas.listar_encomendas("Pendente")
        menu_encomenda.hide()
    
    if janela == menu_encomenda and evento == 'Encomendas fechadas':
        lista_encomenda = ListarEncomendas.listar_encomendas("Concluído")
        menu_encomenda.hide()

    ##########################################################################
    ##########################################################################
    ###########################BAIXA EM ENCOMENDA#############################
    ##########################################################################
    ##########################################################################

    if janela == dar_baixa_encomenda and evento == sg.WIN_CLOSED or janela == dar_baixa_encomenda and evento == 'Voltar':
        dar_baixa_encomenda.hide()

    
    if janela == dar_baixa_encomenda and evento == 'Confirmar':
        id = valor['id']
        kg_aniversario = valor['kg_bolo_aniversario']
        kg_casamento = valor['kg_bolo_casamento']

        preco_final = PrecoFinal(id, kg_aniversario, kg_casamento).modificar_status()

        dar_baixa_encomenda.hide()

        popup_baixa = BaixaEncomenda.popup_baixa(preco_final)

    if janela == popup_baixa and evento == sg.WIN_CLOSED or janela == popup_baixa and evento == 'Ok':
        popup_baixa.hide()


