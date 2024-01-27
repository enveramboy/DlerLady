from PIL import Image, ImageTk

class Card:
    def __init__(self, path, name, value):
        self.p = path
        self.n = name
        self.val = value

deck = [
    # Ace
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\ace_of_clubs.png", "ace of clubs", (1, 11)),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\ace_of_diamonds.png", "ace of diamonds", (1, 11)),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\ace_of_hearts.png", "ace of hearts", (1, 11)),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\ace_of_spades.png", "ace of spades", (1, 11)),

    # 2
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\2_of_clubs.png", "2 of clubs", 2), 
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\2_of_diamonds.png", "2 of diamonds", 2), 
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\2_of_hearts.png", "2 of hearts", 2),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\2_of_spades.png", "2 of spades", 2),

    # 3
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\3_of_clubs.png", "3 of clubs", 3),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\3_of_diamonds.png", "3 of diamonds", 3),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\3_of_hearts.png", "3 of hearts", 3),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\3_of_spades.png", "3 of spades", 3),

    # 4
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\4_of_clubs.png", "4 of clubs", 4),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\4_of_diamonds.png", "4 of diamonds", 4),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\4_of_hearts.png", "4 of hearts", 4),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\4_of_spades.png", "4 of spades", 4),

    # 5
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\5_of_clubs.png", "5 of clubs", 5),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\5_of_diamonds.png", "5 of diamonds", 5),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\5_of_hearts.png", "5 of hearts", 5),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\5_of_spades.png", "5 of spades", 5),

    # 6
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\6_of_clubs.png", "6 of clubs", 6),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\6_of_diamonds.png", "6 of diamonds", 6),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\6_of_hearts.png", "6 of hearts", 6),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\6_of_spades.png", "6 of spades", 6),

    # 7
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\7_of_clubs.png", "7 of clubs", 7),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\7_of_diamonds.png", "7 of diamonds", 7),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\7_of_hearts.png", "7 of hearts", 7),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\7_of_spades.png", "7 of spades", 7),

    # 8
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\8_of_clubs.png", "8 of clubs", 8),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\8_of_diamonds.png", "8 of diamonds", 8),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\8_of_hearts.png", "8 of hearts", 8),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\8_of_spades.png", "8 of spades", 8),

    # 9
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\9_of_clubs.png", "9 of clubs", 9),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\9_of_diamonds.png", "9 of diamonds", 9),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\9_of_hearts.png", "9 of hearts", 9),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\9_of_spades.png", "9 of spades", 9),

    # 10
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\10_of_clubs.png", "10 of clubs", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\10_of_diamonds.png", "10 of diamonds", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\10_of_hearts.png", "10 of hearts", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\10_of_spades.png", "10 of spades", 10),

    # Jack
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\jack_of_clubs2.png", "jack of clubs", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\jack_of_diamonds2.png", "jack of diamonds", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\jack_of_hearts2.png", "jack of hearts", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\jack_of_spades2.png", "jack of spades", 10),

    # King
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\king_of_clubs2.png", "king of clubs", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\king_of_diamonds2.png", "king of diamonds", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\king_of_hearts2.png", "king of hearts", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\king_of_spades2.png", "king of spades", 10),

    # Queen
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\queen_of_clubs2.png", "queen of clubs", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\queen_of_diamonds2.png", "queen of diamonds", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\queen_of_hearts2.png", "queen of hearts", 10),
    Card(r"C:\Users\enver\OneDrive\Desktop\MsDealer\cards\queen_of_spades2.png", "queen of spades", 10)
]