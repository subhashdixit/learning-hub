# 40 Python programming problems with worked solutions

[Python home](../../README.md) · [Theory](../../01-theory/README.md)

16 easy,16 medium and 8 hard problems. Read the contract, solve it yourself, then expand the solution. Each solution is also an executable file with assertions; run `python3 run_all.py` to check all 40 in isolated processes. Python 3.10+ standard library only. Complexity statements use the usual unit-cost model unless noted.

## 01. Safe average — Easy

Return the average of a nonempty numeric sequence; raise ValueError for empty input.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):
    if not xs:raise ValueError('empty')
    return sum(xs)/len(xs)
assert solve([2,4])==3
try:solve([])
except ValueError:pass
else:raise AssertionError('empty accepted')
```

One pass to sum: O(n) time and O(1) extra space for an existing sequence.

[Executable file](01-safe-average.py)

</details>

## 02. Count vowels — Easy

Count ASCII vowels in a string, ignoring case.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):return sum(c.lower() in 'aeiou' for c in text)
assert solve('Python AI')==3 and solve('')==0
```

Define the alphabet explicitly; Unicode language rules require a different contract. O(n) time.

[Executable file](02-count-vowels.py)

</details>

## 03. Palindrome normalization — Easy

Ignore nonalphanumeric characters and case; determine whether the resulting string is a palindrome.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):
    cleaned=''.join(c.casefold() for c in text if c.isalnum())
    return cleaned==cleaned[::-1]
assert solve('A man, a plan, a canal: Panama')
assert solve('') and not solve('python')
```

A normalized copy is clear: O(n) time and space. Normalization conventions are part of the task.

[Executable file](03-palindrome-normalization.py)

</details>

## 04. Stable unique values — Easy

Remove repeated hashable values while keeping the first-occurrence order.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):return list(dict.fromkeys(xs))
assert solve([3,1,3,2,1])==[3,1,2] and solve([])==[]
```

Dictionary insertion order preserves first occurrence. O(n) average time and O(k) space; unhashable values need another approach.

[Executable file](04-stable-unique-values.py)

</details>

## 05. Frequency map — Easy

Count occurrences of hashable values.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import Counter
def solve(xs):return dict(Counter(xs))
assert solve('banana')=={'b':1,'a':3,'n':2} and solve([])=={}
```

Counts avoid repeated scans; O(n) average time and O(k) space for k distinct values.

[Executable file](05-frequency-map.py)

</details>

## 06. Second distinct largest — Easy

Return the second distinct largest number, or None when absent.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):
    values=sorted(set(xs),reverse=True)
    return values[1] if len(values)>1 else None
assert solve([5,5,3])==3 and solve([5,5]) is None and solve([]) is None
```

Distinctness is explicit. O(n log n) worst-case sorting time and O(n) extra space; a one-pass alternative is possible.

[Executable file](06-second-distinct-largest.py)

</details>

## 07. Merge totals — Easy

Combine two amount dictionaries by summing amounts on shared keys without mutating inputs.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(a,b):
    out=a.copy()
    for key,value in b.items():out[key]=out.get(key,0)+value
    return out
a={'x':2};assert solve(a,{'x':3,'y':1})=={'x':5,'y':1} and a=={'x':2}
```

Copying establishes ownership. O(n+m) average time and output space.

[Executable file](07-merge-totals.py)

</details>

## 08. Flatten one level — Easy

Flatten a sequence of sequences exactly one level.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(rows):return [v for row in rows for v in row]
assert solve([[1,2],[],[3]])==[1,2,3] and solve([])==[]
```

The contract is one level, not arbitrary recursive flattening. O(total elements) time/output space.

[Executable file](08-flatten-one-level.py)

</details>

## 09. Reverse words — Easy

Reverse whitespace-separated word order; normalize whitespace to single spaces.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):return ' '.join(text.split()[::-1])
assert solve('  learn   Python now ')== 'now Python learn'
assert solve('')==''
```

split handles whitespace groups; reversing preserves each word’s characters. O(n) time and space.

[Executable file](09-reverse-words.py)

</details>

## 10. Factorial — Easy

Compute n! for a nonnegative integer, rejecting bool and invalid inputs.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError('nonnegative integer required')
    total=1
    for k in range(2,n+1):total*=k
    return total
assert solve(0)==1 and solve(5)==120
```

The empty product is 1. O(n) multiplications; large-integer bit complexity grows with result size.

[Executable file](10-factorial.py)

