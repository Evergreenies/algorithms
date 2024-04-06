"""
The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their prospective 
opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

```
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
```

Write an algorithm that pairs the men and women together in such a way that no 
two people of opposite sex would both rather be with each other than with their 
current partners.
"""


def stable_marriage(
    men_preferences: dict[str, list], women_preferences: dict[str, list]
) -> dict[str, str]:
    men = list(set(men_preferences.keys()))
    matches = {}

    while men:
        for man in men:
            for woman in men_preferences[man]:
                if woman not in matches:
                    matches[man] = woman
                    men.remove(man)
                    break
                else:
                    current_partner = matches[woman]
                    if women_preferences[woman].index(man) < women_preferences[
                        woman
                    ].index(current_partner):
                        matches[man] = woman
                        men.remove(man)
                        men.append(current_partner)
                        break

    return matches


if __name__ == "__main__":
    guy_preferences = {
        "andrew": ["caroline", "abigail", "betty"],
        "bill": ["caroline", "betty", "abigail"],
        "chester": ["betty", "caroline", "abigail"],
    }

    gal_preferences = {
        "abigail": ["andrew", "bill", "chester"],
        "betty": ["bill", "andrew", "chester"],
        "caroline": ["bill", "chester", "andrew"],
    }

    final_matches = stable_marriage(guy_preferences, gal_preferences)
    print(final_matches)

    assert len(final_matches) == 3
