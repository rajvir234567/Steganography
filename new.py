from pil import image

def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), "08b"))
        return(newd).08b
        
def main():
    if (a == 1):
        encode()
    elif (a == 2):
        print("decoded word:" + decode())
    else:
        raise Exception("enter correct input")

if __name__ == '_main_':
    main()

def encode():
    image = input("enter image name"(widthExtensions))
    image = image.open(img, 'r')
    
    data = input("enter data to be encoded")
    if (len(data) == 0):
        raise ("data is empty")
    
    new_img = image.copy()
    encode_enc(new_img, data)
    
    new_img_name = input("enter the name")
    new_img = save(new_img_name, std, new_img_name)
    main()

def encode_enc(new_img):
    v = new_img.size[0]
    (x, y) = (0, 0)
    for pixels in modpix(new_img.getdata(), data):
        new_img.putpixel((x, y), pixel)

    if (x == w-1):
        x = 0
        y += 1

def decode():
    