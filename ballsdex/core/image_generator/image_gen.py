import os
from pathlib import Path
import textwrap
from PIL import Image, ImageFont, ImageDraw, ImageOps
from typing import TYPE_CHECKING
from ballsdex.core.models import Regime, Economy 

if TYPE_CHECKING:
    from ballsdex.core.models import BallInstance


SOURCES_PATH = Path(os.path.dirname(os.path.abspath(__file__)), "./src")
WIDTH = 1500
HEIGHT = 2000

RECTANGLE_WIDTH = WIDTH - 40
RECTANGLE_HEIGHT = (HEIGHT // 5) * 2

CORNERS = ((34, 261), (1393, 992))
artwork_size = [b - a for a, b in zip(*CORNERS)]

title_font = ImageFont.truetype(str(SOURCES_PATH / "Geologica-SemiBold.ttf"), 170)
capacity_name_font = ImageFont.truetype(str(SOURCES_PATH / "Bobby Jones Soft.otf"), 110)
capacity_description_font = ImageFont.truetype(str(SOURCES_PATH / "OpenSans-Semibold.ttf"), 75)
stats_font = ImageFont.truetype(str(SOURCES_PATH / "Bobby Jones Soft.otf"), 130)
credits_font = ImageFont.truetype(str(SOURCES_PATH / "arial.ttf"), 40)


def draw_card(ball_instance: "BallInstance"):
    ball = ball_instance.countryball
    ball_health = (237, 115, 101, 255)
    
    if ball.regime == Regime.BASISCP:
      image = Image.open(str(SOURCES_PATH / "basis.png"))
    elif ball.regime == Regime.TEACHER:
      image = Image.open(str(SOURCES_PATH / "basisteacher.png"))
    elif ball.regime == Regime.NONBASIS:
      image = Image.open(str(SOURCES_PATH / "nonbasis.png")) 
    elif ball.regime == Regime.BASISOTHER:
      image = Image.open(str(SOURCES_PATH / "basisother.png"))
    else:
      raise RuntimeError(f"Classification unknown: {ball.regime}")
    
    draw = ImageDraw.Draw(image)
    draw.text((50, 20), ball.short_name or ball.country, font=title_font)
    for i, line in enumerate(textwrap.wrap("About Me", width=28)):
        draw.text(
            (100, 1050 + 100 * i),
            line,
            font=capacity_name_font,
            fill=(230, 230, 230, 255),
            stroke_width=2,
            stroke_fill=(0, 0, 0, 255),
        )
    for i, line in enumerate(textwrap.wrap(ball.capacity_description, width=33)):
        draw.text(
            (60, 1300 + 60 * i),
            line,
            font=capacity_description_font,
            stroke_width=1,
            stroke_fill=(0, 0, 0, 255),
        )
    draw.text(
        (320, 1670),
        str(ball_instance.health),
        font=stats_font,
        fill=ball_health,
        stroke_width=1,
        stroke_fill=(0, 0, 0, 255),
    )
    draw.text(
        (960, 1670),
        str(ball_instance.attack),
        font=stats_font,
        fill=(252, 194, 76, 255),
        stroke_width=1,
        stroke_fill=(0, 0, 0, 255),
    )
    draw.text(
        (30, 1870),
        # Modifying the line below is breaking the licence as you are removing credits
        # If you don't want to receive a DMCA, just don't
        "BASIS Image Modification by Vaedz & Robby\nCreated by El Laggron",
        font=credits_font,
        fill=(0, 0, 0, 255),
        stroke_width=0,
        stroke_fill=(255, 255, 255, 255),
    )

    artwork = Image.open("." + ball.collection_card)
    image.paste(ImageOps.fit(artwork, artwork_size), CORNERS[0])

    #Economy icon

    #icon = ImageOps.fit(icon, (192, 192))
    #image.paste(icon, (1200, 30), mask=icon)

    #icon.close()

    artwork.close()

    return image
