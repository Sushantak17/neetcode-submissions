class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        for c in lst:
            if c == "..":
                if stack:
                    stack.pop()
            elif c != "" and c!= ".":
                stack.append(c)

        return "/" + "/".join(stack)
        