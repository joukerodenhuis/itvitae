import curses
import datetime

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    s = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_color(curses.COLOR_ORANGE, 255,   165,   0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_ORANGE, curses.COLOR_ORANGE)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_GREEN)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLUE)
    curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_MAGENTA)

    # Loop where k is the last character pressed
    while (k != ord('q')):



        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)
        
        junk = "" 
        x = 0
        y = 0
        
        while x < width:
            junk += "x"
            x += 1
        
        
        begin_x = 0
        for x in range(6):
            t = int(x + 1)
            begin_y = int(x * height / 6)
            
            stdscr.attron(curses.color_pair(t))
            stdscr.addstr(begin_y, 0, junk)
            stdscr.addstr(begin_y + 1, 0, junk)
            stdscr.addstr(begin_y + 2, 0, junk)
            stdscr.attroff(curses.color_pair(t))
        
        stdscr.refresh()
        
        # Declaration of strings
        title = "Curses example"[:width-1]
        subtitle = "Written by Clay McLeod"[:width-1]
        keystr = "Last key pressed: {}".format(k)[:width-1]
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
        if k == 0:
            keystr = "No key press detected..."[:width-1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_x_gmstr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        

        # Render status bar
        

        # Turning on attributes for title
        

        # Rendering title
        

        # Turning off attributes for title
        

        # Print rest of text
        

        # Addition for fun
        if k == ord(" "):
            
            if s == 0:
                gm1 = datetime.datetime.now()
                gmstr = str(gm1 - gm1)
                stdscr.addstr(start_y + 7, start_x_gmstr, gmstr)
                s = 1

            elif s == 1:
                gm2 = datetime.datetime.now()
                gmstr = str(gm2-gm1)
                stdscr.addstr(start_y + 7, start_x_gmstr, gmstr)
                s = 0
            

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()