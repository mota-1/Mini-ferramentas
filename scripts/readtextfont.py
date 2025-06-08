import pygame
import pygame.freetype
from xml.etree import ElementTree as ET
from io import BytesIO

# Load the .fnt file
def load_fnt_file(fnt_path):
    tree = ET.parse(fnt_path)
    root = tree.getroot()

    char_info = {}
    for char_element in root.iter('char'):
        char_id = int(char_element.get('id'))
        x = int(char_element.get('x'))
        y = int(char_element.get('y'))
        width = int(char_element.get('width'))
        height = int(char_element.get('height'))
        xoffset = int(char_element.get('xoffset'))
        yoffset = int(char_element.get('yoffset'))
        xadvance = int(char_element.get('xadvance'))

        char_info[char_id] = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'xoffset': xoffset,
            'yoffset': yoffset,
            'xadvance': xadvance
        }

    return char_info

# Display text using the atlas and .fnt file
def display_text(screen, font, text, atlas_image, char_info):
    x, y = 50, 50  # Initial position

    for char in text:
        char_code = ord(char)
        if char_code in char_info:
            char_data = char_info[char_code]

            # Create a surface for the character
            char_surface = pygame.Surface((char_data['width'], char_data['height']), pygame.SRCALPHA)
            char_surface.blit(atlas_image, (0, 0), (char_data['x'], char_data['y'] + 463*3, char_data['width'], char_data['height']))

            # Display the character on the screen
            screen.blit(char_surface, (x + char_data['xoffset'], y + char_data['yoffset']))

            # Move the position for the next character
            x += char_data['xadvance']

    pygame.display.flip()

# Load the atlas image
atlas_path = r"C:\Users\mathe\rucoyimage.png"
atlas_image = pygame.image.load(atlas_path)

# Load the .fnt file
fnt_path = r'C:\Users\mathe\TarefasALOP\firstfontattempt\xmlrucoyfont.fnt'
char_info = load_fnt_file(fnt_path)

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Font Rendering')

# Set up the font
font_size = 24
font = pygame.freetype.SysFont('arial', font_size)

# Display text
text_to_display = "hello world!"
display_text(screen, font, text_to_display, atlas_image, char_info)

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
###################################################################################################################
# import os
# import pygame
# import pygame.freetype
# from xml.etree import ElementTree as ET
# from PIL import Image

# # Load the .fnt file
# def load_fnt_file(fnt_path):
#     tree = ET.parse(fnt_path)
#     root = tree.getroot()

#     char_info = {}
#     for char_element in root.iter('char'):
#         char_id = int(char_element.get('id'))
#         x = int(char_element.get('x'))
#         y = int(char_element.get('y'))
#         width = int(char_element.get('width'))
#         height = int(char_element.get('height'))
#         xoffset = int(char_element.get('xoffset'))
#         yoffset = int(char_element.get('yoffset'))
#         xadvance = int(char_element.get('xadvance'))

#         char_info[char_id] = {
#             'x': x,
#             'y': y,
#             'width': width,
#             'height': height,
#             'xoffset': xoffset,
#             'yoffset': yoffset,
#             'xadvance': xadvance
#         }

#     return char_info

# # Render text to a transparent surface
# def render_text_to_surface(font, text, atlas_image, char_info, offset):
#     total_width = 0

#     for char in text:
#         char_code = ord(char)
#         if char_code in char_info:
#             char_data = char_info[char_code]

#             total_width += char_data['xadvance']
            
#     surface = pygame.Surface((total_width + 10, font.size + 10), pygame.SRCALPHA)
#     # print(font.size)
#     # surface = pygame.Surface((500, 150), pygame.SRCALPHA)
#     x_offset, y_offset = offset

#     x = 0
#     y = 0
#     for char in text: # 'a' is at 440
#         char_code = ord(char)
#         if char_code in char_info:
#             char_data = char_info[char_code]
#             # print(char_data['y'])
#             char_surface = pygame.Surface((char_data['width'], char_data['height']), pygame.SRCALPHA)
#             char_surface.blit(atlas_image, (0, 0), (char_data['x']+x_offset, char_data['y']+y_offset, char_data['width'], char_data['height']))

#             surface.blit(char_surface, (x + char_data['xoffset'], y + char_data['yoffset']))

#             x += char_data['xadvance']

#     return surface

# # Save a Pygame surface to a PNG file with transparency
# def save_surface_to_png(surface, file_path):
#     pygame.image.save(surface, file_path)

# # Initialize pygame and the FreeType library
# pygame.init()
# pygame.freetype.init()

# # Load the atlas image
# atlas_path = r"C:\Users\mathe\rucoyimage.png"
# atlas_image = pygame.image.load(atlas_path)

# # Load the .fnt file
# fnt_path = r'C:\Users\mathe\TarefasALOP\firstfontattempt\xmlrucoyfont.fnt'
# char_info = load_fnt_file(fnt_path)

# # Set up the font
# font_size = 32
# font = pygame.freetype.SysFont('arial', font_size)

