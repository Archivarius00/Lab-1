
color = [232,150]

SET_COLOR = '\x1b[48;5;'
END = '\x1b[0m'

def draw_line(k, offset, color):
    line = '   ' * k
    print(f"{'   ' * offset}{SET_COLOR}{color}m{line}{END}", end = '')

# draw_line(k=4, offset=20, color=255)

def draw_figure():

    
    def line1():
        draw_line(k=5, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=5, offset=0, color=255); print('', end = '')
    def line2():
        draw_line(k=4, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=1, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=4, offset=0, color=255); print('', end = '')
    def line3():
        draw_line(k=3, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=3, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=3, offset=0, color=255); print('', end = '')
    def line4():
        draw_line(k=2, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=5, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=2, offset=0, color=255); print('', end = '')
    def line5():
        draw_line(k=1, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=7, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=1, offset=0, color=255); print('', end = '')
    def line6():
        draw_line(k=0, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=9, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=0, offset=0, color=255); print('', end = '')

    line1(); line1(); line1(); line1(); print()
    line2(); line2(); line2(); line2(); print()
    line3(); line3(); line3(); line3(); print()
    line4(); line4(); line4(); line4(); print()
    line5(); line5(); line5(); line5(); print()
    line6(); line6(); line6(); line6(); print()    






if __name__ == "__main__":
    for k in range(5):
        draw_figure()
    