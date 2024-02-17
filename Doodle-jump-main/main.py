def main() -> None:
    import pygame, sys
    from scripts.app import App

    pygame.init()
    app = App()
    app.run()
    pygame.quit()

if __name__ == "__main__":
    main()