# # Render text to surface
# text_to_display = "the quick brown fox, jumps over the lazy dog!"

# prefixes = ["Golden", "Icy", "Dragon", "Minotaur"]
# lone_items = ["Armor", "Light Armor", "Helmet", "Hood", "Legs", "Boots", "Belt", "Bow", "Shield"]
# offset_pairs = [(0, 463*3), (0, 463), (463, 463*2), (463, 463)] # white, green, blue, purple, yellow


# # Save the surface to a PNG file with transparency
# output_path = "C:\\Users\\mathe\\TarefasALOP\\pythontextfont\\output_text"
# counter = 0
# while (os.path.exists(f'{output_path}{counter}.png')):
#     counter +=1

# for n in prefixes:
#     for m in lone_items:
#         for z in offset_pairs:
#             text_surface = render_text_to_surface(font, f'{n} {m}', atlas_image, char_info, z)
#             save_surface_to_png(text_surface, f'{output_path}{counter}.png')
#             counter +=1

# # Quit pygame and FreeType
# pygame.quit()
# pygame.freetype.quit()
##############################################################################

# import easyocr
# print('began!')
# # Create OCR reader instance
# reader = easyocr.Reader(['en'])

# # Load an image for OCR
# image_path = r"C:\Users\mathe\Pictures\Screenshots\Captura de tela 2024-02-06 220007.png"
# print('reading image!')
# # Perform OCR on the image
# result = reader.readtext(image_path)
# print('printing results!')
# # Print the results
# for detection in result:
#     text = detection[1]
#     confidence = detection[2]
#     print(f'Text: {text}, Confidence: {round(confidence*100, 2)}')


################################################################################
# valid_strings = ["id", "x", "y", "width", "height", "xoffset", "yoffset", "xadvance", "page", "chnl", "letter"]
# with open(r"C:\Users\mathe\TarefasALOP\mythic_replacement.fnt", "r", encoding='utf-8') as file:
#     contents = file.read()


# # paragraphs = contents.split('\n')
# # print(paragraphs[0:15])

# # for i in range(8, 296):
# #     paragraphs[i] = '<'+paragraphs[i]+"/>"
# # result = "\n".join(paragraphs)



# ################
# # Replace special characters with XML entities
# # contents = contents.replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;").replace("\"", "&quot;")#.replace("&", "&amp;")

# Split and process contents
# split_contents = contents.split('=')
# print(split_contents[21-2:21+2])
# for i in range(21, len(split_contents)):
#     temp_split = split_contents[i].split(' ')
#     if len(temp_split) > 1 and temp_split[1] in valid_strings and temp_split[0].isdigit():
#         if temp_split[1] == "letter":
#             split_contents[i] = f'= "{temp_split[0]}" {temp_split[1]} = '
#         else:
#             split_contents[i] = f'= "{temp_split[0]}" {temp_split[1]}'

# results = "".join(split_contents[1:len(split_contents)])
#######
# negative_nums = contents.replace("-3", '= "-3"')

# results = negative_nums
# with open(r"C:\Users\mathe\TarefasALOP\tempxmlfont.fnt", "x", encoding='utf-8') as second_file:
#     second_file.write(results)

# def betterNumParser(num):
#     try:
#         invalid_integer = int(num)
#         return True
#     except Exception:
#         return False


# def formatToXML():
#     valid_strings = ["id", "x", "y", "width", "height", "xoffset", "yoffset", "xadvance", "page", "chnl", "letter"]
#     with open(r"C:\Users\mathe\Downloads\justforit\rucoy-online-1-27-0\assets\gui\font.fnt", "r", encoding='utf-8') as file:
#         contents = file.read()
#     contents = contents.replace("<", "&lt;").replace(">", "&gt;").replace("'", "&apos;").replace("&", "&amp;")#.replace("\"", "&quot;")

#     paragraphs = contents.split('\n')
#     startIndex = None
#     for j, m in enumerate(paragraphs):
#         if m.startswith("char"):
#             startIndex = j
#             break

#     for i in range(startIndex, len(paragraphs)):
#         paragraphs[i] = '<'+paragraphs[i]+"/>"
#     contents = '\n'.join(paragraphs)


#     ############
    
#     print(contents)
#     split_contents = contents.split('=')
#     print(split_contents[21-2:21+2])
#     for i in range(21, len(split_contents)):
#         temp_split = split_contents[i].split(' ')
#         if len(temp_split) > 1 and temp_split[1] in valid_strings and betterNumParser(temp_split[0]):
#             if temp_split[1] == "letter":
#                 split_contents[i] = f'= "{temp_split[0]}" {temp_split[1]} = '
#             else:
#                 split_contents[i] = f'= "{temp_split[0]}" {temp_split[1]}'

#     results = "".join(split_contents)

#     with open(r"C:\Users\mathe\TarefasALOP\tempxmlfont.fnt", "x", encoding='utf-8') as second_file:
#         second_file.write(results)
# formatToXML()