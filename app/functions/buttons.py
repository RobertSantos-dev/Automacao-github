from jobs.visit_github import visit_github
from functions.save_file import SaveFile


class ButtonsEvent():
    def __init__(self, files: SaveFile) -> None:
        self.files = files
        self.repositories: list[dict] = []

    def btn_search(self, value: dict, app, rendering_two):
        digit = value.get()
        self.__clear_elements(app)
        self.repositories = visit_github(digit)
        rendering_two()

    def btn_save(self, value: dict, app):
        digit = value.get()
        self.files.save_file_csv(self.repositories, digit)
        self.files.save_file_json(self.repositories, digit)
        self.__close(app)

    def __clear_elements(self, app):
        for widget in app.winfo_children():
            widget.destroy()

    def __close(self, app):
        app.destroy()