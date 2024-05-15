import os
import pymol.cmd as cmd

pymol_directory = os.path.join(os.path.expanduser("~"), "PyMOL")
fetch_directory = os.path.join(pymol_directory, "Fetch")

def init():
    cmd.bg_color("grey20")
    cmd.space("cmyk")
    cmd.set("shininess", 250)
    cmd.set("ambient_occlusion_scale", 18)
    cmd.set("mesh_widt", 0.3)
    cmd.set("cartoon_fancy_helices", 1)
    cmd.set("cartoon_oval_length", 0.8)
    cmd.set("cartoon_oval_width", 0.2)
    cmd.set("stick_radius", 0.18)
    cmd.set("cartoon_side_chain_helper", "on")
    cmd.set("antialias", 1)
    cmd.set("ray_trace_mode", 1)
    cmd.set("ray_opaque_background", 1)
    cmd.set("seq_view", 1)
    cmd.set("dash_color", "black")
    cmd.set("dash_gap", "0.3")
    cmd.set("dash_length", "0.1")
    cmd.set("dash_width", "1.5")
    # cmd.set("fetch_path", cmd.exp_path(fetch_directory), quiet=0) F Fetch directory

    capital = {'VAL':'Val', 'ILE':'Ile', 'LEU':'Leu', 'GLU':'Glu', 'GLN':'Gln', \
    'ASP':'Asp', 'ASN':'Asn', 'HIS':'His', 'TRP':'Trp', 'PHE':'Phe', 'TYR':'Tyr',    \
    'ARG':'Arg', 'LYS':'Lys', 'SER':'Ser', 'THR':'Thr', 'MET':'Mey', 'ALA':'Ala',    \
    'GLY':'Gly', 'PRO':'Pro', 'CYS':'Cys'}

    # label sele and name ca, capital[resn]
    

def view(mode="0"):
    if mode == "aa":
        cmd.set("seq_view_format", 1)
    if mode == "a":
        cmd.set("seq_view_format", 2)
    if mode == "c":
        cmd.set("seq_view_format", 3)
    cmd.set("seq_view_format", mode)

def remove_water():
    print("Water is removed.")
    cmd.remove("resn hoh")

# Surface

def surface(object, ambient_scale=18, transparency="off", level=0.5):
    cmd.set("surface_quality", 1)
    cmd.set("ambient_occlusion_mode", 1)
    cmd.set("ambient_occlusion_scale", ambient_scale)
    cmd.set("shininess", "250")
    cmd.set("surface_color", "white")
    cmd.show("surface", f"{object}")
    if transparency == "on":
        cmd.set("transparency", level)

def surface_hydrophobic(selection='all', ambient_scale=18, transparency="off", level=0.7):
    s = str(selection)
    cmd.set("surface_quality", 1)
    cmd.set("ambient_occlusion_mode", 1)
    cmd.set("ambient_occlusion_scale", ambient_scale)
    cmd.set("surface_color", "default")
    cmd.show("surface", f"{selection}")
    if transparency == "on":
      cmd.set("transparency", level)
    cmd.set_color('color_ile',[0.996,0.062,0.062])
    cmd.set_color('color_phe',[0.996,0.109,0.109])
    cmd.set_color('color_val',[0.992,0.156,0.156])
    cmd.set_color('color_leu',[0.992,0.207,0.207])
    cmd.set_color('color_trp',[0.992,0.254,0.254])
    cmd.set_color('color_met',[0.988,0.301,0.301])
    cmd.set_color('color_ala',[0.988,0.348,0.348])
    cmd.set_color('color_gly',[0.984,0.394,0.394])
    cmd.set_color('color_cys',[0.984,0.445,0.445])
    cmd.set_color('color_tyr',[0.984,0.492,0.492])
    cmd.set_color('color_pro',[0.980,0.539,0.539])
    cmd.set_color('color_thr',[0.980,0.586,0.586])
    cmd.set_color('color_ser',[0.980,0.637,0.637])
    cmd.set_color('color_his',[0.977,0.684,0.684])
    cmd.set_color('color_glu',[0.977,0.730,0.730])
    cmd.set_color('color_asn',[0.973,0.777,0.777])
    cmd.set_color('color_gln',[0.973,0.824,0.824])
    cmd.set_color('color_asp',[0.973,0.875,0.875])
    cmd.set_color('color_lys',[0.899,0.922,0.922])
    cmd.set_color('color_arg',[0.899,0.969,0.969])
    cmd.color("color_ile","("+s+" and resn ile)")
    cmd.color("color_phe","("+s+" and resn phe)")
    cmd.color("color_val","("+s+" and resn val)")
    cmd.color("color_leu","("+s+" and resn leu)")
    cmd.color("color_trp","("+s+" and resn trp)")
    cmd.color("color_met","("+s+" and resn met)")
    cmd.color("color_ala","("+s+" and resn ala)")
    cmd.color("color_gly","("+s+" and resn gly)")
    cmd.color("color_cys","("+s+" and resn cys)")
    cmd.color("color_tyr","("+s+" and resn tyr)")
    cmd.color("color_pro","("+s+" and resn pro)")
    cmd.color("color_thr","("+s+" and resn thr)")
    cmd.color("color_ser","("+s+" and resn ser)")
    cmd.color("color_his","("+s+" and resn his)")
    cmd.color("color_glu","("+s+" and resn glu)")
    cmd.color("color_asn","("+s+" and resn asn)")
    cmd.color("color_gln","("+s+" and resn gln)")
    cmd.color("color_asp","("+s+" and resn asp)")
    cmd.color("color_lys","("+s+" and resn lys)")
    cmd.color("color_arg","("+s+" and resn arg)")

