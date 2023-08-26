import zipfile
import pathlib


# dest_folder should be the complete path not a folder name
# use pathmaker library to create path

def make_zip(filepaths, dest_folder):
    dest_path = pathlib.Path(dest_folder, "compress.zip")
    with zipfile.ZipFile(dest_path, "w") as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


def feet_inch(feet, inches):
    return (feet * 0.3048) + (inches * 0.0254)


def fluid_ounce_mm(ounce):
    return ounce * 29.57353

# if __name__ == "__main__":
#     make_zip()
