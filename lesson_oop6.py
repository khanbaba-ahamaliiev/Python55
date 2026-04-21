from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Optional

class Status(Enum):
    working = 'working'
    vacation = 'vacation'
    offline = 'offline'


class Employee(ABC):
    def __init__(
            self,
            name:str,
            salary:int,
            status:Status = Status.working,
    ):

        self._name = name
        self._salary = salary
        self._status = status

    def info(self):
        print(f'Name: {self._name}, Salary: {self._salary}, \nStatus: {self._status.value}')

    def start_work(self):
        self._status = Status.working

    def take_vacation(self):
        self._status = Status.vacation

    def increase_salary(self, amount):
        self._salary += amount


class Programmer(Employee):
    def __init__(
            self,
            name:str,
            salary:int,
            language:str,
            projects: Optional[List[str]] = None,
            bugs_fixed:int = 0,
            status: Status = Status.working
    ):
        super().__init__(name, salary, status)

        self._language = language
        self._bugs_fixed = bugs_fixed

        if projects is None:
            self._projects = []
        else:
            self._projects = projects

    def info(self):
        super().info()
        print(f"Projects: {self._projects}")
        print(f"Language: {self._language}")
        print(f"Bugs Fixed: {self._bugs_fixed}")

    def add_project(self, project:str):
        self._projects.append(project)

    def fix_bug(self, count:int):
        self._bugs_fixed += count

    def change_language(self, new_language:str):
        self._language = new_language



pr1 = Programmer(
    'Mike',
    1000,
    'Python'
)

pr2 = Programmer('Mary',
    1000,
    'Java'
)

pr1.info()
pr2.info()


class Designer(Employee):
    def __init__(
        self,
        name: str,
        salary: int,
        tool: str,
        style: str,
        works_done: int = 0,
        status: Status = Status.working,
    ):
        super().__init__(name, salary, status)

        self._tool = tool
        self._style = style
        self._works_done = works_done

    def info(self):
        super().info()
        print(f"Tool: {self._tool}")
        print(f"Style: {self._style}")
        print(f"Works Done: {self._works_done}")

    def create_design(self):
        self._works_done += 1

    def change_style(self, new_style: str):
        self._style = new_style

    def change_tool(self, new_tool: str):
        self._tool = new_tool
