# Functions

def calc_APW(nc: float, enh: float, delayed: float) -> float:
    """
    Calculate APW (Absolute Percentage Washout)

    Parameters:
        nc (float): Non-contrast HU
        enh (float): Enhanced HU
        delayed (float): Delayed HU

    Returns: APW (float)
    """
    APW = (enh - delayed) / (enh - nc)
    return APW


def calc_RPW(enh: float, delayed: float) -> float:
    """
    Calculate RPW (Relative Percentage Washout)

    Parameters:
        enh (float): Enhanced HU
        delayed (float): Delayed HU

    Return: RPW (float)
    """
    RPW = (enh - delayed) / enh
    return RPW