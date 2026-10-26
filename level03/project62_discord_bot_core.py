"""Project 62: Discord bot command core; discord.py integration is intentionally separate."""
from __future__ import annotations

COMMANDS={
    "help": "Available commands: !help, !about, !ping",
    "about": "I am a local demo command handler, not connected to Discord.",
    "ping": "Pong!",
}

def handle_command(message: str) -> str | None:
    """Handle a supported prefix command; return None for ordinary chat."""
    if not isinstance(message, str):
        raise ValueError("message must be a string")
    stripped=message.strip()
    if not stripped.startswith("!"):
        return None
    command=stripped[1:].split(maxsplit=1)[0].lower() if stripped[1:].strip() else ""
    return COMMANDS.get(command, "Unknown command. Type !help for available commands.")

if __name__ == "__main__":
    print("Discord command core (offline; not connected to Discord)")
    while True:
        msg=input("Message (quit to exit): ")
        if msg.strip().lower()=="quit": break
        reply=handle_command(msg)
        if reply is not None: print(reply)
