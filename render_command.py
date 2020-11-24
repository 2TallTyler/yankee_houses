#################################
####### SET UP FILES HERE #######
#################################

# Name of NewGRF, as it appears in file names
name = "r1_fulton_snow"

manifest = "manifest"

#################################
# NO NEED TO CHANGE STUFF BELOW #
#################################

import subprocess
import shutil

input_voxel = "voxel/" + name + ".vox"
manifest_path = "voxel/manifest/" + manifest + ".json"
output_sprite = "src/gfx/" + name


gorender = subprocess.run(["C:/tools/gorender/renderobject.exe", "-input", input_voxel, "-m", manifest_path, "-output", output_sprite, "-8", "-palette", "C:/tools/gorender/files/ttd_palette.json"], stdout = subprocess.PIPE, text=True)
print(gorender.stdout)
