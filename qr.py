import cv2
from pyzbar import pyzbar
from pynput.keyboard import Key, Controller

#installation
#sudo apt-get install libzbar0
#pip3 install opencv-python
#pip3 install Pillow



def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        global yakalanan
        yakalanan=barcode_info
        #keyboard = Controller()
        #if(yakalanan!= ""):
            #keyboard.press(Key.esc)
            #keyboard.release(Key.esc)
            

        #print(yakalanan)
    return frame


def main():
    #1
    
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()

    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        
        cv2.imshow('Barcode/QR code reader', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
    #3
    camera.release()
    cv2.destroyAllWindows()

def QRdanEkle():
    main()
    print("yakalanan:"+yakalanan)
    return yakalanan

