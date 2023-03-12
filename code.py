class Solution:    
    def findItinerary(self, tickets):
        
        path, d = [], defaultdict(list)
        for a,b in tickets: insort(d[a], b)      # build the graph; insort to return lex-smallest route
        
        def dfs(loc):                            # check for a path including each flight
            while d[loc]: dfs(d[loc].pop(0))     # pop off the flight
            path.append(loc)
            
        dfs("JFK")
        return path[::-1]                        # Reverse the path after recursion
 
