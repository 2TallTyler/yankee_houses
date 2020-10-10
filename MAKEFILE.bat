@ECHO OFF

ECHO Running GoRender

rem ECHO Rendering buildings
C:\Users\train\Documents\gorender\renderobject.exe -input voxel\house.vox -manifest files\manifest.json -output src\gfx\house  -8

exit


ECHO Batch: Running Python file merger
python %~dp0\nmlc\merge_nml.py

ECHO Batch: Copying merged file to src/merged directory
copy /y /v %~dp0\nmlc\yankee_houses.nml %~dp0\src\merged\yankee_houses.nml

ECHO Batch: Running NMLC compiler
%~dp0\nmlc\nmlc -c -t src\custom_tags.txt -l src\lang --grf yankee_houses.grf nmlc\yankee_houses.nml

ECHO Batch: Cleaning up
DEL %~dp0\nmlc\yankee_houses.nml

set /P c=Complete!
if /I "%c%" EQU "TT" (goto :copy
) else (exit)

:copy
ECHO Copying to NewGRF directory
copy /y /v %~dp0\yankee_houses.grf C:\Users\train\Documents\OpenTTD\newgrf\
pause
exit
