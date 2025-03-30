import os
from pathlib import Path
import re
from string import ascii_lowercase, digits
from PIL import Image, ImageDraw, ImageFont


BACKGROUND_IMG = "horror.png"
FONT_FILE = "Roboto-Light.ttf"
OUTPUT_DIR = "images"
START_OFFSET_TEXT = (650, 160)
TEXT_COLOR = (255, 255, 255, 255)
LINE_SPACING = 140
SEPARATOR = "|"


def _create_output_file_name(text):
    fname = text.lstrip("#").replace(f" {SEPARATOR} ", " ")
    fname = re.sub(f"[^{ascii_lowercase + digits}]", "-", fname.lower())
    fname = f"{fname}.png"
    return fname


def create_thumbnail(text,
                     template=BACKGROUND_IMG,
                     output_dir=OUTPUT_DIR,
                     fontfile=FONT_FILE,
                     font_size=100,
                     text_color=TEXT_COLOR,
                     start_offset=START_OFFSET_TEXT,
                     line_spacing=LINE_SPACING):
    base = Image.open(template).convert('RGBA')
    image = Image.new('RGBA', base.size)
    offset = start_offset

    for i, line in enumerate(text.split(SEPARATOR)):
        left, top = offset
        top += i * line_spacing
        font = ImageFont.truetype(fontfile, font_size)
        draw_context = ImageDraw.Draw(image)
        new_offset = (left, top)
        draw_context.text(new_offset, line,
                          font=font, fill=text_color)

    out = Image.alpha_composite(base, image)

    output_file_path = Path(output_dir) / _create_output_file_name(text)

    out.save(output_file_path)


if __name__ == "__main__":

    create_thumbnail("Vibe Coding")
