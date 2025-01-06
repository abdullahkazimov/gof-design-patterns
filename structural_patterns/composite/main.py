from composite import F1Driver, F1Team

def main():
    # Create individual drivers
    driver1 = F1Driver("Max Verstappen")
    driver2 = F1Driver("Sergio Pérez")
    driver3 = F1Driver("Lewis Hamilton")
    driver4 = F1Driver("George Russell")

    # Create first team (Red Bull Racing)
    team_red_bull = F1Team("Red Bull Racing")
    team_red_bull.add_item(driver1)
    team_red_bull.add_item(driver2)

    # Create second team (Mercedes-AMG Petronas)
    team_mercedes = F1Team("Mercedes-AMG Petronas")
    team_mercedes.add_item(driver3)
    team_mercedes.add_item(driver4)

    new_team = F1Team("Red Mercedes Team")
    new_team.add_item(team_mercedes)
    new_team.add_item(team_red_bull)

    # Display the teams and their drivers
    print(team_red_bull.display())
    print()
    print(team_mercedes.display())
    print()
    print(new_team.display())

if __name__ == "__main__":
    main()
