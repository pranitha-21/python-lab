import numpy as np

def format_strings(arr):
    
    arr = arr.astype(str)

    center_aligned = np.char.center(arr, 15, fillchar='_')
    left_justified = np.char.ljust(arr, 15, fillchar='_')
    right_justified = np.char.rjust(arr, 15, fillchar='_')

    return center_aligned, left_justified, right_justified


arr = np.array(['apple', 'banana', 'kiwi', 'pineapple', 'fig'])

centered, left, right = format_strings(arr)

print("Original:\n", arr)
print("\nCenter Aligned:\n", centered)
print("\nLeft Justified:\n", left)
print("\nRight Justified:\n", right)
