from app import App
from simple_colors import red


def main():
    app = App()
    app.start()


try:
    main()
except KeyboardInterrupt:
    print("\n" + red("Cerrando aplicación de manera forzada..."))
