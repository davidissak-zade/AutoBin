import RPi.GPIO as GPIO
from servo import activateServo
from IR import trashDetected
from magneticSwitch import BinsAttachementStatusUpdate


class TrashBin:
    def __init__(self):
        self.full = False
        self.attached = False

# Trash bins objects


blackBin = TrashBin()
blueBin = TrashBin()
orangeBin = TrashBin()
greenBin = TrashBin()


while (True):
    if trashDetected():
        BinType = input("Enter bin type: ")
        BinsAttachmentStatus = BinsAttachementStatusUpdate()
        if BinType.lower() == "black" and BinsStatus["black"]:
            pass
        elif BinType.lower() == "blue" and BinsStatus["blue"]:
            pass
        elif BinType.lower() == "orange" and BinsStatus["orange"]:
            pass
        elif BinType.lower() == "green" and BinsStatus["green"]:
            pass
