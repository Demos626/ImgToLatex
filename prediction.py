from skimage.measure import regionprops
from skimage.util import invert
from skimage.transform import resize
import numpy as np
def prediction(label_image, neural):
    count = 1
    image = []
    for region in regionprops(label_image):
        if region.area >= 10:
            reg = region.image
            h = len(reg[0])
            w = len(reg)
            wc, hc = 0, h-1
            if w > h:
                if (h > 50 and w > h*2):
                    w = h-h//3
                    img = np.zeros((h+8,w))
                    for i in range(4, h+4):
                        for j in range(4, w-4):
                            img[i][j] = reg[wc][hc]
                            wc += 1
                        hc -= 1
                        wc = 0
                else:
                    if h < 15 and w > h*20: w = h*20
                    w += 8
                    img = np.zeros((w,w))
                    if w-h % 2 == 0: 
                        for i in range((w-h)//2, w-(w-h)//2):
                            for j in range(4, w-4):
                                img[i][j] = reg[wc][hc]
                                wc += 1
                            hc -= 1
                            wc = 0
                    else:
                        for i in range((w-h)//2-1, w-(w-h)//2-1) :
                            for j in range(4, w-4):
                                img[i][j] = reg[wc][hc]
                                wc += 1
                            hc -= 1
                            wc = 0

            elif h > w:
                h += 8
                img = np.zeros((h,h))
                if h-w % 2 == 0: 
                    for i in range(4, h-4):
                        for j in range((h-w)//2, h - (h-w)//2):
                            img[i][j] = reg[wc][hc]
                            wc += 1
                        hc -= 1
                        wc=0
                else:
                    for i in range(4, h-4):
                        for j in range((h-w)//2, h - (h-w)//2-1):
                            img[i][j] = reg[wc][hc]
                            wc += 1
                        hc -= 1
                        wc = 0
            else: 
                h += 10
                img = np.zeros((h,h))
                for i in range(5, h-5):
                    for j in range(5, h-5):
                        img[i][j] = reg[wc][hc]
                        wc += 1
                    hc -= 1
                    wc = 0
            img = resize(img, (32,32), order=0)
            img = invert(img)
            image.append(img)
            count += 1
    image = np.array(image)
    symbols = []
    T = neural.recognize(image)
    d = {line.split('~')[0]: line.split('~')[1].rstrip('\n') for line in open('data\\command.txt')}
    for i in range(len(T)): symbols.append(str(d[str(T[i][0]).zfill(3)]))
    regions = regionprops(label_image)
    count = 0
    string = ""
    frac_numb = index_numb = None
    frac_down = frac_up = ""
    frac = index = False
    from code import Code
    tex = Code(symbols, regions)
    for symb in symbols:
        now = regions[count]
        if symb is '-' and not frac:
            nxt = regions[count+1]
            x, y = now.centroid
            x_nxt, y_nxt = nxt.centroid
            if y_nxt-y > len(now.image[0])*2 or y_nxt-y < -len(now.image[0])*2:
                frac = True
                frac_numb = count
                count += 1
                continue
        if not index and count is not 0:
            index_numb = count-1
            pre = regions[index_numb]
        elif not index: 
            index_numb = 0
            pre = regions[index_numb]
        if frac:
            frac = tex.fr(now, regions[frac_numb], count)
            if not frac:
                string += tex.give_string()
                tex.zeros_string()  
        else:
            index = tex.ind(pre, now, symb, index_numb)
            if not index:
                string += tex.give_string()
                tex.zeros_string()
        count += 1
    else:
        if index:
            tex.last_ind()
        if frac:
            tex.last_frac()
        string += tex.give_string()
        return string