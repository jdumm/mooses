import cv2
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt


def räkna_älgarna(cframe, dframe, draw_roi=False):
    ''' Use pytesseract to read the digits of the current moose counter
        from a single frame
    '''
    # Use pytesseract to read the digits of the current moose counter
    y1, y2, x1, x2 = 845, 895, 165, 250
    roi = cframe[y1:y2, x1:x2]
    cv2.rectangle(dframe, (x1,y1), (x2,y2), (255,255,0), 2)
    groi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    for psm_val in [8,9]:
        text = pytesseract.image_to_string(Image.fromarray(groi),config=f'--psm {psm_val} -c tessedit_char_whitelist=0123456789')
        try:
            num_mooses = int(text)
            break 
        except:
            num_mooses = -1
    font = cv2.FONT_HERSHEY_DUPLEX
    h,w,_ = roi.shape
    cv2.putText(dframe, "--> ", (280,873), font, 0.6, (255,255,0), 2, cv2.LINE_AA)
    cv2.putText(dframe, str(num_mooses), (330,885), font, 1.8, (255,255,0), 2, cv2.LINE_AA)
    if draw_roi:
        print(f"read_current_mooses, raw text: '{text}'  w/ current number of mooses: '{num_mooses}'")
        plt.figure()
        plt.imshow(roi)
        plt.show()
    return num_mooses
