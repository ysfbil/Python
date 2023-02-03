print("Setting up")
import cv2
import numpy as np
from utils import *
import solver
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # tensorflow uyarılarının görünmemsi için

###########################333
pathImage = "Resources/1.jpg"
heightImg = 450
widthImg = 450
model = initializePredictionModel()  # modeli yüklüyoruz.
###################33333

# Resmi hazırlama
img = cv2.imread(pathImage)
img = cv2.resize(img, (widthImg, heightImg))
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
imgThershold = preProcess(img)

# Tüm kenarları bulma
imgContours = img.copy()
imgBigContour = img.copy()
contours, hierarchy = cv2.findContours(imgThershold, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)  # Kenarları buluyoruz. RETR_EXTERNAL dış kenar buluyor
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)  # tüm kenarları kopya resme çizdiriyoruz

# En büyük kenarı bulma
biggest, maxArea = biggestContour(contours)  # en büyük kenarı oluşturan kısmı buluyoruz
if biggest.size != 0:
    biggest = reorder(biggest)  # koordinat sırasını düzenliyoruz.
    cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25)  # kenarı kopya resme çiziyoruz
    # sudoku resmini kenar noktalarını alıp perspektif düzeltmesi yapıyoruz
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    imgWarpColored = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

    imgDetectedDigits = imgBlank.copy()

    # Resimleri bölme ve herbir rakamı bulma
    imgSolvedDigits = imgBlank.copy()
    boxes = splitBoxes(imgWarpColored)
    print(len(boxes))
    # cv2.imshow("sample",boxes[0])
    numbers = getPrediction(boxes, model)
    print(numbers)
    imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers, color=(255, 0, 255))
    numbers = np.asarray(numbers)
    posArray = np.where(numbers > 0, 0, 1)

    # çözümleri bulma
    board = np.array_split(numbers, 9)  # vektörden istenilen matris formatna çevirdik
    try:
        solver.solve(board)  # çözümledik
    except:
        pass

    flatList = []
    for sublist in board:
        for item in sublist:
            flatList.append(item)
    solvedNumbers = flatList * posArray
    imgSolvedDigits = displayNumbers(imgSolvedDigits, solvedNumbers)

    # çözümü soru resmi üzerine aktarma
    pts2 = np.float32(biggest)
    pts1 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgInWarpColored = img.copy()
    imgInWarpColored = cv2.warpPerspective(imgSolvedDigits, matrix, (widthImg, heightImg))
    inv_perspective = cv2.addWeighted(imgInWarpColored, 1, img, 0.5, 1)
    imgDetectedDigits = drawGrid(imgDetectedDigits)
    imgSolvedDigits = drawGrid(imgSolvedDigits)

    imageArray = ([img, imgThershold, imgBigContour, imgWarpColored],
                  [imgDetectedDigits, imgSolvedDigits, imgInWarpColored, inv_perspective])
    stackedImage = stackImages(imageArray, 0.7)
    cv2.imshow('Stacked Images', stackedImage)

else:
    print("Sudoku bulunamadı")

cv2.waitKey(0)
