from datetime import datetime


def get_deadline_status(deadline):
    """
    Calculate scholarship deadline status.
    """

    try:
        deadline_date = datetime.strptime(
            deadline,
            "%d-%m-%Y"
        )

        days_left = (
            deadline_date - datetime.today()
        ).days

        if days_left < 0:
            return "Expired"

        elif days_left <= 30:
            return "Due Soon"

        else:
            return "Active"

    except (ValueError, TypeError):
        return "Date Unavailable"