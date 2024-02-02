import streamlit as st
from utils import icon
from pathlib import Path
from streamlit_image_select import image_select
from streamlit_lottie import st_lottie
import json


# Directories and file paths
THIS_DIR = Path(__file__).parent
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_game.json"

# UI configurations
st.set_page_config(page_title="Game Story Generator", layout="wide")
#icon.show_icon(":game_die:")

# Custom CSS for rainbow heading
css = """
.rainbow {
    font-size: 1.5em;
    background: linear-gradient(135deg, purple, blue);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
"""
# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f) 
    
# Render the custom CSS
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

# Render the heading with rainbow effect
st.markdown("# <span class='rainbow'>Game Story Generator</span>", unsafe_allow_html=True)


# Placeholders for images and gallery
generated_images_placeholder = st.empty()
gallery_placeholder = st.empty()

def configure_sidebar() -> None:
    """
    Setup and display the sidebar elements.

    This function configures the sidebar of the Streamlit application,
    including the form for user inputs and the resources section.
    """
    with st.sidebar:
        with st.form("my_form"):
            st.info("**Welcome! Start by entering your game idea below:**", icon="🎮")
            with st.expander(":rainbow[**Refine your output here**]"):
                prompt = st.text_area(
                    ":orange[**Enter your game idea or concept:**]",
                    value="In a post-apocalyptic world, players must survive and rebuild civilization."
                )
                negative_prompt = st.text_area(":orange[**Elements you don't want in the game story?**]",
                                               value="Avoid cliches and predictable plot twists.",
                                               help="Specify any elements you want to exclude from the story.")

            # The Big Red "Submit" Button!
            submitted = st.form_submit_button(
                "Generate Story", type="primary", use_container_width=True)

        # Credits and resources
        st.divider()
        st.markdown(
            ":orange[**Resources:**]  \n"
            f"<img src='' style='height: 1em'> <p>write the resource used here<p>",
            unsafe_allow_html=True
        )

        return submitted, prompt, negative_prompt


def main_page(submitted: bool,
              prompt: str, negative_prompt: str) -> None:
    """Main page layout and logic for generating game stories.

    Args:
        submitted (bool): Flag indicating whether the form has been submitted.
        prompt (str): User's game idea or concept.
        negative_prompt (str): Elements to avoid in the game story.
    """
    if submitted:
        with st.status('👩🏾‍💻 Crafting your game idea into an epic story...', expanded=True) as status:
            st.write("⚙️ Model initiated")
            st.write("📚 Let your imagination run wild!")

    # Gallery display for inspiration
    with gallery_placeholder.container():
        img = image_select(
            label="Game Idea Generator is an AI-powered tool that automatically transforms sparse game concepts into fleshed-out narratives to fuel the creative process.",
            images=[
                "gallery/1.jpeg", "gallery/5.jpeg",
                "gallery/2.jpeg", "gallery/6.jpeg",
                "gallery/3.jpeg", 
                "gallery/4.jpeg",
            ],
            captions=["Explore a magical fantasy world filled with mystical creatures and ancient artifacts.",
                      "Embark on an intergalactic space adventure, battling alien civilizations and discovering new planets.",
                      "Unravel the secrets of a thrilling mystery game, solving puzzles and uncovering hidden clues.",
                      "Experience bone-chilling horror in a game that will keep you on the edge of your seat.",
                      "Immerse yourself in a rich RPG game with complex characters and branching storylines.",
                      "Challenge your mind with mind-bending puzzles in a captivating puzzle game.",
                     ],
            use_container_width=True
        )


def main():
    """
    Main function to run the Streamlit application.

    This function initializes the sidebar configuration and the main page layout.
    It retrieves the user inputs from the sidebar, and passes them to the main page function.
    The main page function then generates the game story based on these inputs.
    """
    submitted, prompt, negative_prompt = configure_sidebar()
    main_page(submitted, prompt, negative_prompt)


if __name__ == "__main__":
    main()