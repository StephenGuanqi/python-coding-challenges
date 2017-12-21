class BSTNode(object):

    def __init__(self, parent, k):
        """
        Creates a node
        :param parent: The node's parent
        :param k: The key of the node
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """
        Finds and returns the node with key k from the subtree rooted at this node.
        :param k:
        :return:
        """
        if k == self.key:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        """
        Finds the node with the minimum key in the subtree rooted at this node
        :return: the node with the minimum key
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def next_larger(self):
        """
        Returns the node with the next larger key (the successor) in the BST
        """
        if self.right is not None:
            return self.right.findmin()
        current = self
        while current.parent is not None and current is not current.parent.left:
            current = current.parent
        return current.parent

    def insert(self, node):
        """
        inserts a node into the subtree rooted at this node
        :param nod: node to be inserted
        """
        if node is None:
            return
        if node.key < self.key:
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        """
        Delete and return this node from the BST
        :return:
        """
        # deleted node is leaf node or has only one child
        if self.left is None or self.right is None:
            if self is self.parent.left:
                # update parent's child node
                self.parent.left = self.left or self.right
                # update new child node's parent node
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.perent.right.parent = self.parent
            return self
        else:
        # deleted node has left and right subtree
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()

class BST(object):
    def __init__(self):
        self.root = None

    def find(self, key):
        return self.root and self.root.find(key)

    def find_min(self):
        return self.root and self.root.find_min()

    def insert(self, k):
        node = BSTNode(None, k)
        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

    def delete(self, k):
        """
        Delete and returns a node with key k if it exists from the BST
        :param k:
        """
        node = self.root.find(k)
        if node is None:
            return None
        return node.delete()

    def __str__(self):
        if self.root is None: return '<empty tree>'

        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                            node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])


