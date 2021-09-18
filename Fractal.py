from random import randint


class FractalMath():
    def __init__(self):
        self.array_points_figure = [];
        self.array_points_figure_name = [];
        self.array_function_for_point = [];
        self.yu_x = 0
        self.yu_y = 0


    def clear(self):
        self.array_points_figure = [];
        self.array_points_figure_name = [];
        self.yu_x = 0
        self.yu_y = 0


    def new_xy_default(self, pos_point):
        xx, yy = pos_point
        x = (xx - self.yu_x) / 2 + self.yu_x
        y = (yy - self.yu_y) / 2 + self.yu_y
        return (x, y)


    def new_xy_reverse_distance(self, pos_point):
        xx, yy = pos_point
        x = (yy - self.yu_y) / 2 + self.yu_y
        y = (xx - self.yu_x) / 2 + self.yu_x
        return (x, y)


    def new_xy_three_distance(self, pos_point):
        xx, yy = pos_point
        x = (xx - self.yu_x) / 3 + self.yu_x
        y = (yy - self.yu_y) / 3 + self.yu_y
        return (x, y)


    def new_xy_four_distance(self, pos_point):
        xx, yy = pos_point
        x3 = (xx - self.yu_x) / 4 + self.yu_x
        y3 = (yy - self.yu_y) / 4 + self.yu_y
        return (x3, y3)


    def new_xy_five_distance(self, pos_point):
        xx, yy = pos_point
        x = (xx - self.yu_x) / 5 + self.yu_x
        y = (yy - self.yu_y) / 5 + self.yu_y
        return (x, y)


    def get_formula(self, num_selected_point):
        int_point = self.array_points_figure_name.index(num_selected_point)
        # print(self.array_function_for_point)
        func = self.array_function_for_point[int_point]
        return func


    def operation(self, func, coords_select_point_random):
        res = func(coords_select_point_random)
        return res


    def generate_next_point(self):
        return randint(1, len(self.array_points_figure))


    def select_point(self, random_int):
        ind = self.array_points_figure_name.index(random_int)
        return self.array_points_figure[ind]