</details>

## 11. Prime test — Easy

Determine primality for an integer; values below 2 are not prime.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from math import isqrt
def solve(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))
assert solve(2) and solve(29) and not solve(1) and not solve(25)
```

A composite has a factor no larger than its square root. O(sqrt n) trial divisions.

[Executable file](11-prime-test.py)

</details>

## 12. Group records — Easy

Group order IDs by customer, retaining input order within each group.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import defaultdict
def solve(rows):
    out=defaultdict(list)
    for customer,order in rows:out[customer].append(order)
    return dict(out)
assert solve([('a',1),('b',2),('a',3)])=={'a':[1,3],'b':[2]}
```

One pass with grouped append: O(n) average time and O(n) output space.

[Executable file](12-group-records.py)

</details>

## 13. Transpose rectangular rows — Easy

Transpose a rectangular list of rows; reject unequal row lengths.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(rows):
    if not rows:return []
    if any(len(r)!=len(rows[0]) for r in rows):raise ValueError('ragged')
    return [list(c) for c in zip(*rows)]
assert solve([[1,2],[3,4]])==[[1,3],[2,4]] and solve([])==[]
```

Validate before zip, which would otherwise truncate to the shortest row. O(rows×columns) time/space.

[Executable file](13-transpose-rectangular-rows.py)

</details>

## 14. Run-length encoding — Easy

Return consecutive value/count pairs, preserving runs rather than global counts.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from itertools import groupby
def solve(xs):return [(value,sum(1 for _ in run)) for value,run in groupby(xs)]
assert solve('aaabbca')==[('a',3),('b',2),('c',1),('a',1)]
assert solve('')==[]
```

groupby uses consecutive equality, not all equal values anywhere. O(n) time.

[Executable file](14-run-length-encoding.py)

</details>

## 15. Top-k frequent with ties — Easy

Return up to k values ordered by descending frequency, then ascending value; values must be mutually sortable.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import Counter
def solve(xs,k):
    if k<0:raise ValueError('negative k')
    counts=Counter(xs)
    return sorted(counts,key=lambda x:(-counts[x],x))[:k]
assert solve([2,1,2,1,3],2)==[1,2] and solve([],3)==[]
```

The tie contract is explicit. O(n+u log u) time for u unique values.

[Executable file](15-top-k-frequent-with-ties.py)

</details>

## 16. Chunk a sequence — Easy

Split into chunks of positive size; retain a final short chunk.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,size):
    if size<=0:raise ValueError('positive size')
    return [xs[i:i+size] for i in range(0,len(xs),size)]
assert solve([1,2,3,4,5],2)==[[1,2],[3,4],[5]] and solve([],2)==[]
```

Slicing copies the retained sequence elements; total O(n) work/output size.

[Executable file](16-chunk-a-sequence.py)

</details>

## 17. Two-sum indices — Medium

Return indices of two distinct occurrences adding to target, or None.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,target):
    seen={}
    for i,x in enumerate(xs):
        if target-x in seen:return seen[target-x],i
        seen[x]=i
    return None
assert solve([3,3],6)==(0,1) and solve([1],2) is None
```

Before processing i, the map contains only earlier occurrences. O(n) average time and O(n) space.

[Executable file](17-two-sum-indices.py)

</details>

## 18. Balanced brackets — Medium

Check (),[]and{}nesting; ignore other characters.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):
    pairs={')':'(',']':'[','}':'{'};stack=[]
    for c in text:
        if c in '([{':stack.append(c)
        elif c in pairs:
            if not stack or stack.pop()!=pairs[c]:return False
    return not stack
assert solve('a([])') and not solve('([)]') and not solve('(')
```

The stack holds unmatched open brackets in order. O(n) time and O(n) worst-case space.

[Executable file](18-balanced-brackets.py)

</details>

## 19. Binary search first occurrence — Medium

For sorted numbers, return the first matching index or−1.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,target):
    lo,hi=0,len(xs)
    while lo<hi:
        mid=(lo+hi)//2
        if xs[mid]<target:lo=mid+1
        else:hi=mid
    return lo if lo<len(xs) and xs[lo]==target else -1
assert solve([1,2,2,3],2)==1 and solve([],2)==-1
```

Maintain a half-open candidate interval and find the first value not below target. O(log n) time, O(1) extra space.

[Executable file](19-binary-search-first-occurrence.py)

</details>

## 20. Merge sorted sequences — Medium

Merge two ascending sequences, retaining duplicates.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(a,b):
    i=j=0;out=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:out.append(a[i]);i+=1
        else:out.append(b[j]);j+=1
    return out+a[i:]+b[j:]
assert solve([1,3],[2,3])==[1,2,3,3] and solve([],[1])==[1]
```

