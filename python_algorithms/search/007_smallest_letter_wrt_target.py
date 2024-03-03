"""
**Challenge:**
Given a **sorted list of lowercase letters** and a specific **target letter**, 
your task is to find the **smallest letter** in the list that is
**lexicographically larger** than the target.

**Key Points:**
* The input list (`letters`) contains **unique** lowercase letters in **ascending 
alphabetical order**.
* The target letter (`target`) is also a lowercase letter.
* You need to find the **first letter** in the list that comes **after** the target 
in the alphabet, considering **wraparound**.
* If the target letter is the **last letter** in the list (i.e., 'z'), the smallest 
larger letter will be the **first letter** (i.e., 'a').

**Examples:**
* **Input:** `letters = ["c", "f", "j"]`, `target = "a"`
* **Output:** `"c"` (Explanation: "c" is the smallest letter in the list that comes after "a")
* **Input:** `letters = ["c", "f", "j"]`, `target = "d"`
* **Output:** `"f"` (Explanation: "f" is the smallest letter in the list that comes after "d")
* **Input:** `letters = ["c", "f", "j"]`, `target = "z"`
* **Output:** `"a"` (Explanation: Wraparound case - "a" is the smallest letter after "z")
"""


def next_gretest_letter(arr: list[str], target: str) -> str:
    left, right = 0, len(arr)

    while left < right:
        middle = (left + right) // 2
        if ord(arr[middle]) < ord(target):
            left = middle + 1
        else:
            right = middle

    return arr[left % len(arr)]


if __name__ == "__main__":
    assert next_gretest_letter(["c", "f", "j"], "a") == "c"
    assert next_gretest_letter(["c", "f", "j"], "d") == "f"
    assert next_gretest_letter(["c", "f", "j"], "z") == "c"
