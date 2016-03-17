import copy,collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def bt(l,tickets,dep):
        	if not tickets:
        		return l
        	cand=[_ for _ in tickets if _[0]==dep]
        	cand.sort(key=lambda l:l[1])
        	for arr in cand:
        		tmp=copy.deepcopy(tickets)
        		tmp.remove(arr)
        		a=bt(l+[arr[1]],tmp,arr[1])
        		if a!=None:
        			return a
        return bt(['JFK'],tickets,'JFK')


    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def bt(l,dep,used):
        	if	len(used)==len(tickets):
        		return l
        	cand=[(_,i) for i,_ in enumerate(tickets) if _[0]==dep and i not in used]
        	cand.sort(key=lambda l:l[0][1])
        	for arr in cand:
        		a=bt(l+[arr[0][1]],arr[0][1],used+[arr[1]])
        		if a!=None:
        			return a
        return bt(['JFK'],'JFK',[])

    def findItinerary3(self, tickets):
		targets = collections.defaultdict(list)
		for a, b in sorted(tickets)[::-1]:
		    targets[a] += b,
		print targets
		route = []
		def visit(airport):
		    while targets[airport]:
		        visit(targets[airport].pop())
		    route.append(airport)
		visit('JFK')
		return route[::-1]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets=[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

sl=Solution()
print sl.findItinerary(tickets)
print '-'*80
print sl.findItinerary2(tickets)
print '-'*80
print sl.findItinerary3(tickets)
