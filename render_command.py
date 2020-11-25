#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
name = "c3_international_place"

manifest = "manifest_z128"

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess

manifest_path = "voxel/manifest/" + manifest + ".json"

def render(name):
    input_voxel = "voxel/" + name + ".vox"
    output_sprite = "src/gfx/" + name
    gorender = subprocess.run(["C:/tools/gorender/renderobject.exe", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "C:/tools/gorender/files/ttd_palette.json"], stdout = subprocess.PIPE, stderr = subprocess.PIPE, text=True)
    print(gorender.stdout)
    print(gorender.stderr)

# Render sprite varients
render(name) # regular
render(name+"_snow") # snow
