from typing import List
import os
from pathlib import Path



from .turing import exec
from .reader import reader
from .utils import clear_screen


class TUI():
    def __init__(self, directories: List[str] = []):
        self.directories: List[str] = directories 
        self.machines_abs_path: List[Path] = [] 
        self.TailleTerminal = os.get_terminal_size().columns

        for directory in directories:
            if os.path.isdir(directory):    
                print("Reading {0}...".format(directory))
                directory_p: Path = Path(directory)
                for file in directory_p.iterdir():
                    if file.is_file() and file.suffix == ".tur":
                        self.machines_abs_path.append(file)
            else:
                print("{0} is not found or is not a directory.".format(directory))

    @clear_screen
    def show_home(self):
        print("Use machine: 1\nLink machines: 2\nOptimize machine: 3\nExit: 4\n")
        rep: str = input("Choose your command: ")
        match rep:
            case "1":
                self.show_exec()
            case "2":
                self.show_linker()
            case "3":
                self.show_optimizer()
            case "4" | _:
                exit()


    @clear_screen
    def show_exec(self):
        for ind, path in enumerate(self.machines_abs_path):
            print("({0}): {1}".format(ind, path))

        print("Choose a turing machine to execute (By its index)")
        while True:
            try:
                res: int = int(input("-> "))
                formel = reader(self.machines_abs_path[res])
                print(formel)
                exec(formel, "1001", 2, self.TailleTerminal)
                return
            except (IndexError, ValueError):
                print("You must choose an integer AND in the range of indexes shown above")
            
            

    @clear_screen
    def show_linker(self):
        pass

    @clear_screen
    def show_optimizer(self):
        pass

