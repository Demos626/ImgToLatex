import matplotlib.pyplot as plt
class Code:
    def __init__(self, symbols, regions):
        self.symbols = symbols
        self.regions = regions
        self.string = self.string_down = self.string_up = ""
        self.index_up = self.index_down = "" 
        self.index = self.fr_index_up = self.fr_index_down = self.frac = False
        self.down_index_numb = self.up_index_numb = None
        self.frac_down = self.frac_up = ""
        self.frac_up_index = sub_Code(self.symbols)
        self.frac_down_index = sub_Code(self.symbols)
    def ind(self, pre, now, symb, index_numb):
        x_pre, y_pre = pre.centroid
        x, y = now.centroid
        if self.symbols[index_numb] is '-' or self.symbols[index_numb] is '=' or self.symbols[index_numb] is "+":
            self.string += symb
            return self.index
        elif (y_pre - len(pre.image[0])//4 > y) and (y_pre - len(pre.image[0])*2 < y) and (x> x_pre  - len(pre.image)//2 ):
            self.index = True
            self.index_down += symb
        elif (y_pre + len(pre.image[0])//4 < y) and (y_pre + len(pre.image[0])*2 > y) and (x> x_pre  - len(pre.image)//2 ):
            self.index = True
            self.index_up += symb
        else: 
            if self.index_down is not "" and self.index_up is not "":
                self.index = False
                self.string += "_{%s}^{%s}%s"%(self.index_down, self.index_up, symb)  
            elif self.index_down is not "" and self.index_up is "":
                self.index = False
                self.string += "_{%s}%s"%(self.index_down, symb)
            elif self.index_down is "" and self.index_up is not "":
                self.index = False
                self.string += "^{%s}%s"%(self.index_up, symb)
            else: 
                self.string += symb
            self.index_down = self.index_up = ""
            return self.index
        return self.index
    def last_ind(self):
        if self.index_down is not "" and self.index_up is not "":
            self.index = False
            self.string += "_{%s}^{%s}"%(self.index_down, self.index_up)
        elif self.index_down is not "" and self.index_up is "":
            self.index = False
            self.string += "_{%s}"%(self.index_down)
        elif self.index_down is "" and self.index_up is not "":
            self.index = False
            self.string += "^{%s}"%(self.index_up)
    def give_string(self):
        return self.string 
    def zeros_string(self):
        self.string = ""
    def fr(self, now, frac_numb, count):
        self.frac = True
        x, y = now.centroid
        x_frac, y_frac = frac_numb.centroid
        if x < x_frac + len(frac_numb.image)//2 and y_frac > y:
            if self.down_index_numb is None:
                self.down_index_numb = count
            self.fr_index_down = self.frac_down_index.ind(self.regions[self.down_index_numb], now, self.symbols[count], self.down_index_numb)
            if not self.fr_index_down:
                self.frac_down += self.frac_down_index.give_string()
                self.frac_down_index.zeros_string()
                self.down_index_numb = count
        elif x < x_frac + len(frac_numb.image)//2 and y_frac < y:
            if self.up_index_numb is None:
                self.up_index_numb = count
            self.fr_index_up = self.frac_up_index.ind(self.regions[self.up_index_numb], now, self.symbols[count], self.up_index_numb)
            if not self.fr_index_up:
                self.frac_up += self.frac_up_index.give_string()
                self.frac_up_index.zeros_string()
                self.up_index_numb = count
        else:
            self.frac = False
            self.string += "\\frac{%s}{%s}%s"%(self.frac_up, self.frac_down, self.symbols[count])
            self.frac_up = self.frac_down = ""
        return self.frac
    def last_frac(self):
        self.string += "\\frac{%s}{%s}"%(self.frac_up, self.frac_down)
        self.frac_up = self.frac_down = ""
class sub_Code:
    def __init__(self, symbols):
        self.symbols = symbols
        self.string = ""
        self.index_up = self.index_down = "" 
        self.index = False
    def ind(self, pre, now, symb, index_numb):
        x_pre, y_pre = pre.centroid
        x, y = now.centroid
        if self.symbols[index_numb] is '-':
            self.string += symb
            return self.index
        elif (y_pre - len(pre.image[0])//4 > y) and (y_pre - len(pre.image[0])*2 < y) and (x> x_pre  - len(pre.image)//2 ):
            self.index = True
            self.index_down += symb
        elif (y_pre + len(pre.image[0])//4 < y) and (y_pre + len(pre.image[0])*2 > y) and (x> x_pre  - len(pre.image)//2 ):
            self.index = True
            self.index_up += symb
        else: 
            if self.index_down is not "" and self.index_up is not "":
                self.index = False
                self.string += "_{%s}^{%s}%s"%(self.index_down, self.index_up, symb)  
            elif self.index_down is not "" and self.index_up is "":
                self.index = False
                self.string += "_{%s}%s"%(self.index_down, symb)
            elif self.index_down is "" and self.index_up is not "":
                self.index = False
                self.string += "^{%s}%s"%(self.index_up, symb)
            else: 
                self.string += symb
            self.index_down = self.index_up = ""
            return self.index
        return self.index
    def last_ind(self):
        if self.index_down is not "" and self.index_up is not "":
            self.index = False
            self.string += "_{%s}^{%s}"%(self.index_down, self.index_up)
        elif self.index_down is not "" and self.index_up is "":
            self.index = False
            self.string += "_{%s}"%(self.index_down)
        elif self.index_down is "" and self.index_up is not "":
            self.index = False
            self.string += "^{%s}"%(self.index_up) 
    def give_string(self):
        return self.string 
    def zeros_string(self):
        self.string = ""