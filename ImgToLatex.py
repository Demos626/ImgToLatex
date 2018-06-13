import matplotlib.image as mpimg
from skimage.util import invert
from skimage.transform import rescale, rotate
from skimage.color import rgb2gray
import matplotlib.patches as mpatches
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import design  # Это наш конвертированный файл дизайна
import os
import pyqtgraph as pg
import prediction

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.find.clicked.connect(self.browse_folder)
        self.load.clicked.connect(self.set_image)
        self.now_image = None
        self.trash.setValue(0.1)
        self.trash.setSingleStep(0.01)
        # self.image.ui.histogram.hide()
        # self.image.ui.menuBtn.hide()
        # self.image.ui.roiBtn.hide()
        self.image.hideAxis('bottom')
        self.image.hideAxis('left')
        pg.setConfigOptions(imageAxisOrder="row-major")
        self.trash.sigValueChanged.connect(self.lable)
        self.go.clicked.connect(self.get_formula)
        self.label_image = None
        from check import Neural
        self.neural = Neural()

    def browse_folder(self):
        self.image_path.clear()  # На случай, если в списке уже есть элементы
        directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", filter="Images (*.png *.jpg)")
        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            self.image_path.setText(directory[0])   # добавить файл в listWidget

    def set_image(self):
        if self.image_path.text() is not "":
            image = mpimg.imread(self.image_path.text())
            image = rgb2gray(image)
            image = invert(image)
            image = rotate(image, -90, True)
            self.now_image = rescale(image, 3, order=0)
            self.image.clear()
            self.image.addItem(pg.ImageItem(invert(self.now_image).T))
            # self.image.setImage(invert(self.now_image).T)

    def lable(self, sb):
        if self.now_image is not None:
            #-------------------------------------------Настройка фильтра-------------------------------------------
            self.image.removeItem(pg.ImageItem(invert(self.now_image).T))
            self.image.clear()
            bw = closing(self.now_image > self.trash.value(), square(1))
            cleared = clear_border(bw)
            label_image = label(cleared)
            count = 1
            regions = regionprops(label_image)
            #-------------------------------------------Объединение разорванных частей-------------------------------------------
            # x = y а y = x 
            for region in regions: 
                if count < len(regions) and regions[count].area <= regions[count-1].area//5:
                    now, nxt = regions[count-1], regions[count]
                    x, y = now.centroid
                    x_nxt, y_nxt = nxt.centroid
                    if (x_nxt < x + len(now.image) and x_nxt > x - len(now.image)) and (y_nxt < y + len(now.image[0]) and y_nxt - y > 0):
                        label_image[label_image == regions[count].label] = region.label
                elif count < len(regions) and (regions[count].area - region.area < 3*2 and regions[count].area - region.area > -3*2):
                    now, nxt = regions[count-1], regions[count]
                    x, y = now.centroid
                    x_nxt, y_nxt = nxt.centroid
                    if (y_nxt - y < len(now.image)//2 and y_nxt - y > -len(now.image)//2) and (x - x_nxt < 10*2 and x - x_nxt > -10*2) :
                        label_image[label_image == regions[count].label] = region.label
                elif region.area < 40:
                    now, prev = regions[count-1], regions[count-2]
                    x, y = now.centroid
                    x_prev, y_prev = prev.centroid
                    if(y_prev - y < len(prev.image[0])//5):
                        label_image[label_image == region.label] = 0
                count += 1
            self.image.addItem(pg.ImageItem(invert(1*cleared).T))
            #-------------------------------------------Вывод рамок-------------------------------------------
            # for region in regionprops(label_image):
            #     minr, minc, maxr, maxc = region.bbox
            #     rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
            #                                 fill=False, edgecolor='red', linewidth=1)
            #     print(minr, minc, maxr, maxc, rect)
                
            #     # QPainter painter(viewport())
            #     # p = QtGui.QPainter()
            #     # p.begin(self)
            #     # p.setPen(pg.mkPen('r'))
            #     # p.drawRect(QtCore.QRectF(minr, minc, maxr, maxc))
            #     self.image.addRe
            self.label_image = label_image

    def get_formula(self):
        if self.now_image is not None:
            self.formula.setText(prediction.prediction(self.label_image, self.neural))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()