Each step consumes the smallest remaining head. O(n+m) time/output space.

[Executable file](20-merge-sorted-sequences.py)

</details>

## 21. Maximum fixed-window sum — Medium

Return largest sum of k consecutive values; require 1≤k≤n.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,k):
    if not 1<=k<=len(xs):raise ValueError('invalid window')
    current=sum(xs[:k]);best=current
    for i in range(k,len(xs)):
        current+=xs[i]-xs[i-k];best=max(best,current)
    return best
assert solve([2,-1,3,4,-2],2)==7 and solve([-5,-2],1)==-2
```

Update by adding entering and subtracting leaving values; fixed windows work with negatives. O(n) time,O(1) extra space apart from the initial slice.

[Executable file](21-maximum-fixed-window-sum.py)

</details>

## 22. Prefix range sums — Medium

Build prefix sums and answer an inclusive-left/exclusive-right range.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,left,right):
    if not 0<=left<=right<=len(xs):raise ValueError('range')
    prefix=[0]
    for x in xs:prefix.append(prefix[-1]+x)
    return prefix[right]-prefix[left]
assert solve([2,3,4],1,3)==7 and solve([],0,0)==0
```

Preprocessing O(n), then each range query O(1) if the prefix array is reused. This wrapper rebuilds it per call.

[Executable file](22-prefix-range-sums.py)

</details>

## 23. Longest unique substring length — Medium

Find maximum length with no repeated characters.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):
    last={};left=best=0
    for right,c in enumerate(text):
        left=max(left,last.get(c,-1)+1)
        last[c]=right;best=max(best,right-left+1)
    return best
assert solve('abba')==2 and solve('abcabcbb')==3 and solve('')==0
```

Left never moves backward; last occurrence maintains uniqueness. O(n) average time and alphabet-dependent space.

[Executable file](23-longest-unique-substring-length.py)

</details>

## 24. Group anagrams — Medium

Group lowercase-word anagrams, keeping first group appearance order.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(words):
    groups={}
    for word in words:groups.setdefault(''.join(sorted(word)),[]).append(word)
    return list(groups.values())
assert solve(['eat','tea','tan','ate'])==[['eat','tea','ate'],['tan']]
```

Sorted characters are a canonical key under this text contract. O(sum L log L) time.

[Executable file](24-group-anagrams.py)

</details>

## 25. Merge closed intervals — Medium

Merge overlapping or touching intervals after sorting by start.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(intervals):
    out=[]
    for start,end in sorted(intervals):
        if start>end:raise ValueError('reversed interval')
        if out and start<=out[-1][1]:out[-1][1]=max(out[-1][1],end)
        else:out.append([start,end])
    return out
assert solve([[1,3],[2,6],[8,9]])==[[1,6],[8,9]] and solve([])==[]
```

The last output interval covers all merged candidates so far. O(n log n) time, output O(n).

[Executable file](25-merge-closed-intervals.py)

</details>

## 26. Rotate a sequence — Medium

Rotate right by k, accepting negative k as left rotation.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs,k):
    if not xs:return []
    k%=len(xs)
    return list(xs[-k:]+xs[:-k]) if k else list(xs)
assert solve([1,2,3],1)==[3,1,2] and solve([1,2,3],-1)==[2,3,1] and solve([],2)==[]
```

Normalize k modulo length and handle empty input before division. O(n) time/space.

[Executable file](26-rotate-a-sequence.py)

</details>

## 27. Product except self — Medium

Return product of all other values for each index without division.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):
    out=[1]*len(xs);prefix=1
    for i,x in enumerate(xs):out[i]=prefix;prefix*=x
    suffix=1
    for i in range(len(xs)-1,-1,-1):out[i]*=suffix;suffix*=xs[i]
    return out
assert solve([1,2,3,4])==[24,12,8,6] and solve([0,2,3])==[6,0,0]
```

Combine exclusive prefix and suffix products; zeros are handled naturally. O(n) time and O(1) extra beyond output.

[Executable file](27-product-except-self.py)

</details>

## 28. Maximum subarray — Medium

Return largest sum of a nonempty contiguous subarray.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):
    if not xs:raise ValueError('empty')
    current=best=xs[0]
    for x in xs[1:]:current=max(x,current+x);best=max(best,current)
    return best
assert solve([-2,1,-3,4,-1,2,1,-5,4])==6 and solve([-3,-1])==-1
```

