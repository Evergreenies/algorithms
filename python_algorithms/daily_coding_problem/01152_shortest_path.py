"""
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
"""


def simplify_path(path: str) -> str:
    components = path.split("/")
    stack = []

    for component in components:
        if component == "" or component == ".":
            continue

        elif component == "..":
            if stack:
                stack.pop()
        else:
            stack.append(component)

    return "/" + "/".join(stack)


print(simplify_path("/usr/bin/../bin/./scripts/../"))  # Output: "/usr/bin/"
print(simplify_path("/a/./b/../../c/"))  # Output: "/c"
print(simplify_path("/../"))  # Output: "/"
print(simplify_path("/home//foo/"))  # Output: "/home/foo"
print(simplify_path("/home/"))  # Output: "/home"
