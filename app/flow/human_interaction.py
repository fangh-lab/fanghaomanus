"""Human interaction utilities for flow execution."""


def ask_human_confirmation(prompt: str, default: str = "y") -> bool:
    """
    Ask human for confirmation.

    Args:
        prompt: The question to ask
        default: Default answer if user just presses Enter ('y' or 'n')

    Returns:
        True if confirmed, False otherwise
    """
    import sys
    # Force flush output before asking for input
    sys.stdout.flush()
    sys.stderr.flush()

    valid_inputs = {"y": True, "yes": True, "n": False, "no": False, "": default.lower() == "y"}

    while True:
        try:
            user_input = input(f"{prompt} (y/n, default={default}): ").strip().lower()
            sys.stdout.flush()  # Flush after input
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Using default value.")
            return default.lower() == "y"

        if user_input in valid_inputs:
            return valid_inputs[user_input]
        elif user_input == "":
            return default.lower() == "y"
        else:
            print("Please enter 'y' or 'n' (or press Enter for default)")
            sys.stdout.flush()


def ask_human_feedback(prompt: str, allow_empty: bool = True) -> str:
    """
    Ask human for feedback or input.

    Args:
        prompt: The question or prompt to display
        allow_empty: Whether to allow empty input

    Returns:
        User's input string
    """
    import sys
    # Force flush output before asking for input
    sys.stdout.flush()
    sys.stderr.flush()

    while True:
        try:
            user_input = input(f"{prompt}: ").strip()
            sys.stdout.flush()  # Flush after input
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted.")
            return "" if allow_empty else ""

        if user_input or allow_empty:
            return user_input
        else:
            print("Please provide feedback (or press Enter if empty feedback is allowed)")
            sys.stdout.flush()


def display_text_with_pagination(text: str, page_size: int = 20):
    """
    Display text with pagination support.

    Args:
        text: Text to display
        page_size: Number of lines per page
    """
    lines = text.split("\n")
    total_lines = len(lines)

    if total_lines <= page_size:
        print(text)
        return

    current = 0
    while current < total_lines:
        end = min(current + page_size, total_lines)
        print("\n".join(lines[current:end]))

        if end < total_lines:
            user_input = input(f"\n--- Showing {end}/{total_lines} lines. Press Enter for more, 'q' to quit: ").strip().lower()
            if user_input == "q":
                break
        current = end
