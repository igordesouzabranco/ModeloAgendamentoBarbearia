from tkinter import *
from tkinter import ttk

class GUI():

    """Classe GUI organizada com o __init__"""
    x_pad = 4.5
    y_pad = 9
    width_entry = 45

    def __init__(self):
        
        self.window = Tk()
        self.window.wm_title("Agendamento Barbearia")

        self.txtNome = StringVar()
        self.txtCel = StringVar()
        self.txtData = StringVar()
        self.txtOpcao = StringVar()
        opcoes = ["Cabelo", "Sombrancelha", "Barba"]

        self.lnome = Label(self.window, text="Nome")
        self.lcelular = Label(self.window, text="Celular")
        self.ldata = Label(self.window, text="Data")
        self.lopcao = Label(self.window, text="Selecione Opção")
        self.entNOME = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entCEL = Entry(self.window, textvariable=self.txtCel, width=self.width_entry)
        self.entDATA = Entry(self.window, textvariable=self.txtData, width=self.width_entry)
        self.entOPCAO = ttk.Combobox(self.window, textvariable=self.txtOpcao, values=opcoes, width=self.width_entry - 3, state="readonly")

        self.listClientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnViewAll = Button(self.window, text="Ver todos os agendamentos")
        self.btnBuscar = Button(self.window, text="Buscar agendamentos")
        self.btnUpdate = Button(self.window, text="Atualizar agendamento")
        self.btnDel = Button(self.window, text="Deletar agendamento")
        self.btnClose = Button(self.window, text="Fechar", command=self.window.destroy)

        self.lnome.grid(row=0, column=0)
        self.lcelular.grid(row=1, column=0)
        self.ldata.grid(row=2, column=0)
        self.lopcao.grid(row=3, column=0)

        self.entNOME.grid(row=0, column=1)
        self.entCEL.grid(row=1, column=1)
        self.entDATA.grid(row=2, column=1)
        self.entOPCAO.grid(row=3, column=1)

        self.listClientes.grid(row=0, column=2, rowspan=10)
        self.scrollClientes.grid(row=0, column=6, rowspan=10, sticky='NS')
        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

        self.listClientes.configure(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.configure(command=self.listClientes.yview)

        
        self.estilizar_widgets()


    def estilizar_widgets(self):
        for child in self.window.winfo_children():
            w_class = child.__class__.__name__
            if w_class == "Button":
                child.grid_configure(sticky='WE', padx=self.x_pad, pady=self.y_pad)
            elif w_class == "Listbox":
                child.grid_configure(padx=(10, 0), pady=0, sticky='NS')
            elif w_class == "Scrollbar":
                child.grid_configure(padx=0, pady=0, sticky='NS')
            else:
                child.grid_configure(padx=self.x_pad, pady=self.y_pad, sticky='N')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.run()