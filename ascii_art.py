import pyfiglet


def get_ascii_art(text, font='standard'):
    """
    Generate ASCII art from text using PyFiglet.
    """
    if font not in pyfiglet.FigletFont.getFonts():
        font = 'standard'
    fig = pyfiglet.Figlet(font=font)
    return fig.renderText(text)
