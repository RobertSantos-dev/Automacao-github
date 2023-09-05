import os
import csv
import json


class SaveFile:
    def __init__(self) -> None:
        self.header = ['nome', 'descricao']

    def __verify_dir(self) -> bool:
        return os.path.exists(f'files')

    def save_file_csv(self, repositories: list[dict], new_file: str) -> None:
        if (not self.__verify_dir()):
            os.mkdir('files')

        with open(f'files/{new_file}.csv', 'w', newline="") as file_csv:
            writer = csv.DictWriter(file_csv, fieldnames=self.header)
            writer.writeheader()

            for repository in repositories:
                writer.writerow(repository)
    
    def save_file_json(self, repositories: list[dict], new_file: str) -> None:
        if (not self.__verify_dir()):
            os.mkdir('files')

        with open(f'files/{new_file}.json', 'w', newline="") as file_json:
            json.dump(repositories, file_json, ensure_ascii=False, indent=4)