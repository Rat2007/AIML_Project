import os

# Candidates
candidates = {
    "1": "Alice",
    "2": "Bob",
    "3": "Charlie"
}


# Load users
def load_users():
    with open("users.txt", "r") as f:
        return [user.strip() for user in f.readlines()]


# Load voted users
def load_votes():
    if not os.path.exists("votes.txt"):
        return {}

    votes = {}
    with open("votes.txt", "r") as f:
        for line in f:
            user, choice = line.strip().split(",")
            votes[user] = choice
    return votes


# Save vote
def save_vote(user, choice):
    with open("votes.txt", "a") as f:
        f.write(f"{user},{choice}\n")


# Count votes
def count_votes(votes):
    result = {c: 0 for c in candidates.keys()}
    for choice in votes.values():
        result[choice] += 1
    return result


# Main system
def voting_system():
    users = load_users()
    votes = load_votes()

    user = input("Enter your user ID: ")

    if user not in users:
        print("❌ Invalid user!")
        return

    if user in votes:
        print("⚠️ You have already voted!")
        return

    print("\nCandidates:")
    for key, name in candidates.items():
        print(f"{key}. {name}")

    choice = input("Enter your choice: ")

    if choice not in candidates:
        print("❌ Invalid choice!")
        return

    save_vote(user, choice)
    print("✅ Vote recorded successfully!")


# Show results
def show_results():
    votes = load_votes()
    results = count_votes(votes)

    print("\n📊 Results:")
    for key, count in results.items():
        print(f"{candidates[key]}: {count} votes")


# Menu
while True:
    print("\n--- Online Voting System ---")
    print("1. Vote")
    print("2. Show Results")
    print("3. Exit")

    option = input("Choose option: ")

    if option == "1":
        voting_system()
    elif option == "2":
        show_results()
    elif option == "3":
        print("Exiting...")
        break
    else:
        print("Invalid option!")