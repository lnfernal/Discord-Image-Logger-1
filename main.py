import requests
import io
from flask import Flask, request, send file

try:
    # Your stub in here
    with open("exestub.exe" , "rb") as e:
        s = e.read()
        
    # Just put any image here
    with open("image.jpg" , 'wb') as f:
        f.write(s)

    print("JPG opened")

except Exception as e:
    print(e)