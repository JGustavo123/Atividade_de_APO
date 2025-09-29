from database.db import conectar, criar_tabela
from models.item import Item

class ItemDAO:

    def adicionar(self, item: Item):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO itens (descricao, quantidade) VALUES (?, ?)", 
                       (item.descricao, item.quantidade))
        conn.commit()
        conn.close()

    def listarTodos(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM itens")
        linhas = cursor.fetchall()
        conn.close()
        return [Item(id=row[0], descricao=row[1], quantidade=row[2]) for row in linhas]