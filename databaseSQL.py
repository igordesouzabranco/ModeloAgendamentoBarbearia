import sqlite3 as sql

class TransactionObject():
    database = "agendamentos.db"
    conn = None
    cur = None
    connected = False


    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        if TransactionObject.connected:
            TransactionObject.conn.close()
            TransactionObject.connected = False

    def execute(self, sql_query, parms=None):
        if TransactionObject.connected:
            if parms is None:
                TransactionObject.cur.execute(sql_query)
            else:
                TransactionObject.cur.execute(sql_query, parms)
            return True
        return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        return False
    
    def initDB():
        trans = TransactionObject()
        trans.connect()
        trans.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, 
        celular TEXT, 
        data TEXT, 
        opcao TEXT)""")
        trans.persist()
        trans.disconnect()


    def insert(nome, celular, data, opcao):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO agendamentos VALUES (NULL, ?, ?, ?, ?)", (nome, celular, data, opcao))
        trans.persist()
        trans.disconnect()

    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM agendamentos")
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def search(self, nome="", celular="", data="", opcao=""):
        self.connect()
        query = """
            SELECT * FROM agendamentos 
            WHERE (nome LIKE ? OR ? = '') 
            AND (celular LIKE ? OR ? = '') 
            AND (data LIKE ? OR ? = '') 
            AND (opcao LIKE ? OR ? = '')
            """
        params = (
        f'%{nome}%', nome, 
        f'%{celular}%', celular, 
        f'%{data}%', data, 
        f'%{opcao}%', opcao)

        self.cur.execute(query, params)
        rows = self.cur.fetchall()
        self.disconnect()
        return rows

    def delete(id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM agendamentos WHERE id = ?", (id,))
        trans.persist()
        trans.disconnect()

    
    def update(id, nome, celular, data, opcao):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE agendamentos SET nome=?, celular=?, data=?, opcao=? WHERE id=?", (nome, celular, data, opcao, id))
        trans.persist()
        trans.disconnect()

TransactionObject.initDB()