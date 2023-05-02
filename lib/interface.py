from data_downloader import get_ranking, filter_by_country, get_club_data
from vizualize import plot_club_elo

def clubs_without_spaces(club_series):
    return [club.replace(' ', '') for club in club_series]

def get_country_elo(df, country_tag):
    filtered_df = filter_by_country(df, country_tag)
    clubs = clubs_without_spaces(filtered_df['Club'])
    return clubs

def select_teams(df, num_teams, country_tag):
    clubs = get_country_elo(df, country_tag)
    selected_clubs = []
    for i in range(num_teams):
        while True:
            print("\nAvailable teams:")
            for idx, club in enumerate(clubs, start=1):
                print(f"{idx}. {club}")
            try:
                choice = int(input(f"Select team {i+1}: ")) - 1
                if choice >= 0 and choice < len(clubs):
                    selected_clubs.append(clubs.pop(choice))
                    break
                else:
                    print("Invalid selection. Please try again.")
            except (ValueError):
                print("Invalid input. Please try again.")
    return selected_clubs

def main():
    ranking_date = '2022-05-01'
    df = get_ranking(ranking_date)

    if df is not None:
        while True:
            print("Menu:")
            print("1. Compare entire league")
            print("2. Compare teams from same league")
            print("3. Compare teams from different leagues")
            try:
                option = int(input("Choose an option (1-3): "))
                if option in [1, 2, 3]:
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please try again.")

        if option == 1:
            country_tag = input("Enter the league's country code (e.g., ENG,            ESP, ITA, GER, etc.): ")
            club_list = get_country_elo(df, country_tag)
        elif option == 2:
            try:
                num_teams = int(input("How many teams do you want to compare? "))
            except ValueError:
                print("Invalid input. Please try again.")
                return

            country_tag = input("Enter the league's country code (e.g., ENG, ESP, ITA, GER, etc.): ")
            club_list = select_teams(df, num_teams, country_tag)
        else:
            num_teams = int(input("How many teams do you want to compare? "))
            club_list = []
            for i in range(num_teams):
                while True:
                    country_tag = input(f"Enter the league's country code for team {i + 1} (e.g., ENG, ESP, ITA, GER, etc.): ")
                    clubs = get_country_elo(df, country_tag)
                    print("\nAvailable teams:")
                    for idx, club in enumerate(clubs, start=1):
                        print(f"{idx}. {club}")
                    try:
                        choice = int(input(f"Select team {i + 1}: ")) - 1
                        if choice >= 0 and choice < len(clubs):
                            club_list.append(clubs[choice])
                            break
                        else:
                            print("Invalid selection. Please try again.")
                    except (ValueError):
                        print("Invalid input. Please try again.")

        club_data = get_club_data(club_list)
        plot_club_elo(club_list, club_data)

if __name__ == '__main__':
    main()

