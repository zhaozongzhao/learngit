
def getSize(driver):
        x=driver.get_window_size()['width']
        y=driver.get_window_size()['height']
        return(x,y)
def swipeLeft(driver):
#向左滑动
       l=getSize
       x1=int(l[0]*0.75)
       y1=int(l[1]*0.5)
       x2=int(l[0]*0.25)
       driver.swipe(x1,y1,x2,y1,500)
#向右滑动
def swipeRight(driver):
        l=getSize()
        x1=int(l[0]*0.25)
        y1=int(l[1]*0.5)
        x2=int(l[0]*0.75)
        driver.swipe(x1,y1,x2,y1,500)
#向上滑动
def swipeUp(driver):
        l=getSize(driver)
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.75)
        y2=int(l[1]*0.25)
        driver.swipe(x1,y1,x1,y2,500)
#向下滑动
def swipeDown(driver):
        l=getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        driver.swipe(x1,y1,x1,y2,500)