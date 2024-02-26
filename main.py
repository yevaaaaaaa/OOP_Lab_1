from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.trapeze import Trapeze
from figures.triangle import Triangle

def create_figure(figure_info: list[str]):
    figure_type = figure_info.pop(0)
    figure = None
    
    if figure_type == 'Circle':
        figure = Circle(*figure_info)
        
    elif figure_type == 'Parallelogram':
        pass
    
    elif figure_type == 'Rectangle':
        figure = Rectangle(*figure_info)
        
    elif figure_type == 'Trapeze':
        figure = Trapeze(*figure_info)
        
    elif figure_type == 'Triangle':
        figure = Triangle(*figure_info)
    
    return figure

if __name__ == "__main__":
    filepaths_to_read = ['inputs/input01.txt', 'inputs/input02.txt', 'inputs/input03.txt']
    for filepath in filepaths_to_read:
        
        print('==============================')
        print(f"filepath - {filepath}")
        print('==============================')
        
        figures = []
        
        # read from file
        with open(filepath, 'r') as file:
            for line in file:
                
                figure_info = line.split()
                figure = create_figure(figure_info)
                
                if figure:
                    figures.append(figure)
                
        # max area
        figure_with_max_area = max(figures, key=lambda figure: figure.area())
        print(f'Max area is: {figure_with_max_area.area()}')
        
        # max perimeter
        figure_with_max_perimeter = max(figures, key=lambda figure: figure.perimeter())
        print(f'Max perimeter is: {figure_with_max_perimeter.perimeter()}')
        