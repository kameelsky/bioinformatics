import string, os
from time import sleep

def list_records(pdb: str, option: str) -> list:
    if option == "1":
        with open(pdb, "r") as f:
            lines_all = f.readlines()
            lines = [line for line in lines_all if line.startswith("ATOM") and "MOL" in line]
            return lines
    elif option == "2":
        with open(pdb, "r") as f:
            lines_all = f.readlines()
            lines = [line for line in lines_all if line.startswith(("ATOM", "HETATM"))]
            return lines
    elif option == "3":
        record_types = []
        print("\n")
        while True:
            record = input("\tRecord type: ")
            if record != "":
                record_types.append(record)
                continue
            elif record == "":
                break
        residue_name = input("\n\tResidue name: ")
        with open(pdb, "r") as f:
            lines_all = f.readlines()
            lines = [line for line in lines_all if line.startswith(tuple(record_types)) and residue_name in line]
            return lines

def extract_atom_name(records: list) -> list:
    l = []
    for record in records: 
        scope = record[12:16]
        output1 = []     
        if scope[0] == "H" and scope[1] in [i for i in string.ascii_uppercase[0:8]] and len([i for i in scope if i != " "]) == 4:
            output1.append("H")
        elif scope[1:4] == "HXT":
            output1.append("H")
        elif scope[1:4] == "OXT":
            output1.append("O")
        elif scope[1:3] == "HZ":
            output1.append("H")
        elif scope[1:3] == "NZ":
            output1.append("N")
        elif scope[1:3] == "CZ":
            output1.append("C")
        else:
            if scope[0] == " " and scope[1] in ["S", "C", "H", "N", "O", "P"] and scope[2] in ([i for i in string.ascii_uppercase[0:8]] + [str(i) for i in range(1,10)] + [" "]):
                output1.append(scope[1])
            elif scope[0] == " " and scope[1] in ["S", "C", "H", "N", "O", "P"] and scope[2] not in ([i for i in string.ascii_uppercase[0:8]] + [str(i) for i in range(1,10)]):
                output1.append(scope[1])
                output1.append(scope[2])
            else:
                if scope[0] != "H" and scope[1] != " ":
                    output1.append(scope[0])
                    output1.append(scope[1])
                if scope[0] != "H" and scope[1] in [i for i in range(0,10)]:
                    output1.append(scope[0])
                else:
                    pass
        output2 = "".join(output1).lower().capitalize()
        l.append(output2)
    return l

def correction(list_of_records: list, list_of_atoms: list):
    new_list = []
    MyDict = zip(list_of_records, list_of_atoms)
    for record, atom in MyDict:
        record = list(record)
        if len(atom) == 1:
            record[77] = atom[0]
        elif len(atom) == 2:
            record[76] = atom[0]
            record[77] = atom[1]
        new_list.append("".join(record))
    return new_list

class Main:
    """
    The script fills in the missing elemet symbol in .pdb files.
    """

    def pdb():
        Options_dict = {key:value for key,value in enumerate(["Record type: 'ATOM'; Residue name: 'MOL'", 
                                                            "Record type: ['ATOM', 'HETATM']",
                                                            "User default"], start=1)}
        pdb = input("# Provide the name/location of the .pdb file (e.g. input.pdb): ")
        print("\n# Options of filtering:\n")
        for key, value in Options_dict.items():
            print(f"\t{key}. {value}")
        option = input("\n\tSelect number: ")
        return pdb, option
        
    def corrections(user_option: str, pdbFile: str, write_to_pdb: bool = True):
        records = list_records(pdb=pdbFile, option=user_option)
        atoms = extract_atom_name(records=records)
        corrections = correction(records, atoms)
        with open(pdbFile, "r") as f:
            filedata = f.read()
        for wrong, correct in zip(records, corrections):
            filedata = filedata.replace(wrong, correct)
        print(filedata)
        if write_to_pdb == True:
            new_name = "correct_" + os.path.basename(pdbFile)
            with open(new_name, "w") as f:
                f.write(filedata)
            print(f"Corrected .pdb file: {os.path.abspath(new_name)}")
            
    def root():
        print("* " * 50, "\n", Main.__doc__)
        sleep(1)
        while True:
            pdb, option = Main.pdb()
            Main.corrections(pdbFile=pdb, user_option=option)
            anw = input("\nDo you want to repeat? (y/n): ")
            if anw.lower() == "y":
                print("\n")
                continue
            else:
                print("\nExiting.")
                break
              
if __name__=="__main__":
    Main.root()