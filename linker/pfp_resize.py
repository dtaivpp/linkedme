from PIL import Image

def image_resize(filepath):
  image = Image.open(filepath)
  image = image.resize((500,500),Image.ANTIALIAS)
  image.save(fp="docs/500x500.png")
  return "docs/500x500.png"