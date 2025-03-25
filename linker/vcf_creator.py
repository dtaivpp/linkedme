from pfp_resize import image_resize
from pfp_encode import encode
from pfp_resize import image_resize

def create_vcard(config):
  pfp_path = image_resize("pfp.PNG")

  encoded_photo = encode(pfp_path)
  return "BEGIN:VCARD\n" \
         "VERSION:4.0\n" \
        f"PHOTO;ENCODING=base64;TYPE=PNG:{encoded_photo}\n" \
          "N:Tippett;David;;;\n" \
          "FN:David Tippett\n" \
          "ORG:Amazon\n" \
          "TITLE:Search Engineer - GitHub\n" \
          "item1.URL;type=pref:https://linkedin.com/in/david.tippett\n" \
          "item1.X-ABLabel:LinkedIn\n" \
          "item2.URL:https://tippybits.com\n" \
          "item2.X-ABLabel:Website\n" \
          "item3.URL:https://bsky.app/profile/taidesu.bsky.social\n" \
          "item3.X-ABLabel:BlueSky\n" \
          "END:VCARD"

def write_out_vcard(vcard):
  with open('contact.vcf', 'w') as f:
    f.write(vcard)

if __name__=="__main__":
  card = create_vcard("")
  write_out_vcard(card)