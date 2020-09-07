import click
from click_shell import shell
from geometric_tool.figures import Circle, Rectangle, Square, Triangle

figure_dict = {}


def sort_area(fig):
    return fig.calculate_area()


def sort_perimeter(fig):
    return fig.calculate_perimeter()


@shell(prompt='Geometric_tool > ',
       intro='Figure inc. Geometric Tool \n Created by Federico Cumiano')
def my_app():
    pass


@my_app.group()
def create():
    pass


@create.command()
@click.option("--name",
              prompt="Name of the Circle",
              help="The name of the circle.")
@click.option("--radius",
              type=float,
              prompt="Radius",
              help="Radius of the circle.")
def circle(name, radius):
    # figure_list.append(Circle(name, radius))
    figure_dict[name] = Circle(name, radius)
    click.echo(f"{name} created. Circle with radius {radius}")


@create.command()
@click.option("--name",
              prompt="Name of the Triangle",
              help="The name of the triangle.")
@click.option("--sides",
              type=float,
              nargs=3,
              prompt="Sides",
              help="Sides of the triangle, separated by space.")
def triangle(name, sides):
    figure_dict[name] = Triangle(name, *sides)
    click.echo(
        f"{name} created. Triangle with sides {sides[0]}, {sides[1]}, {sides[2]}"
    )


@create.command()
@click.option("--name",
              prompt="Name of the Rectangle",
              help="The name of the rectangle.")
@click.option("--sides",
              type=float,
              nargs=2,
              prompt="Sides",
              help="Sides of the rectangle, separated by space.")
def rectangle(name, sides):
    figure_dict[name] = Rectangle(name, *sides)
    click.echo(f"{name} created. Rectangle with sides {sides[0]}, {sides[1]}")


@create.command()
@click.option("--name",
              prompt="Name of the Square",
              help="The name of the square.")
@click.option("--side", type=float, prompt="Side", help="Side of the square.")
def square(name, side):
    figure_dict[name] = Square(name, side)
    click.echo(f"{name} created. Square with side {side}")


@my_app.command()
@click.option("--sort",
              default="",
              type=click.Choice(["", "area", "perimeter"],
                                case_sensitive=False),
              help="You can sort the list by area or perimeter.")
def ls(sort):
    figure_list = []
    for key in figure_dict.keys():
        figure_list.append(figure_dict[key])
    click.echo("Showing list...")
    if sort == "area":
        click.echo("Sorting by area...")
        figure_list.sort(key=sort_area)
    elif sort == "perimeter":
        click.echo("Sorting by perimeter...")
        figure_list.sort(key=sort_perimeter)
    for fig in figure_list:
        print(fig)
    if len(figure_list) == 0:
        click.echo("No figures to print.")


@my_app.command()
@click.option("--name",
              default="",
              help="The name of the figure to fetch area.")
def area(name):
    if name:
        click.echo(f"Searching for {name}...")
        if name in figure_dict:
            click.echo("Figure found!")
            click.echo(
                f"Name: {name}, Area: {figure_dict[name].calculate_area()}")
        else:
            click.echo("Figure not found.")
    else:
        click.echo("Printing all areas:")
        for figure in figure_dict.values():
            click.echo(f"Name: {figure.name}, Area: {figure.calculate_area()}")


@my_app.command()
@click.option("--name",
              default="",
              help="The name of the figure to fetch perimeter.")
def perimeter(name):
    if name:
        click.echo(f"Searching for {name}...")
        if name in figure_dict:
            click.echo("Figure found!")
            click.echo(
                f"Name: {name}, Perimeter: {figure_dict[name].calculate_perimeter()}"
            )
        else:
            click.echo("Figure not found.")
    else:
        click.echo("Printing all perimeters:")
        for figure in figure_dict.values():
            click.echo(
                f"Name: {figure.name}, Perimeter: {figure.calculate_perimeter()}"
            )


@my_app.group()
def add():
    pass


@add.command()
@click.option("--figure1",
              prompt="Name of figure 1: ",
              help="The name of the first figure to add.")
@click.option("--figure2",
              prompt="Name of figure 2: ",
              help="The name of the second figure to add.")
def perimeter(figure1, figure2):
    if figure1 in figure_dict and figure2 in figure_dict:
        click.echo(f"Adding {figure1}´s, and {figure2}´s perimeters...")
        result = figure_dict[figure1].calculate_perimeter(
        ) + figure_dict[figure2].calculate_perimeter()
        click.echo(f"Result: {result}")
    else:
        click.echo("You must input two valid figure names.")


@add.command()
@click.option("--figure1",
              prompt="Name of figure 1: ",
              help="The name of the first figure to add.")
@click.option("--figure2",
              prompt="Name of figure 2: ",
              help="The name of the second figure to add.")
def area(figure1, figure2):
    if figure1 in figure_dict and figure2 in figure_dict:
        click.echo(f"Adding {figure1}´s, and {figure2}´s areas...")
        result = figure_dict[figure1].calculate_area(
        ) + figure_dict[figure2].calculate_area()
        click.echo(f"Result: {result}")
    else:
        click.echo("You must input two valid figure names.")


@my_app.group()
def sub():
    pass


@sub.command()
@click.option("--figure1",
              prompt="Name of figure 1: ",
              help="The name of the first figure to add.")
@click.option("--figure2",
              prompt="Name of figure 2: ",
              help="The name of the second figure to add.")
def perimeter(figure1, figure2):
    if figure1 in figure_dict and figure2 in figure_dict:
        click.echo(f"Subtracting {figure1}´s, and {figure2}´s perimeters...")
        result = figure_dict[figure1].calculate_perimeter(
        ) - figure_dict[figure2].calculate_perimeter()
        click.echo(f"Result: {result}")
    else:
        click.echo("You must input two valid figure names.")


@sub.command()
@click.option("--figure1",
              prompt="Name of figure 1: ",
              help="The name of the first figure to add.")
@click.option("--figure2",
              prompt="Name of figure 2: ",
              help="The name of the second figure to add.")
def area(figure1, figure2):
    print("This function subtracts the areas for two objects")
    if figure1 in figure_dict and figure2 in figure_dict:
        click.echo(f"Subtracting {figure1}´s, and {figure2}´s areas...")
        result = figure_dict[figure1].calculate_area(
        ) - figure_dict[figure2].calculate_area()
        click.echo(f"Result: {result}")
    else:
        click.echo("You must input two valid figure names.")


if __name__ == '__main__':
    my_app()
