#settings.py

def init():

    # global theme settings (currently only effects timewidget)

    global colortheme #theme for text color and background color
    colortheme = 'dark' #themes include: 'light', 'dark', 'gray' 
    global colorthemetext #variable for what the current theme's font color is
    colorthemetext = 'white' #dark theme = white text, gray theme & dark theme = black text
    global colorthemebackground #variable for what the current theme's background color is
    colorthemebackground = 'black' #dark theme = black, gray theme = gray, light theme = white

    global textsize #theme for text size
    textsize = 'medium' #sizes include: 'small', 'medium', 'large'
    global textsizenum #theme for text size 15=small, 55=medium, 75=large
    textsizenum = 55 #set default to medium

    global mainwindowcolor #background color for the mainwindow include: 'black', 'gray', white'
    mainwindowcolor = 'black' 

    global themewindowswitcher #switcher for theme window selector, 0 is currently hidden 1 is currently visible
    themewindowswitcher = 1

    #VISIBILITY GLOBALS: 1 means the widget should be showing on the screen, 0 is hidden
    #all visibility globals start at 1, meaning all widgets are visible on program start
    global timewidgetVisibility
    timewidgetVisibility = 1

    global stockwidgetVisibility
    stockwidgetVisibility = 1

    global mapwidgetVisibility
    mapwidgetVisibility = 1

    global weatherwidgetVisibility
    weatherwidgetVisibility = 1

    global calenderwidgetVisibility
    calenderwidgetVisibility = 1