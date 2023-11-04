from PIL import Image

base_width= 800
img = Image.open('proyector.jfif')
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
img.save('somepic.png')