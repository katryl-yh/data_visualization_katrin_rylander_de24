from pathlib import Path

DATA_DIRECTORY = Path(__file__).parents[0] / "data/resultat_ansokning_program"

files = [f.name for f in DATA_DIRECTORY.iterdir() if f.is_file()] 

print(files)
