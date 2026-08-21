"""Print the only lists that matter."""

MUST = [
    "one user story",
    "compose up",
    "auth",
    "eval number",
    "deployed URL",
    "threat model",
    "5-min demo script",
]
WONT = [
    "mobile app",
    "training a model",
    "kubernetes",
    "five agent personas",
]

if __name__ == "__main__":
    print("MUST", len(MUST), "WONT", len(WONT))