The best subarray ending here either starts here or extends the previous best ending. O(n) time.

[Executable file](28-maximum-subarray.py)

</details>

## 29. Stable record deduplication — Medium

Keep the last record by ID while preserving first-ID appearance order.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(rows):
    out={}
    for row in rows:out[row['id']]=row.copy()
    return list(out.values())
assert solve([{'id':'a','v':1},{'id':'b','v':2},{'id':'a','v':3}])==[{'id':'a','v':3},{'id':'b','v':2}]
```

Replacement retains dictionary insertion position. State why last-input wins is appropriate before using it on event histories.

[Executable file](29-stable-record-deduplication.py)

</details>

## 30. Memoized Fibonacci — Medium

Return F(n), with F(0)=0,F(1)=1,for a nonnegative integer.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from functools import lru_cache
@lru_cache(None)
def solve(n):
    if n<0:raise ValueError('negative')
    return n if n<2 else solve(n-1)+solve(n-2)
assert solve(0)==0 and solve(10)==55
```

Memoization avoids repeated subproblems: O(n) additions and O(n) cache/recursion depth; very large n needs an iterative strategy.

[Executable file](30-memoized-fibonacci.py)

</details>

## 31. Next greater values — Medium

For each number, return the next strictly greater value to its right, or None.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(xs):
    out=[None]*len(xs);stack=[]
    for i,x in enumerate(xs):
        while stack and xs[stack[-1]]<x:out[stack.pop()]=x
        stack.append(i)
    return out
assert solve([2,1,2,4,3])==[4,2,4,None,None] and solve([])==[]
```

A monotonic stack retains indices awaiting a greater value. Each index is pushed/popped once: O(n) time and space.

[Executable file](31-next-greater-values.py)

</details>

## 32. Postfix expression evaluation — Medium

Evaluate whitespace-separated integer operands and +,-,*operations; reject malformed stack structure.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(text):
    stack=[]
    for token in text.split():
        if token in {'+','-','*'}:
            if len(stack)<2:raise ValueError('missing operand')
            b=stack.pop();a=stack.pop();stack.append(a+b if token=='+' else a-b if token=='-' else a*b)
        else:stack.append(int(token))
    if len(stack)!=1:raise ValueError('malformed expression')
    return stack[0]
assert solve('2 3 + 4 *')==20 and solve('5 2 -')==3
```

Pop the right operand before the left for noncommutative subtraction. O(tokens) time and stack space.

[Executable file](32-postfix-expression-evaluation.py)

</details>

## 33. Breadth-first shortest path — Hard

Return shortest unweighted path between vertices, or None.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import deque
def solve(graph,start,end):
    q=deque([start]);parent={start:None}
    while q:
        node=q.popleft()
        if node==end:
            path=[]
            while node is not None:path.append(node);node=parent[node]
            return path[::-1]
        for nxt in graph.get(node,[]):
            if nxt not in parent:parent[nxt]=node;q.append(nxt)
    return None
assert solve({'a':['b','c'],'b':['d'],'c':['d']},'a','d')==['a','b','d']
assert solve({},'a','z') is None
```

BFS visits increasing edge distance in an unweighted graph. O(V+E) time and O(V) space for reached vertices.

[Executable file](33-breadth-first-shortest-path.py)

</details>

## 34. Topological order with cycle detection — Hard

Return a topological ordering of a directed graph containing all supplied vertices; raise on cycles.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import deque
def solve(graph):
    nodes=set(graph)|{v for values in graph.values() for v in values};degree={v:0 for v in nodes}
    for values in graph.values():
        for v in values:degree[v]+=1
    q=deque(sorted(v for v in nodes if degree[v]==0));out=[]
    while q:
        u=q.popleft();out.append(u)
        for v in graph.get(u,[]):
            degree[v]-=1
            if degree[v]==0:q.append(v)
    if len(out)!=len(nodes):raise ValueError('cycle')
    return out
assert solve({'a':['b'],'b':['c']})==['a','b','c']
try:solve({'a':['b'],'b':['a']})
except ValueError:pass
else:raise AssertionError('cycle missed')
```

Repeatedly remove zero-indegree vertices. O(V+E), plus initial sorting for deterministic starting order.

[Executable file](34-topological-order-with-cycle-detection.py)