def surface_yrb(selection='all', ambient_scale=18, transparency="off", level=0.5):

    cmd.set("surface_quality", "1")
    cmd.set("ambient_occlusion_mode", "1")
    cmd.set("ambient_occlusion_scale", ambient_scale)
    cmd.set("shininess", "250")
    cmd.set("surface_color", "default")
    cmd.show("surface", f"{selection}")
    if transparency == "on":
        cmd.set("transparency", level)
    cmd.set_color('yellow',[0.950,0.78,0.0])
    cmd.set_color('grey',[0.95,0.95,0.95])
    cmd.set_color('red',[1.0,0.4,0.4])
    cmd.set_color('blue',[0.2,0.5,0.8])

    mapping = {}
    mapping['arg'] = [ ('NE,NH2,NH1', 'blue'), ('CD,CZ', 'grey'), ('CG', 'yellow') ]
    mapping['asn'] = [ ('CG,OD1,ND2', 'grey') ]
    mapping['asp'] = [ ('CG', 'grey'), ('OD2,OD1', 'red')  ]
    mapping['cys'] = [ ('SG', 'grey') ]
    mapping['gln'] = [ ('CG', 'yellow'), ('CD,OE1,NE2', 'grey') ]
    mapping['glu'] = [ ('CG', 'yellow'), ('CD', 'grey'), ('OE1,OE2', 'red') ]
    mapping['his'] = [ ('CG,CD2,ND1,NE2,CE1', 'grey') ]
    mapping['ile'] = [ ('CG1,CG2,CD1', 'yellow') ]
    mapping['leu'] = [ ('CG,CD1,CD2', 'yellow') ]
    mapping['lys'] = [ ('CG,CD', 'yellow'), ('CE', 'grey'), ('NZ', 'blue') ]
    mapping['met'] = [ ('CG,CE', 'yellow'), ('SD', 'grey') ]
    mapping['phe'] = [ ('CG,CD1,CE1,CZ,CE2,CD2', 'yellow') ]
    mapping['pro'] = [ ('CG', 'yellow'), ('CD', 'grey') ]
    mapping['ser'] = [ ('CB,OG', 'grey') ]
    mapping['thr'] = [ ('CB,OG1', 'grey'), ('CG2', 'yellow') ]
    mapping['trp'] = [ ('CG,CD2,CZ2,CH2,CZ3,CE3', 'yellow'), ('CD1,NE1,CE2', 'grey') ]
    mapping['tyr'] = [ ('CG,CE1,CD1,CE2,CD2', 'yellow'), ('CZ,OH', 'grey') ]
    mapping['val'] = [ ('CG1,CG2', 'yellow') ]

def surface_hide(object):
    cmd.hide("surface", object)

# Transparency

def transparency(type, selection, level):
    if type == "cartoon":
        name = "temp"
        cmd.select(name, f"{selection}")
        cmd.set("cartoon_transparency", level, name)
        cmd.delete(name)
    elif type == "sticks":
        name = "temp"
        cmd.select(name, f"{selection}")
        cmd.set("stick_transparency", level, name)
        cmd.delete(name)

# Selection

def side(objects):
    objects = objects.split(" ")
    if len(objects) == 1 and objects[0] == "obj":
        extraction = " ".join(cmd.get_names("objects", 1))
        cmd.select(f"({extraction}) and not name C and not name O and not name N and not name CA")
    else:
        for object in objects:
            cmd.select(f"{object} and not name C and not name O and not name N and not name CA")

def main(objects):
    objects = objects.split(" ")
    if len(objects) == 1 and objects[0] == "obj":
        extraction = " ".join(cmd.get_names("objects", 1))
        cmd.select(f"({extraction}) and name C and name O and name N and name CA")
    else:
        for object in objects:
            cmd.select(f"{object} and name C and name O and name N and name CA")

def remove(objects):
    objects = objects.split(" ")
    if len(objects) == 1 and objects[0] == "obj":
        for object in cmd.get_names("objects", 1):
            cmd.delete(object)
    else:
        for object in objects:
            cmd.delete(object)

