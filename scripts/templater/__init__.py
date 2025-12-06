

__all__ = ["templates", "main"]

def generate_this(file_const):
    return {
        "filepath": str((pathlib.Path(file_const) ).resolve()),
        "dirpath": str((pathlib.Path(file_const) / "..").resolve())
    }

THIS = generate_this(__file__)

if __name__ == "__main__":
    print(__all__)
    print()
    print(__file__)
    print()
    print(THIS)