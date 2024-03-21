from subprocess import CalledProcessError, run


def generate_requirements_txt():
    """Generate requirements.txt file"""

    command = [
        "poetry",
        "export",
        "-f",
        "requirements.txt",
        "--output",
        "requirements.txt",
    ]

    try:
        run(command, capture_output=True, check=True)

    except CalledProcessError as e:
        print(
            f"Couldn't generate Requirements.txt file, this is the reason: {e.stderr.decode()}"
        )

    else:
        print("Requirements.txt generated successfully")


generate_requirements_txt()
