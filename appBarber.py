from TkGui import *
import databaseSQL as core

app = None
selected = None

def view_command():
    rows = core.TransactionObject.view() 
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():

    app.listClientes.delete(0, END) 
    rows = core.TransactionObject().search(
        app.txtNome.get(), 
        app.txtCel.get(), 
        app.txtData.get(), 
        app.txtOpcao.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.TransactionObject.insert(app.txtNome.get(), app.txtCel.get(), app.txtData.get(), app.txtOpcao.get())
    view_command()

def update_command():
    if selected:
        core.TransactionObject.update(selected[0], app.txtNome.get(), app.txtCel.get(), app.txtData.get(), app.txtOpcao.get())
        view_command()

def del_command():
    if selected:
        core.TransactionObject.delete(selected[0])
        view_command()

def getSelectedRow(event):
    global selected
    selection = app.listClientes.curselection()
    if selection: 
        index = selection[0]
        selected = app.listClientes.get(index)
        
        app.entNOME.delete(0, END)
        app.entNOME.insert(END, selected[1])
        app.entCEL.delete(0, END)
        app.entCEL.insert(END, selected[2])
        app.entDATA.delete(0, END)
        app.entDATA.insert(END, selected[3])
        app.entOPCAO.delete(0, END)
        app.entOPCAO.insert(END, selected[4])

if __name__ == "__main__":
    app = GUI()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    
    app.run()

