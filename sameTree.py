"""
Given the roots of two binary trees: p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""

class Solution:
  """
  This function takes in the roots of the two binary trees: p and q and if identical true, if not false
  Checks 3 cases:
  1. If both trees are empty, they are the same.
  2. If one tree is empty, but the other isn't, they're not the same
  3. If the values at the current nodes are different, then the trees are not the same.
  If none of these cases apply, the function recursively checks if the left and right subtrees are the same, 
  if both subtrees are the same, then the whole tree is the same.
  """
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q: #both trees are empty so they are the same
      return True
    elif not p or not q: #one tree is empty, not the two, so they're not the same
      return False
    elif p.val != q.val: #values mismatch at the current nodes so they're not the same
      return False
    else: #recurisvely checks if the left and right subtrees are the same 
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
           
                 
