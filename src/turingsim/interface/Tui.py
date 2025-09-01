from typing import List
import os
from pathlib import Path


from ..core.TuringMachine import TuringMachine
from ..utils.reader import reader
from ..utils.misc import clear_screen


class Tui():
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


    def home_or_exit(self):                  
        print("========================================")
        print("| (1): Return to home menu | (2): Exit |")
        print("========================================")

        rep: str = input("Choose an option by its index -> ")
        match rep:
            case "1":
                self.show_home()
            case "2":
                exit()


    @clear_screen
    def show_home(self):
        print("============================================================================")
        print("| ╔╦╗┬ ┬┬─┐┬┌┐┌┌─┐  ╔╦╗┌─┐┌─┐┬ ┬┬┌┐┌┌─┐                                    |")
        print("|  ║ │ │├┬┘│││││ ┬  ║║║├─┤│  ├─┤││││├┤                                     |")
        print("|  ╩ └─┘┴└─┴┘└┘└─┘  ╩ ╩┴ ┴└─┘┴ ┴┴┘└┘└─┘                                    |")
        print("| ╔═╗┬┌┬┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐                                                |")            
        print("| ╚═╗│││││ ││  ├─┤ │ │ │├┬┘                                                |")            
        print("| ╚═╝┴┴ ┴└─┘┴─┘┴ ┴ ┴ └─┘┴└─                  by Sanghyeon PARK (ropopau)   |")    
        print("============================================================================")
        print("| (1): Use machine | (2): Link machine | (3): Optimize machine | (4): Exit |")
        print("============================================================================")

        rep: str = input("Choose an option by its index -> ")
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
        print("============= Found .tur files =============")
        if len(self.machines_abs_path) == 0:
            print("No .tur files found in the given paths")
            self.home_or_exit()

        for ind, path in enumerate(self.machines_abs_path):
            print("({0}): {1}".format(ind, path))
        print("============================================")
        print("Choose a turing machine by its index")
        while True:
            try:
                res: int = int(input("-> "))
                formel = reader(self.machines_abs_path[res])
                tur: TuringMachine = TuringMachine(formel)
                word: str = input("Type a word\n-> ")
                speed: int = int(input("Choose an execution speed from 1 to 5 (1 is the slowest 5 is the fastest)\n-> "))
                if speed < 1 or speed > 5:
                    print("Invalid speed. Executing with default speed")
                    speed = 1

                real_speed: float = (5 - speed) / 4

                tur.exec(word, real_speed, self.TailleTerminal)
                self.home_or_exit(); 
            except (IndexError, ValueError) as e:
                print("Invalid input")
            except (KeyboardInterrupt):
                exit()
            

    @clear_screen
    def show_linker(self):
        print("Not implemented yet.")
        self.home_or_exit()



    @clear_screen
    def show_optimizer(self):
        print("Not implemented yet.")
        self.home_or_exit()


