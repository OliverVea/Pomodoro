import typer

def main():
    typer.run(typermain)

def typermain(name: str):
    print(f'Hello, {name}!')

if __name__ == '__main__':
    main()