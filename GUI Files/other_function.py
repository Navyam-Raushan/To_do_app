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


"""Because we are extracting the file so we
    open it in the read mode.
    we must provide absolute path when we call function."""


def extract_zip(zippath, dest_dir):
    with zipfile.ZipFile(zippath, "r") as file:
        file.extractall(dest_dir)


def feet_inch(feet, inches):
    return (feet * 0.3048) + (inches * 0.0254)


def fluid_ounce_mm(ounce):
    return ounce * 29.57353

# if __name__ == "__main__":
#     make_zip()
