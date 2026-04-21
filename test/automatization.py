from pathlib import Path
import shutil

route_one = Path("test-folder")
route_two = Path("test-folder-two")

if any(route_one.iterdir()):
    for archivo in route_one.iterdir():
        if archivo.is_file() and archivo.suffix in (".jpg", ".png"):
            address = (route_two / archivo.name)
            shutil.move(archivo, address)
if any(route_two.iterdir()):
    for archivo in route_two.iterdir():
        if archivo.is_file() and archivo.suffix in (".jpg", ".png"):
            address = (route_one / archivo.name)
            shutil.move(archivo, address)
