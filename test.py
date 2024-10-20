color = [232,150]

SET_COLOR = '\x1b[48;5;'
END = '\x1b[0m'

def draw_line(k, offset, color):
    line = '   ' * k
    print(f"{'   ' * offset}{SET_COLOR}{color}m{line}{END}", end = '')

# draw_line(k=4, offset=20, color=255)

def draw_figure():

    
    def line1():
        draw_line(k=0, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=15, offset=0, color=255); print('', end = '')
    def line2():
        draw_line(k=0, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=15, offset=0, color=255); print('', end = '')
    def line3():
        draw_line(k=0, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=15, offset=0, color=255); print('', end = '')
    def line4():
        draw_line(k=1, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=14, offset=0, color=255); print('', end = '')
    def line5():
        draw_line(k=1, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=14, offset=0, color=255); print('', end = '')
    def line6():
        draw_line(k=1, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=14, offset=0, color=255); print('', end = '')
    def line7():
        draw_line(k=2, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=13, offset=0, color=255); print('', end = '')
    def line8():
        draw_line(k=2, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=13, offset=0, color=255); print('', end = '')
    def line9():
        draw_line(k=3, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=12, offset=0, color=255); print('', end = '')
    def line10():
        draw_line(k=4, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=11, offset=0, color=255); print('', end = '')
    def line11():
        draw_line(k=5, offset=0, color=255); draw_line(k=1, offset=0, color=0); draw_line(k=10, offset=0, color=255); print('', end = '')
    def line12():
        draw_line(k=6, offset=0, color=255); draw_line(k=2, offset=0, color=0); draw_line(k=8, offset=0, color=255); print('', end = '')
    def line13():
        draw_line(k=8, offset=0, color=255); draw_line(k=3, offset=0, color=0); draw_line(k=5, offset=0, color=255); print('', end = '')
    def line14():
        draw_line(k=11, offset=0, color=255); draw_line(k=5, offset=0, color=0); draw_line(k=0, offset=0, color=255); print('', end = '')

    
    line1(); print()
    line1(); print()
    line1(); print()
    line2(); print()
    line3(); print()
    line4(); print()
    line5(); print()
    line6(); print()
    line7(); print()
    line8(); print()
    line9(); print()
    line10(); print()
    line11(); print()
    line12(); print()   
    line13(); print()
    line14(); print()




if __name__ == "__main__":
    draw_figure()