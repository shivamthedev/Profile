from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My Web Page", page_icon=":tada", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# -----Local CSS-----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

# -----Load Assets-----
lottie_gamedev = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_u9NulgbvAu.json")
image = Image.open("image.png")
image2 = Image.open("Image2.png")

#  -----Header Section-----
with st.container():
    st.subheader("Hi, I am Shivam :wave:")
    st.title("A Programmer from India")
    st.write(
        "I am passionate about creating animes and games based on Indian culture.")


# -----What I do-----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do")
        st.write("##")
        st.write("""
                 I run a game development company whose vision is to introduce rich Indian culture to the world by their games.
                 Also creates gaming content for Indian Gamers.
                 """)
    with right_column:
        st_lottie(lottie_gamedev, height=300, key='gamedev')


# -----Projects-----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image)
    with text_column:
        st.subheader("Crowd City")
        st.write("""
                 Become the biggest crowd in town!
                 Gather people accross the city and crush your opponents with your overwhelming leadership!
                 """)
        st.markdown(
            "[Play Game](https://play.google.com/store/apps/details?id=io.voodoo.crowdcity)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(image2)
    with text_column:
        st.subheader("Urban Drug Empire")
        st.write("""
                 Push towards your goal of becoming a drug lord in and around a gritty narcos underworld. Can you reach the top?

                 - Begin your journey as a drug dealer by making as much money as possible. Buy and sell drugs to earn big profits with stock market trading elements.

                 - Start from the bottom and rise up the ranks to kingpin! Expand your empire and shoot your way to the top.

                 - Travel to multiple real-world locations buying and selling products at the right price to maximise profits whilst avoiding prison

                 - Use grand strategy and gangster skills in this life simulation game to build your own urban drug empire!

                 - Purchase residential properties to expand your inventory space and improve your criminal and mafia empire.

                 - Purchase businesses and expand your underworld empire to become a drug kingpin.

                 - Expand and build your businesses to earn a passive income.

                 - Buy guns and weapons to aid you against crime, cartels, mafia and bent cops.

                 - Bribe shady cops to escape punishment and remove your wanted level.

                 - Use drug labs and weed farms

                 - Sell weed, cocaine, crack, mushrooms, ecstasy, meth and more.

                 - Heal yourself using the doctor to ensure a long reign.

                 - Buy and collect luxury cars and jets to give you a better chance of escaping a sticky situation.

                 -Commit crimes in the city of crimes, earn respect, become a ruthless crime lord and build your own mafia empire.

                 """)
        st.markdown(
            "[Play Game](https://play.google.com/store/apps/details?id=com.CybertaleProductions.UrbanDrugEmpire)")


# -----Contact form-----
with st.container():
    st.write("---")
    st.header("Get in touch with me!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/me.shivam.dev@gmail.com" method="POST">
    <input type = "hidden" name = "_captcha value = "false">
    <input type="text" name="name" placeholder = "Your name" required>
    <input type="email" name="email" placeholder = "Your email" required>
    <textarea name="message" placeholder="Your Message here" required ></textarea>
    <button type="submit">Send</button>
   </form>
    """
    
    left_column, right_coloumn = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_coloumn:
        st.empty()
