# P1

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        return len(s1[-1])
```

# P2
```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(str(i) for i in digits)
        s = int(s) + 1
        return list(int(i) for i in str(s))
```
