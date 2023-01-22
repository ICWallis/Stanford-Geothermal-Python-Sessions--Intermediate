import numpy as np


def interpolate_survey(x_target, x_source, y_source):
    '''
    1D linear interpolation of monotonically increasing data, such as well survey data.

    Given two lists or 1D arrays of related values (x_source, y_source), linearly interpolate
    y values from  a list of x values (x_target). For example, x may be well measured depth and y may be
    vertical depth. The method expects 1D arrays or lists, so .values must be called on 
    Pandas dataframe columns. x_source and y_source must be the same length and must be monotonically increasing.
    Results are rounded to 2 decimal places.

    Args:   
                x_target: (list/1D np.array) interpolation target values
                x_source: (list/1D np.array) known x value that maps to the known y value
                y_source: (list/1D np.array) known y value that that 
    
    Returns:    1D array of y values that map to x_target and are linearly interpolated from x_source and y_source
    '''
    # Rasing input data errors
    if (not np.all(np.diff(x_target) > 0)):
        raise ValueError(
            'x_target (first positional arg) must be in increasing order and not contain NaN'
            )

    if (not np.all(np.diff(x_source) > 0)):
        raise ValueError(
            'x_source (second positional arg) must be in increasing order and not contain NaN'
            )

    if (not np.all(np.diff(y_source) > 0)):
        raise ValueError(
            'y_source (third positional arg) must be in increasing order and not contain NaN'
            )
    
    # Generating the interpolated value
    y_target = np.around(np.interp(x_target, x_source, y_source),2)

    return y_target