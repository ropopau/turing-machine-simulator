# Turing Machine Simulator
## Quickstart

To test with the givens turing machine files:

Do, at the project root:
```bash
poetry install
poetry run tms -d ./turs
```

Then follow the instruction.

## How to write a .tur file

I will not really explain how a turing machine formal description works, but more about the syntax:

you have first 4 mandatory headers:
- `&name` -> the name of your machine
- `&init` -> the initial state
- `&accept` -> the accepting state
- `&nbr` -> the number of tapes

Then for the transitions:

- One transition follows the following syntax (example for a 2 tapes machine):
```
qInit,ReadTape1,ReadTape2
qNext,WriteTape1,WriteTape2,MoveTape1,MoveTape2
```
Just look at the examples for more understanding

- For the movements, `>` is to go right, `<` to go left and `-` to not move

- `#` is for empty character

- `*` is for any character