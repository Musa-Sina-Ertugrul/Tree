class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def remove_child(self, name):
        if len(self.children) == 0:
            return False
        for child in self.children:
            if child.data is not name:
                child.remove_child(name)
            else:
                self.children.remove(child)
                return True

    def get_level(self):
        level = 0
        parent = self.parent
        while parent != None:
            level += 1
            parent = parent.parent
        return level

    def print(self):
        print(" " * self.get_level() * 3 + "|__" + self.data)
        if self.children:
            for child in self.children:

                child.print()


root = TreeNode("Electronics")

laptop = TreeNode("Laptop")
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("ThinkPad"))

cellphone = TreeNode("Cellphone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))

tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))

root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)

root.print()
root.remove_child("TV")
print()
root.print()

