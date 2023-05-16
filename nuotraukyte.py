
from PIL import Image


image = Image.open("dragon.png")
width, height = (564, 846)
new_size = (150, 200) # vietoje "width" ir "height" įrašykite norimus parametrus, pvz.: (60, 80)
resized_image = image.resize(new_size)
resized_image.save("small_dragon.png")