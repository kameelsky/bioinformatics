from dataclasses import dataclass, field
import json
import os
try:
    import typer
    from typing_extensions import Annotated
    import pymol.cmd as cmd
    from pymol import CmdException
except ModuleNotFoundError:
    print("\nScript requires PyMOL and typer modules.\n")
    quit()

@dataclass
class PyMOL:

    pdb: str
    name: str = field(default_factory=str, repr=False, init=False)
    ligand: str
    distance: float = field(default=10)
    resi: list[int] = field(default_factory=list[int], repr=False, init=False)
    resn: list[str] = field(default_factory=list[str], repr=False, init=False)
    dictionary_format: dict = field(default_factory=dict, repr=True, init=False)

    def extract_pdb_name(self):
        self.name = os.path.splitext(self.pdb)[0]

    def pocket(self):
        try:
            cmd.load(self.pdb)
            cmd.select("pocket", f"{self.name} and (resn {self.ligand} around {self.distance})")
            selection = cmd.get_model("pocket and name CA")
            self.resi = [atom.resi for atom in selection.atom]
            self.resn = [atom.resn for atom in selection.atom]
            self.dictionary_format = {key:value for key, value in zip(self.resn, self.resi)}
        except CmdException as error:
            print("\n", error, "Check the name.")

    def __post_init__(self):
        self.extract_pdb_name()
        self.pocket()

def main(pdb: Annotated[str, typer.Argument()],
         ligand: Annotated[str, typer.Argument()],
         distance: Annotated[float, typer.Argument(help="Distance from the ligand in Angstrems")] = 8.0,
         format: Annotated[str, typer.Option(help="Export format: txt, json")] = "txt",
         export: Annotated[bool, typer.Option(help="Print the output in the console window")] = False,
         ):
    
    """
    INSTRUCTIONS:

    Provide the PDB file and the name of the LIGAND, e.g.:
    python <script_name.py> 1xjd.pdb STU

    Change the default distance by adding '--distance' option, e.g.:
    python <script_name.py> 1xjd.pdb STU --distance 10
    """

    pml = PyMOL(pdb, ligand, distance)

    if format == "txt":

        output = [f"{atom_resn.capitalize()}{atom_resi}" for atom_resi, atom_resn in zip(pml.resi, pml.resn)]

        for _ in output:
            print(_)

        if export == True:
            with open(f"{pml.name}_{pml.distance}A.txt", "w") as f:
                for atom_resi, atom_resn in zip(pml.resi, pml.resn):
                    f.write(f"{atom_resi} {atom_resn}\n")
        else:
            pass

    elif format == "json":

        indent: int = 2

        output = output = json.dumps(pml.dictionary_format, indent=indent)
        print(output)

        if export == True:
            with open(f"{pml.name}_{pml.distance}A.txt", "w") as file:
                json.dump(pml.dictionary_format, file, indent=indent)
        else:
            pass
        
    
if __name__ == "__main__":
    typer.run(main)
