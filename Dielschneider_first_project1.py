teamranking_national = ['1. Ireland','2. South Africa','3. New Zealand','4. France','5. England','6. Argentina','7. Scotland','8.Italy','9. Fiji','10. Australia']
print(teamranking_national)

team_rosters = {
    'Ireland': ["name: Johnny Sexton, position: Fly-half",
"name: James Ryan, position: Lock",
"name: Tadhg Furlong, position: Prop",
"name: Peter O'Mahony, position: Flanker",
"name: Josh van der Flier, position: Flanker",
"name: Caelan Doris, position: Number 8",
"name: Jamison Gibson-Park, position: Scrum-half",
"name: Bundee Aki, position: Centre",
"name: Garry Ringrose, position: Centre",
"name: Hugo Keenan, position: Fullback",
"name: Andrew Porter, position: Prop",
"name: Iain Henderson, position: Lock",
"name: Jack Conan, position: Number 8",
"name: Robbie Henshaw, position: Centre",
"name: Mack Hansen, position: Wing",
"name: James Lowe, position: Wing",
"name: Keegan Glover, position: Hooker"],
    'South Africa': ["name: Siya Kolisi, position: Flanker",
"name: Pieter-Steph Du Toit, position: Flanker",
"name: Lood De Jager, position: Lock",
"name: Francois Louw, position: Flanker",
"name: Faf de Klerk, position: Scrum-half",
"name: Handré Pollard, position: Fly-half",
"name: Damian de Allende, position: Centre",
"name: Lukhanyo Am, position: Centre",
"name: Cheslin Kolbe, position: Wing",
"name: Makazole Mapimpi, position: Wing",
"name: Bongi Mbonambi, position: Hooker",
"name: Eben Edzebeth, position: Lock",
"name: Trevor Nyakane, position: Prop",
"name: Steven Kitshoff, position: Prop",
"name: Malcolm Marx, position: Hooker",
"name: Vincent Koch, position: Prop"],
    'New Zealand': ["name: Sam Cane, position: Flanker",
"name: Brodie Retallick, position: Lock",
"name: Joe Moody, position: Prop",
"name: Ardie Savea, position: Flanker",
"name: Tawera Kerr-Barlow, position: Scrum-half",
"name: Beauden Barrett, position: Fly-half",
"name: Ngani Laumape, position: Centre",
"name: Rieko Ioane, position: Wing",
"name: Sevu Reece, position: Wing",
"name: Damian McKenzie, position: Fullback",
"name: Owen Franks, position: Prop",
"name: Scott Barrett, position: Lock",
"name: Dalton Papali'i, position: Flanker",
"name: Anton Lienert-Brown, position: Centre",
"name: Jordie Barrett, position: Fullback/Wing",
"name: Sam Whitelock, position: Lock",
"name: Codie Taylor, position: Hooker"],
    'France': ["name: Antoine Dupont, position: Scrum-half",
"name: Romain Ntamack, position: Fly-half",
"name: Virimi Vakatawa, position: Centre",
"name: Gaël Fickou, position: Centre",
"name: Damian Penaud, position: Wing",
"name: Louis Rees-Zammit, position: Wing",
"name: Melvyn Jaminet, position: Fullback",
"name: Cameron Woki, position: Lock/Flanker",
"name: Paul Willemse, position: Lock",
"name: Romain Taofifenua, position: Lock",
"name: Cyril Baille, position: Prop",
"name: Gustav Louw, position: Prop",
"name: Julien Marchand, position: Hooker",
"name: Charles Ollivon, position: Flanker",
"name: Gregory Alldritt, position: Number 8",
"name: Baptiste Serin, position: Scrum-half",
"name: Maxime Medard, position: Fullback"],
    'England': ["name: Owen Farrell, position: Fly-half/Centre",
"name: Maro Itoje, position: Lock",
"name: Tom Curry, position: Flanker",
"name: Courtney Lawes, position: Lock/Flanker",
"name: Freddie Steward, position: Fullback",
"name: Henry Slade, position: Centre",
"name: Billy Vunipola, position: Number 8",
"name: Ben Youngs, position: Scrum-half",
"name: Elliot Daly, position: Wing/Centre",
"name: Max Malins, position: Wing",
"name: Joe Marchant, position: Centre",
"name: Kyle Sinckler, position: Prop",
"name: Jamie George, position: Hooker",
"name: Joe Launchbury, position: Lock",
"name: Dan Cole, position: Prop",
"name: Sam Simmonds, position: Number 8",
"name: Jack Nowell, position: Wing"],
    'Argentina': ["name: Pablo Matera, position: Flanker",
"name: Marcos Kremer, position: Flanker",
"name: Agustín Creevy, position: Hooker",
"name: Tomas Lavanini, position: Lock",
"name: Matías Alemanno, position: Lock",
"name: Julián Montoya, position: Hooker",
"name: Nicolás Sánchez, position: Fly-half",
"name: Gonzalo Bertranou, position: Scrum-half",
"name: Matías Moroni, position: Centre",
"name: Jerónimo De la Fuente, position: Centre",
"name: Emiliano Boffelli, position: Wing",
"name: Pato Fernández, position: Wing",
"name: Santiago Carreras, position: Fullback/Wing",
"name: Nahuel Tetaz Chaparro, position: Prop",
"name: Francisco Gómez Kodela, position: Prop",
"name: Lautaro Bazán Vélez, position: Scrum-half",
"name: Facundo Isa, position: Number 8"],
    'Scotland': ["name: Stuart Hogg, position: Fullback",
"name: Finn Russell, position: Fly-half",
"name: Hamish Watson, position: Flanker",
"name: Jamie Ritchie, position: Flanker",
"name: Duncan Weir, position: Fly-half",
"name: Ali Price, position: Scrum-half",
"name: Mark Bennett, position: Centre",
"name: Chris Harris, position: Centre",
"name: Darcy Graham, position: Wing",
"name: Sione Tuipulotu, position: Centre",
"name: Adam Hastings, position: Fly-half",
"name: Zander Fagerson, position: Prop",
"name: WP Nel, position: Prop",
"name: Scott Cummings, position: Lock",
"name: Jonny Gray, position: Lock",
"name: Matt Fagerson, position: Number 8",
"name: Luke Crosbie, position: Flanker"],
    'Italy': ["name: Sergio Parisse, position: Number 8",
"name: Canna Tommaso, position: Fly-half",
"name: Giacomo Nicotera, position: Hooker",
"name: Lorenzo Cannone, position: Flanker",
"name: Michele Lamaro, position: Flanker",
"name: Nicolo' Gallo, position: Lock",
"name: Federico Ruzza, position: Lock",
"name: Monty Ioane, position: Wing",
"name: Tommaso Menoncello, position: Centre",
"name: Pierre Bruno, position: Wing",
"name: Paolo Garbisi, position: Fly-half",
"name: Luca Bigi, position: Hooker",
"name: Guglielmo Palazzani, position: Scrum-half",
"name: Marco Riccioni, position: Prop",
"name: Danilo Fischetti, position: Prop",
"name: Edoardo Padovani, position: Fullback",
"name: Sebastian Negri, position: Flanker"],
    'Fiji': ["name: Semi Radradra, position: Centre",
"name: Josua Tuisova, position: Wing",
"name: Vereniki Goneva, position: Wing",
"name: Levani Botia, position: Flanker",
"name: Peceli Yato, position: Number 8",
"name: Teti Tela, position: Fly-half",
"name: Frank Lomani, position: Scrum-half",
"name: Niko Matawalu, position: Scrum-half",
"name: Alivereti Raka, position: Wing",
"name: Isake Katonibau, position: Flanker",
"name: Savenaca Rawaca, position: Hooker",
"name: Tevita Cavubati, position: Lock",
"name: Mikaele Tuugakoto, position: Lock",
"name: Leone Nakarawa, position: Lock",
"name: Manasa Saulo, position: Prop",
"name: Viliame Mata, position: Number 8",
"name: Josua Kerevi, position: Centre"],
    'Australia': ["name: Michael Hooper, position: Flanker",
"name: James O'Connor, position: Fly-half/Centre",
"name: Samu Kerevi, position: Centre",
"name: Quade Cooper, position: Fly-half",
"name: Kurtley Beale, position: Fullback",
"name: Taniela Tupou, position: Prop",
"name: Allan Alaalatoa, position: Prop",
"name: Matt Philip, position: Lock",
"name: Izack Rodda, position: Lock",
"name: Rob Valetini, position: Flanker",
"name: Tate McDermott, position: Scrum-half",
"name: Nick Phipps, position: Scrum-half",
"name: Andrew Kellaway, position: Wing",
"name: Marika Koroibete, position: Wing",
"name: Lukhan Salakaia-Loto, position: Lock/Flanker",
"name: Harry Wilson, position: Number 8",
"name: Jordan Petaia, position: Centre/Wing"]
}


