from pyscript import document
import time
import random


def loops_sample(e):

    result = document.getElementById("result")

    while True:

        for i in range(5000):

            result.innerHTML += f"Generating Robux {random.randint(1,999999)} 💰<br>"

        time.sleep(0.01)
        
        waste = []
        for x in range(10000):
            waste.append(x * x * x)
