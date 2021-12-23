
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


arquivo = pd.read_excel('Dados_Cobaia.xlsx')



def graficoPizza():
    Entregue = arquivo.loc[arquivo['Status']=='Entregue']
    Pendente = arquivo.loc[arquivo['Status']=='Pendente']
    plt.title('Status dos pedidos')
    plt.pie([len(Entregue),len(Pendente)], labels=['Entregue','Pendente'], autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

graficoPizza()

