def averageOfLevels(self, root):
        result = []
        count = []

        def getLevelSum(node, level):
            if not node:
                return
            if len(result) <= level:
                result.append(node.data)
                count.append(1)
            else:
                result[level] += node.data
                count[level] += 1
            if node.leftChild:
                getLevelSum(node.leftChild, level+1)
            if node.rightChild:
                getLevelSum(node.rightChild, level+1)
        getLevelSum(root, 0)
        average = []
        for i in range(0, len(result)):
            av = float(float(result[i])/float(count[i]))
            average.append(av)
        return average
    