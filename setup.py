import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_freeze.setup(
    name="Snake Game",
    options={"build_exe": {"packages": ["pygame"],
                           "included_files": []}}
)
