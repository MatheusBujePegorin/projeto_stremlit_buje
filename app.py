import streamlit as st

st.set_page_config(page_title="Proejeto Streamlit", layout="wide")
st.markdown("# Testando o Streamlit")

def main():
    abas = st.tabs([
    "Clientes",
    "Cadastar Cliente",
    "Editar",
    "Deletar"
    ])
    with abas[0]:
        st.title("Clientes")

    with abas[1]:
        st.title("Cadastar Cliente")

        with st.form(key="add_cliente", clear_on_submit=True):
            nome = st.text_input("Nome", placeholder= "Nome")
            email = st.text_input("Email", placeholder= "Email")
            idade = st.number_input("Idade", placeholder= "Idade")
            telefone = st.number_input("Telefone", placeholder= "Telefone")
            profissao = st.selectbox("Selecione a profissão", options = [
                "Desenvolvedor de sistemas", "Analista de Infraestrutura",
                "DBA Senior", "Tecnico de Informatica"
            ])
            btn_cadastrar = st.form_submit_button("Cadastrar Cliente")

            data_cliente = {
                "nome": nome,
                "email" : email,
                "idade": idade,
                "telefone": telefone,
                "profissao": profissao
            }
            st.write(data_cliente)


    with abas [2]:
        st.title("Editar")

    with abas[3]:
        st.title("Deletar")
main()


