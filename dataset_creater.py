import cv2
import numpy as np
import sqlite3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0) # 0 for inbuilt camera

def insertorupdate(Id, age, Name ):
    conn = sqlite3.connect("FaceBase.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID = " + str(Id) # check if id already exists
    cursor = conn.execute(cmd) 
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if isRecordExist == 1:
        conn.execute("UPDATE STUDENTS SET NAME = ? WHERE ID = ?",(Name, Id))
        conn.execute("UPDATE STUDENTS SET AGE = ? WHERE ID = ?",(age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS(ID, NAME, AGE) VALUES(?, ?, ?)",(Id, Name, age))    