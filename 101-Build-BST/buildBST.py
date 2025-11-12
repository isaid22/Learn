# build_bst_visual.py
# -----------------------------------
# Build a Binary Search Tree (BST) from a list of numbers
# and print both its inorder traversal and visual layout.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    """Insert a value into the BST recursively."""
    if root is None:
        print(f"Creating new node with value {val}")
        return TreeNode(val)

    if val < root.val:
        print(f"{val} < {root.val}: go LEFT")
        root.left = insert(root.left, val)
    else:
        print(f"{val} >= {root.val}: go RIGHT")
        root.right = insert(root.right, val)

    return root


def build_bst(nums):
    """Build a BST from a list of numbers."""
    root = None
    for num in nums:
        print(f"\nInserting {num} into the BST...")
        root = insert(root, num)
    return root


def inorder(root):
    """Inorder traversal (sorted order)."""
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def print_tree(root, level=0, prefix="Root: "):
    """Recursively print the tree sideways."""
    if root is not None:
        print_tree(root.right, level + 1, prefix="R── ")
        print("    " * level + prefix + str(root.val))
        print_tree(root.left, level + 1, prefix="L── ")


def main():
    # Example list (unsorted is fine)
    nums = [8, 3, 10, 1, 6, 14, 4, 7, 13]

    print("Building BST from list:", nums)
    root = build_bst(nums)

    print("\n\nInorder traversal (should be sorted):")
    inorder(root)
    print("\n")

    print("Visual representation of BST:")
    print_tree(root)


if __name__ == "__main__":
    main()
