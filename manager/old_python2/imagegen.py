#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import textwrap

img = Image.new('RGB', (600, 300), color = (237, 237, 237))

fnt = ImageFont.truetype('./fonts/george-williams_monospace/Monospace.ttf', 40)
d = ImageDraw.Draw(img)
text = "fün’a"
text = textwrap.fill(text, width=29)

d.text((10, 10), text, font=fnt, fill=(28, 26, 27))

img.save('pil_text.jpg')