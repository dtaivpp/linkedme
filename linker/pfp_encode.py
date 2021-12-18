import base64

def encode(filepath: str):
  with open(filepath, "rb") as f:
    return base64.b64encode(f.read()).decode('utf-8')

if __name__=="__main__":
  print(encode("pfp.PNG"))