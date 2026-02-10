from pyscript import document
import random
import time


def loops_sample(e):

    result = document.getElementById("result")
    junk = []

    while True:

        big = ""
        for i in range(3000):
            big += f"Generating Robux {random.randint(1,999999)} 💰<br>"

        result.innerHTML = big


        for x in range(40000):
            junk.append(x * x * x)

        if len(junk) > 200000:
            junk.clear()

        time.sleep(0.01)
