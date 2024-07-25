# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1, leaf2 = [], []

        def get_leaves(root, leaf):
            if not root:
                return
            if root.left: #왼쪽에 자식노드 있으면
                get_leaves(root.left, leaf)
            if root.right:
                get_leaves(root.right, leaf)
            if not root.left and not root.right: #자식 없는 경우
                leaf.append(root.val) #현재 노드 값 리스트에 추가

        get_leaves(root1, leaf1)
        get_leaves(root2, leaf2)

        return True if leaf1 == leaf2 else False