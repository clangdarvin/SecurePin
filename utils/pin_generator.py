import secrets


def generate_pin(n_digits: int) -> str:
    """Generates a 4-digit or 6-digit PIN using the secrets library.

    Args:
        n_digits: an integer that determines whether it's a 4-digit or 6-digit PIN.

    Returns:
        The n-digit PIN based on the user preference.
    """
    if n_digits not in [4, 6]:
        raise ValueError("The argument must be 4 or 6.")

    return "".join(str(secrets.randbelow(10)) for _ in range(n_digits))
