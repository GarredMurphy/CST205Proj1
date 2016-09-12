from PIL import Image


#get all of the images
imageList = [Image.open("1.png"), Image.open("2.png"), Image.open("3.png"), Image.open("4.png"), Image.open("5.png"), Image.open("6.png"), Image.open("7.png"), Image.open("8.png"), Image.open("9.png")]





#create an image
outputImage = imageList[0]
imageWidth = outputImage.width
imageHeight = outputImage.height

redList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
greenList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
blueList = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, imageWidth):
    print (x)
    for y in range(0, imageHeight):
        for z in range(0, 9):
            redList[z], greenList[z], blueList[z] = imageList[z].getpixel((x,y)) #get pixels from each image.
        redSort = sorted(redList) #sort values
        greenSort = sorted(greenList)
        blueSort = sorted(blueList)
        outputImage.putpixel((x, y), (redSort[4], greenSort[4], blueSort[4])) #use median in output image


outputImage.show()