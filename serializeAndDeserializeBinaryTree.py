# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
The serialization and deserialization of a binary tree involves converting the tree into a string format that can be stored or transmitted and then reconstructing the tree from the string format. The algorithm for serialization could involve traversing the tree using a pre-order traversal, where each node is added to a string with a delimiter to separate the nodes. For deserialization, the string can be split using the same delimiter and recursively reconstruct the binary tree from the string by creating nodes for each substring in the pre-order traversal order.
"""
class Codec:

    def serialize(self, root):
        #first checks if the current node is null and adds None to the serialized string if it is
        #if the node is not null, it adds the nodes value followed by the serialized format of its left and right children
        #Encodes a tree to a single string.

        if not root:
            return "None," #indicate null node with "None"

        serialized = str(root.val) + ","
        serialized += self.serialize(root.left)
        serialized += self.serialize(root.right)

        return serialized

    def deserialize(self, data):
        #this method takes the serialized string and recursively buidls the binary tree by first creating the root node
        #and then recursively creating its left and right children using the remaining elements in the list.
        #the method removes the processed elements from the list as it constructs the tree
        #decodes your encoded data to tree.

        def build_tree(vals):
            if vals[0] == "None":
                vals.pop(0) #remove null node if so
                return None

            # if not None, then create the node and remove the processed val
            root = TreeNode(int(vals[0])) #create node
            vals.pop(0)    #remove the processed val

            root.left = build_tree(vals)
            root.right = build_tree(vals)

            return root

        data_list = data.split(",")
        root = build_tree(data_list)

        return root



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
