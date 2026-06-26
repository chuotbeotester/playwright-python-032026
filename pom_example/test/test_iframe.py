import time

def test_single_iframe(page):
    page.goto("https://demo.automationtesting.in/Frames.html")
     
    frame =  page.frame_locator("#singleframe")
    frame.locator("input").fill("Hello")
    time.sleep(3)

