from PIL import Image,ImageFilter

kitten=Image.open("./wikiPedia/kitten.jpg")
blurryKitten=kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save("./wikiPedia/kitten_blurred.jpg")
blurryKitten.show()