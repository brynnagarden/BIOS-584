from self_py_fun.Quiz3Fun import *

# You can use this .py script to perform debugging task.
sample_arr_1 = np.array([1,2,3,4,5])
d_1 = compute_D_partial(sample_arr_1)
# The correct d_1 should be 5.66.

# your solution to 1.
def compute_D_partial_for_task_1_only(input_signal):
    r"""
    :param input_signal:
    """
    T_len = len(input_signal)
    signal_diff_one = input_signal[-1] - input_signal[1:]
    D_val = np.sum(np.sqrt(1+signal_diff_one**2)) / (T_len - 1)
    return D_val