# Extraction/Copy

def chains(object): # Extracts chains
    list = cmd.get_chains(object)
    for chain in list:
        sele = f"Chain_{chain}_{object}"
        cmd.extract(sele, f"chain {chain} and {object}")

def pocket_resi(objects, resi): # Copy pocket based on resi
    objects = objects.split(" ")
    if len(objects) == 1 and objects[0] == "obj":
        for object in cmd.get_names("objects", 1):
            name = f"Pocket_{object}"
            cmd.select(f"{object} and resi {resi}")
            cmd.show_as("sticks", "sele")
            cmd.set_bond("stick_radius", 0.07, "sele")
            cmd.copy_to(f"{name}", "sele")
            cmd.show_as("cartoon", "sele")
            cmd.color("white", f"{name} and name c+ca")
            cmd.color("blue", f"{name} and name n")
            cmd.color("red", f"{name} and name o")
            cmd.delete("sele")
    else:
        for object in objects:
            name = f"Pocket_{object}"
            cmd.select(f"{object} and resi {resi}")
            cmd.show_as("sticks", "sele")
            cmd.set_bond("stick_radius", 0.07, "sele")
            cmd.copy_to(f"{name}", "sele")
            cmd.show_as("cartoon", "sele")
            cmd.color("white", f"{name} and name c+ca")
            cmd.color("blue", f"{name} and name n")
            cmd.color("red", f"{name} and name o")
            cmd.delete("sele")

def pocket_sele(object, selection): # Copy pocket based on selection
    name = f"Pocket_sele_{object}"
    cmd.select(f"{object} and {selection}")
    cmd.show_as("sticks", "sele")
    cmd.set_bond("stick_radius", 0.07, "sele")
    cmd.copy_to(f"{name}", "sele")
    cmd.show_as("cartoon", "sele")
    cmd.color("white", f"{name} and name c+ca")
    cmd.color("blue", f"{name} and name n")
    cmd.color("red", f"{name} and name o")
    # cmd.delete("sele")

def pocket_around(object, ligand, distance):
    name = f"Pocket-{distance}_{object}"
    cmd.select(f"{object} and (resn {ligand} around {distance})")
    selection = cmd.get_model(f"sele and name CA")
    resi = [atom.resi for atom in selection.atom]
    resn = [atom.resn.capitalize() for atom in selection.atom]
    comb = [f"{residue}{integer}" for residue, integer in zip(resn, resi)]
    comb_dict = {key:value for key, value in zip(resn, resi)}
    print(f"\nResidues around {distance} Angstrems from {ligand}:\n",", ".join(comb))
    print("\nPyMOL resi format:\n", "+".join(resi))
    print("\n.json format:\n" ,comb_dict)
    cmd.show_as("sticks", "sele")
    cmd.set_bond("stick_radius", 0.07, "sele")
    cmd.copy_to(f"{name}", "sele")
    cmd.show_as("cartoon", "sele")
    cmd.color("white", f"{name} and name c+ca")
    cmd.color("blue", f"{name} and name n")
    cmd.color("red", f"{name} and name o")
    cmd.delete("sele")

def ligand(object, ligand_resn, ligand_name): # Extracts ligand
    sele = f"Ligand_{ligand_name}"
    cmd.extract(sele, f"resn {ligand_resn} and {object}")
    cmd.show_as("sticks", sele)
    cmd.show("spheres", sele)
    cmd.set("sphere_scale", 0.3)

# Visual effects

def radius(object, level):
    cmd.set_bond("stick_radius", f"{level}", f"{object}")

# Console

def obj(): # Prints all enabled objects
    print(" ".join(cmd.get_names("objects", 1)))

def fasta(selection): # Prints FASTA
    print("\n")
    fasta = cmd.get_fastastr(selection)
    print(fasta)
    if "?" in fasta:
        print("Modifications present")

# Align

def align_custom(mobile, target):
    mobile = mobile.split(" ")
    for object in mobile:
        cmd.align(mobile=object, target=target)

init()
cmd.extend('v', view)
cmd.extend('w', remove_water)
cmd.extend('surface', surface)
cmd.extend('surface_hydrophobic', surface_hydrophobic)
cmd.extend('surface_yrb', surface_yrb)
cmd.extend('surface_hide', surface_hide)
cmd.extend('transparency', transparency)
cmd.extend('side', side)
cmd.extend('chains', chains)
cmd.extend('pocket_resi', pocket_resi)
cmd.extend('radius', radius)
cmd.extend('pocket_sele', pocket_sele)
cmd.extend('ligand', ligand)
cmd.extend('obj', obj)
cmd.extend('fasta', fasta)
cmd.extend('pocket_around', pocket_around)
cmd.extend('align_custom', align_custom)
cmd.extend('remove', remove)
cmd.extend('main', main)