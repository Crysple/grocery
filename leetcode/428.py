"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        self.data = ""
        def serialize(root):
            if not root:
                #self.data += '#'
                return
            self.data += str(root.val)
            if root.children:
                self.data += '['
                [serialize(child) for child in root.children]
                self.data = self.data[:-1] + ']' # replace last ',' as ']'
            self.data += ','
        serialize(root)
        #print(self.data[:-1])
        return self.data[:-1]
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        
        BNF:
        expr ::= node {, node  }
        node ::= digit['[' expr ']']
        """
        if not data:
            return None
        data = [*filter(lambda x:x, re.split("([\[\],])", data) + ["$"])]
        self.idx = 0
        def lookahead():
            return data[self.idx]

        def get_token():
            self.idx += 1
            return data[self.idx-1]
        
        def node():
            root = Node(int(get_token()), [])
            if lookahead() == '[':
                get_token()
                root.children = expr()
                get_token()
            return root

        def expr():
            res = [node()]
            while lookahead() == ",":
                get_token() # ,
                res.append(node())
            return res

        return expr()[0]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
