import json
import streamlit as st
from streamlit_option_menu import option_menu

# Configurar a página do app
st.set_page_config(page_title="Tinder Talk Assistant", layout="wide")

# Título do App
st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
        color: #FE3C72;
        margin-bottom: 20px;
    }
    .title-container h1 {
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
    }
    .title-container p {
        font-size: 1.2rem;
        color: #FF7854;
    }
    </style>
    <div class="title-container">
        <h1>Tinder Talk Assistant</h1>
        <p>Boost your conversations and make her interested!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Estilização personalizada com CSS
st.markdown(
    """
    <style>
    body {
        background-color: #FDF3F4;
        font-family: Arial, sans-serif;
    }
    .css-18e3th9 {
        background-color: #FDF3F4;
        font-family: Arial, sans-serif;
    }
    .stButton > button {
        background-color: #FE3C72;
        color: white;
        font-size: 16px;
        border: none;
        border-radius: 50px;
        padding: 10px 20px;
        margin: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FF7854;
        transform: scale(1.05);
    }
    .menu-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        margin-bottom: 20px;
    }
    .menu-container button {
        border-radius: 30px;
        background-color: #FF7854;
        color: white;
        margin: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .menu-container button:hover {
        background-color: #FE3C72;
        transform: translateY(-2px);
    }
    .script-container {
        margin: 20px auto;
        max-width: 100%;
        padding: 10px;
    }
    .script-card {
        background-color: white;
        border: 1px solid #FF7854;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        font-size: 16px;
        transition: transform 0.2s ease;
    }
    .script-card:hover {
        transform: scale(1.02);
    }
    .script-card h3 {
        color: #FE3C72;
        margin-bottom: 10px;
        font-size: 1.2rem;
    }
    .script-card p {
        color: #333;
        line-height: 1.6;
        font-size: 1rem;
    }
    .favorite-button {
        background-color: #FF7854;
        color: white;
        font-size: 14px;
        border: none;
        border-radius: 10px;
        padding: 5px 10px;
        margin-top: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .favorite-button:hover {
        background-color: #FE3C72;
    }
    @media only screen and (max-width: 768px) {
        .title-container h1 {
            font-size: 2rem;
        }
        .title-container p {
            font-size: 1rem;
        }
        .stButton > button {
            font-size: 14px;
            padding: 8px 16px;
        }
        .script-card {
            padding: 15px;
        }
        .script-card h3 {
            font-size: 1rem;
        }
        .script-card p {
            font-size: 0.9rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Carregar o arquivo JSON atualizado
try:
    with open("scripts_updated.json", "r") as file:
        scripts_data = json.load(file)
except FileNotFoundError:
    st.error("The JSON file 'scripts_updated.json' was not found. Please ensure it is in the same directory as this script.")
    scripts_data = {}
except json.JSONDecodeError:
    st.error("The JSON file 'scripts_updated.json' is not properly formatted. Please check its content.")
    scripts_data = {}

# Lista de favoritos
if "favorites" not in st.session_state:
    st.session_state["favorites"] = []

# Menu principal
menu = st.radio("Navigate", ["Scripts", "Favorites", "Bonus"], horizontal=True, index=0)

if menu == "Scripts":
    # Menu interativo usando Streamlit Option Menu
    selected = option_menu(
        menu_title=None,  # Oculta o título do menu
        options=["Casual Conversation", "Serious Relationship", "Casual Sex", "Just Friendships"],
        icons=["chat-dots", "heart", "fire", "handshake"],  # Ícones associados às opções
        menu_icon="menu-button",  # Ícone do menu principal
        default_index=0,  # Seleção padrão
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#FDF3F4"},
            "icon": {"color": "#FF7854", "font-size": "18px"},
            "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "#FE3C72"},
            "nav-link-selected": {"background-color": "#FF7854"},
        },
    )

    # Exibir os scripts baseados na seleção
    if scripts_data and selected in scripts_data:
        subcategories = list(scripts_data[selected].keys())
        selected_subcategory = st.selectbox(
            "Select what you need help with:",
            subcategories
        )

        if selected_subcategory:
            st.markdown('<div class="script-container">', unsafe_allow_html=True)
            st.subheader(f"{selected} - {selected_subcategory}")
            scripts = scripts_data[selected][selected_subcategory]

            # Exibir cada script como um cartão estilizado
            for idx, script in enumerate(scripts, start=1):
                st.markdown(f"""
                    <div class="script-card">
                        <h3>Script {idx}</h3>
                        <p>{script}</p>
                    </div>
                """, unsafe_allow_html=True)
                if st.button("Add to Favorites", key=f"fav_{idx}"):
                    st.session_state["favorites"].append(script)
                    st.success(f"Script {idx} added to favorites!")
            st.markdown('</div>', unsafe_allow_html=True)

elif menu == "Favorites":
    # Exibir seção de favoritos
    st.markdown("### Favorites")
    if st.session_state["favorites"]:
        for idx, favorite in enumerate(st.session_state["favorites"], start=1):
            st.markdown(f"""
                <div class="script-card">
                    <h3>Favorite {idx}</h3>
                    <p>{favorite}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("No favorites yet. Add some scripts!")

elif menu == "Bonus":
    # Exibir cantadas bônus
    st.markdown("### Bonus: Seductive Lines to Win Her Over")
    bonus_lines = [
        "Are you a magician? Because every time I look at you, everyone else disappears.",
        "Do you have a name, or can I call you mine?",
        "You must be tired because you've been running through my mind all day.",
        "Are you French? Because Eiffel for you.",
        "Is your name Google? Because you have everything I’ve been searching for.",
        "Do you believe in love at first sight, or should I walk by again?",
        "If beauty were a crime, you’d be serving a life sentence.",
        "Are you an interior decorator? Because when I saw you, the room became beautiful.",
        "Do you have a map? I keep getting lost in your eyes.",
        "Are you a time traveler? Because I see my future with you."
    ]

    for idx, line in enumerate(bonus_lines, start=1):
        st.markdown(f"""
            <div class="script-card">
                <h3>Line {idx}</h3>
                <p>{line}</p>
            </div>
        """, unsafe_allow_html=True)
