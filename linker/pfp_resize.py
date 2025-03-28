from PIL import Image

def image_resize(filepath="pfp.PNG"):
  image = Image.open(filepath)
  image = image.resize((500,500))
  image.save(fp="docs/500x500.png")
  return "docs/500x500.png"

if __name__ == "__main__":
  image_resize()