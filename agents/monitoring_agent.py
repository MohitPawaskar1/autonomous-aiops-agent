from pathlib import Path

def read_logs():
    log_file = Path("data/sample_logs.txt")

    with open(log_file, "r") as f:
        logs = f.readlines()

    return "".join(logs)