def display_teams():
    print("Top 10 National Rugby Teams:")
    for team in teamranking_national:
        print(team)


def display_roster(team):
    team_name = team.split('. ')[1]  
    if team_name in team_rosters:
        print(f"Roster for {team_name}: {', '.join(team_rosters[team_name])}")
    else:
        print("Team roster not found.")


def find_team_index(team_name):
    for i, team in enumerate(teamranking_national):
        if team_name.lower() in team.lower():
            return i
    return None


def predict_winner(team1, team2):
    index1 = find_team_index(team1)
    index2 = find_team_index(team2)

    if index1 is not None and index2 is not None:
        if index1 < index2:
            print(f"{teamranking_national[index1]} is more likely to win against {teamranking_national[index2]}.")
        elif index1 > index2:
            print(f"{teamranking_national[index2]} is more likely to win against {teamranking_national[index1]}.")
        else:
            print("Both teams are equally ranked!")
    else:
        print("One or both teams not found!")


def main():
    while True:
        print("\n--- Rugby Team App ---")
        print("1. Display top 10 teams")
        print("2. View a team's roster")
        print("3. Predict match winner between two teams")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            display_teams()
        elif choice == '2':
            team_name = input("Enter team name or number: ")
            team_found = next((team for team in teamranking_national if team_name.lower() in team.lower()), None)
            if team_found:
                display_roster(team_found)
            else:
                print("Team not found.")
        elif choice == '3':
            team1 = input("Enter the first team name or number: ")
            team2 = input("Enter the second team name or number: ")
            predict_winner(team1, team2)
        elif choice == '4':
            print("goodbye.")
            break
        else:
            print("Invalid choice. Please choose again.")

main()
