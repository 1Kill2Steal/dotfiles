import sys
import re
import colorsys


### This Python script is generated by ChatGippidy because I was lazy writing it.
### It offets the hue for all the hex color values (for example: #FF0000)
### to the hue shift from the user input.
### And of course it saves a ton of time for manual color scheming configuration.


def hex_to_rgb(hex_color):
    """Converts a hexadecimal color string to RGB."""
    return tuple(int(hex_color[i : i + 2], 16) for i in (1, 3, 5))


def rgb_to_hex(rgb_color):
    """Converts an RGB color tuple to hexadecimal."""
    return "#{:02x}{:02x}{:02x}".format(*rgb_color)


def adjust_hue(hex_color, offset):
    """Adjusts the hue of a hexadecimal color."""
    rgb_color = hex_to_rgb(hex_color)
    h, s, v = colorsys.rgb_to_hsv(*[c / 255 for c in rgb_color])
    h = (h * 360 + offset) % 360
    r, g, b = colorsys.hsv_to_rgb(h / 360, s, v)
    return rgb_to_hex((int(r * 255), int(g * 255), int(b * 255)))


def process_file(input_file, output_file, hue_offset):
    """Processes the input file with the given hue offset."""
    with open(input_file, "r") as f:
        content = f.read()
    modified_content = re.sub(
        r"#[0-9a-fA-F]{6}", lambda match: adjust_hue(match.group(), hue_offset), content
    )
    with open(output_file, "w") as f:
        f.write(modified_content)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 color_shift.py input_file output_file hue_offset")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    hue_offset = int(sys.argv[3])

    if not 1 <= hue_offset <= 360:
        print("Hue offset must be between 1 and 255.")
        sys.exit(1)

    process_file(input_file, output_file, hue_offset)
    print(
        f"File '{input_file}' processed with hue offset {hue_offset}. Output written to '{input_file}_{hue_offset}.txt'."
    )