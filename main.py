import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from algoritms import draw_line_step, draw_line_dda, draw_line_bresenham, draw_circle_bresenham, draw_line_casteljau, draw_smooth_line

class RasterAlgorithmsApp:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        self.ax.set_aspect('equal')

        self.algorithm_var = "step"
        self.start_x = 0
        self.start_y = 0
        self.end_x = 10
        self.end_y = 10

        # Создание кнопок и текстовых полей
        self.step_button = Button(plt.axes([0.1, 0.05, 0.1, 0.075]), 'Step')
        self.dda_button = Button(plt.axes([0.2, 0.05, 0.1, 0.075]), 'DDA')
        self.bresenham_button = Button(plt.axes([0.3, 0.05, 0.1, 0.075]), 'Bresenham')
        self.circle_button = Button(plt.axes([0.4, 0.05, 0.1, 0.075]), 'Circle')
        self.casteljau_button = Button(plt.axes([0.5, 0.05, 0.1, 0.075]), 'Casteljau')
        self.smooth_button = Button(plt.axes([0.6, 0.05, 0.1, 0.075]), 'Smooth')

        self.start_x_text = TextBox(plt.axes([0.1, 0.15, 0.1, 0.075]), 'Start X', initial="0")
        self.start_y_text = TextBox(plt.axes([0.2, 0.15, 0.1, 0.075]), 'Start Y', initial="0")
        self.end_x_text = TextBox(plt.axes([0.3, 0.15, 0.1, 0.075]), 'End X', initial="10")
        self.end_y_text = TextBox(plt.axes([0.4, 0.15, 0.1, 0.075]), 'End Y', initial="10")

        self.draw_button = Button(plt.axes([0.7, 0.05, 0.1, 0.075]), 'Draw')

        # Привязка событий к кнопкам
        self.step_button.on_clicked(self.set_step)
        self.dda_button.on_clicked(self.set_dda)
        self.bresenham_button.on_clicked(self.set_bresenham)
        self.circle_button.on_clicked(self.set_circle)
        self.casteljau_button.on_clicked(self.set_casteljau)
        self.smooth_button.on_clicked(self.set_smooth)
        self.draw_button.on_clicked(self.draw)

    def set_step(self, event):
        self.algorithm_var = "step"

    def set_dda(self, event):
        self.algorithm_var = "dda"

    def set_bresenham(self, event):
        self.algorithm_var = "bresenham"

    def set_circle(self, event):
        self.algorithm_var = "circle_bresenham"

    def set_casteljau(self, event):
        self.algorithm_var = "casteljau"

    def set_smooth(self, event):
        self.algorithm_var = "smooth"

    def draw(self, event):
        self.ax.clear()
        self.ax.grid(True)
        self.ax.set_xlim(-20, 20)
        self.ax.set_ylim(-20, 20)
        self.ax.set_aspect('equal')

        self.start_x = int(self.start_x_text.text)
        self.start_y = int(self.start_y_text.text)
        self.end_x = int(self.end_x_text.text)
        self.end_y = int(self.end_y_text.text)

        if self.algorithm_var == "step":
            points = draw_line_step(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var == "dda":
            points = draw_line_dda(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var == "bresenham":
            points = draw_line_bresenham(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var == "circle_bresenham":
            points = draw_circle_bresenham(self.start_x, self.start_y, self.end_x)
        elif self.algorithm_var == "casteljau":
            points = draw_line_casteljau(self.start_x, self.start_y, self.end_x, self.end_y)
        elif self.algorithm_var == "smooth":
            points = draw_smooth_line(self.start_x, self.start_y, self.end_x, self.end_y)

        if self.algorithm_var == "circle_bresenham":
            self.ax.plot([x for x, y in points], [y for x, y in points], 'bo')
        else:
            self.ax.plot([x for x, y in points], [y for x, y in points], 'ro')

        plt.draw()

if __name__ == "__main__":
    app = RasterAlgorithmsApp()
    plt.show()