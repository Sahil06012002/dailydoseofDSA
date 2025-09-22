
class Node:
    def __init__(self, val):
        self.right = None
        self.val = val
        self.left = None

class Solution:
    def boundaryTraversal(self, root):
        result = []
        # Code here
        def traverse_left(temp) :
            if temp.left == None:
                result.append(temp.val)
                return
            result.append(temp.val)
            traverse_left(temp.left)
            

        def collect_leaf(temp) :
            if temp == None :
                return 
            
            if temp.left == None and temp.right == None :
                result.append(temp.val)

            collect_leaf(temp.left)
            collect_leaf(temp.right)
            
        # append right in reverse order 
        def traverse_right(temp) :
            if temp.right == None :
                result.append(temp.val)
                return
            traverse_right(temp.right)
            result.append(temp.val)
            
        temp = root
        

        traverse_left(temp)
        temp = root
        collect_leaf(temp)
        
        temp = root
        
        if temp.right :
            traverse_right(temp.right)

        return result
            
root = Node(1)
root.right = Node(2)
root.right.left = Node(3)
root.right.right = Node(4)

sol = Solution()
print(sol.boundaryTraversal(root))
  
        
class Test :
    def determineLocation(locations, redirectRecords):
        n = len(locations)
        visited = set()
        
        # Start at first server
        curr_x, curr_y = locations[0]
        visited.add((curr_x, curr_y))
        
        for direction in redirectRecords:
            candidates = []
            
            for x, y in locations:
                if (x, y) in visited:
                    continue
                
                if direction == 1 and x > curr_x and y > curr_y:
                    candidates.append((x, y))
                elif direction == 2 and x > curr_x and y < curr_y:
                    candidates.append((x, y))
                elif direction == 3 and x < curr_x and y > curr_y:
                    candidates.append((x, y))
                elif direction == 4 and x < curr_x and y < curr_y:
                    candidates.append((x, y))
            
            if not candidates:
                continue  
            
            best = min(candidates, key=lambda p: (p[0]-curr_x)**2 + (p[1]-curr_y)**2)
            
            curr_x, curr_y = best
            visited.add(best)
        
        return [curr_x, curr_y]
