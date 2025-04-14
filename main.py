from utils import check_strength, generate_strong_password, load_common_passwords

def main():
    common_passwords = load_common_passwords()

    while True:
        print("\n=== Password Strength Checker & Generator ===")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            password = input("Enter password to check: ")
            score, suggestions = check_strength(password, common_passwords)
            print(f"\n🔐 Strength Score: {score}/100")
            if suggestions:
                print("💡 Suggestions to improve:")
                for s in suggestions:
                    print(f" - {s}")
            else:
                print("✅ Great password!")

        elif choice == "2":
            length = input("Enter desired length (default 12): ")
            try:
                length = int(length)
            except:
                length = 12
            new_password = generate_strong_password(length)
            print(f"\n🆕 Generated Password: {new_password}")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