</details>

## 35. Coin-change minimum — Hard

For positive integer denominations, find minimum coins for a nonnegative amount, or−1.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(coins,amount):
    if amount<0 or any(c<=0 for c in coins):raise ValueError('domain')
    dp=[0]+[amount+1]*amount
    for total in range(1,amount+1):
        for coin in coins:
            if coin<=total:dp[total]=min(dp[total],1+dp[total-coin])
    return dp[amount] if dp[amount]<=amount else -1
assert solve([1,3,4],6)==2 and solve([2],3)==-1 and solve([],0)==0
```

Dynamic programming, not greedy, handles denomination sets where the largest coin first is wrong. O(amount×coins) time.

[Executable file](35-coin-change-minimum.py)

</details>

## 36. Longest increasing subsequence length — Hard

Return length of a strictly increasing subsequence.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from bisect import bisect_left
def solve(xs):
    tails=[]
    for x in xs:
        i=bisect_left(tails,x)
        if i==len(tails):tails.append(x)
        else:tails[i]=x
    return len(tails)
assert solve([10,9,2,5,3,7,101,18])==4 and solve([2,2])==1 and solve([])==0
```

tails[k]tracks a small possible endpoint for a length-k+1 subsequence; tails itself need not be the final subsequence. O(n log n) time.

[Executable file](36-longest-increasing-subsequence-length.py)

</details>

## 37. Edit distance — Hard

Compute insertion/deletion/substitution distance between two strings, each cost 1.

<details>
<summary>Solution, checks and reasoning</summary>

```python
def solve(a,b):
    previous=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        current=[i]
        for j,y in enumerate(b,1):current.append(min(current[-1]+1,previous[j]+1,previous[j-1]+(x!=y)))
        previous=current
    return previous[-1]
assert solve('kitten','sitting')==3 and solve('','abc')==3
```

Each state compares prefixes; retain only the prior row. O(mn) time and O(n) space in this orientation.

[Executable file](37-edit-distance.py)

</details>

## 38. LRU cache behaviour — Hard

Implement get/put with capacity 2 or another positive capacity; get returns None for a missing key.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import OrderedDict
class Cache:
    def __init__(self,capacity):
        if capacity<=0:raise ValueError('capacity')
        self.capacity=capacity;self.data=OrderedDict()
    def get(self,key):
        if key not in self.data:return None
        self.data.move_to_end(key);return self.data[key]
    def put(self,key,value):
        self.data[key]=value;self.data.move_to_end(key)
        if len(self.data)>self.capacity:self.data.popitem(last=False)
c=Cache(2);c.put('a',1);c.put('b',2);assert c.get('a')==1;c.put('c',3)
assert c.get('b') is None and c.get('c')==3
```

Access moves an item to most-recent position; evict the least-recent. O(1) average operations, capacity-bounded storage. None as miss is ambiguous if cached values can be None.

[Executable file](38-lru-cache-behaviour.py)

</details>

## 39. Count subarrays with sum k — Hard

Count contiguous subarrays whose sum equals k, including negative inputs.

<details>
<summary>Solution, checks and reasoning</summary>

```python
from collections import defaultdict
def solve(xs,k):
    counts=defaultdict(int,{0:1});prefix=answer=0
    for x in xs:
        prefix+=x;answer+=counts[prefix-k];counts[prefix]+=1
    return answer
assert solve([1,1,1],2)==2 and solve([1,-1,0],0)==3 and solve([],0)==0
```

A prior prefix equal to current−kmarks a qualifying subarray. Query before inserting current prefix avoids counting an empty subarray. O(n) average time/space.

[Executable file](39-count-subarrays-with-sum-k.py)

</details>

## 40. Streaming median — Hard

Return the median after each prefix of a numeric stream.

<details>
<summary>Solution, checks and reasoning</summary>

```python
import heapq
def solve(xs):
    low=[];high=[];out=[]
    for x in xs:
        heapq.heappush(low,-x);heapq.heappush(high,-heapq.heappop(low))
        if len(high)>len(low):heapq.heappush(low,-heapq.heappop(high))
        out.append(-low[0] if len(low)>len(high) else (-low[0]+high[0])/2)
    return out
assert solve([5,1,3,2])==[5,3,3,2.5] and solve([])==[]
```

Maintain lower/upper heaps with ordered partition and balanced sizes. O(log n) per item, O(n) retained stream values.

[Executable file](40-streaming-median.py)

</details>
