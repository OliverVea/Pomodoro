import typer

from climodoro.pomodoro_configuration import get_configuration_order
from climodoro.pomodoro import Pomodoro

app = typer.Typer()

@app.command('start')
def start():
    order = get_configuration_order()
    pomodoro = Pomodoro()

    i = 0
    while True:
        pomodoro.run(order[i])

        if pomodoro.quit:
            exit()

        i = (i + 1) % len(order)

if __name__ == '__main__':
    app()