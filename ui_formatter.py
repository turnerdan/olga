
def format_response(text: str, mode: str) -> str:
    """
    Formats Olga's responses based on mode, for cleaner CLI output.
    Modes: 'work', 'play', 'shared'
    """
    mode_prefixes = {
        "work": "👩‍💼 Olga",
        "play": "🗨️ Olga",
        "shared": "🧵 Olga"
    }

    prefix = mode_prefixes.get(mode, "Olga")
    formatted = f"\n{prefix}: {text}\n"
    return formatted


def print_divider():
    print("\n" + "-" * 60 + "\n")


def pretty_print(text: str, mode: str):
    print_divider()
    print(format_response(text, mode))
    print_divider()
