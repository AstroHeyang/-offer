def is_sequence_BST(sequence):
    if not sequence:
        return False
    return isSequenceOfBST(sequence)


def isSequenceOfBST(sequence):
    if not sequence:
        return True
    root = sequence[-1]
    left, right = [], []
    i = 0
    while i < len(sequence) - 1 and sequence[i] < root:
        left.append(sequence[i])
        i += 1
    j = i
    while j < len(sequence) - 1:
        if sequence[j] < root:
            return False
        else:
            right.append(sequence[j])
        j += 1
    return isSequenceOfBST(left) and isSequenceOfBST(right)