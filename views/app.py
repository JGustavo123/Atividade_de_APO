import streamlit as st
from controllers.item_controller import ItemController

controller = ItemController()

st.title("Cadastro de Itens")

menu = ["Cadastrar Item", "Listar Itens"]
opcao = st.sidebar.selectbox("Menu", menu)

if opcao == "Cadastrar Item":
    st.subheader("Cadastrar Novo Item")
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)

    if st.button("Salvar"):
        controller.criarItem(descricao, quantidade)
        st.success("Item cadastrado com sucesso!")

elif opcao == "Listar Itens":
    st.subheader("Lista de Itens")
    itens = controller.obterTodosOsItens()
    
    if itens:
        data = [
            {"ID": i.id, "Descrição": i.descricao, "Quantidade": i.quantidade}
            for i in itens
        ]
        st.dataframe(data)
    else:
        st.info("Nenhum item cadastrado ainda.")


