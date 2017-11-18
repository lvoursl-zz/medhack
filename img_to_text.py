from PIL import Image
import pyocr
import pyocr.builders

LANG = 'rus'

def convert_img_to_text(img_name, check_rotation=True):
    try:
        tools = pyocr.get_available_tools()
        tool = tools[0]

        img = Image.open(img_name)

        if check_rotation:
            orientation = tool.detect_orientation(
                img,
                lang=LANG
            )            
            text = tool.image_to_string(img.rotate(orientation['angle']), lang=LANG)

        text = tool.image_to_string(img, lang=LANG)

        return text

    except Exception as e:
        print(str(e))
        return None