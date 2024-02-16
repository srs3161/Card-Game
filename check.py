import tkinter as tk
from CardGame import Card, PictureCard, Deck, Game
from PIL import Image, ImageTk
import os
MAX_CARD_WIDTH = 50  # Maximum width for the card images (adjust as needed)
CARD_HEIGHT_RATIO = 1.4  # Aspect ratio of the card images (height / width)
MAX_WIDTH = 500  # Maximum width for the card image
MAX_HEIGHT = 726
PADDING = 10
class CardGameGUI:

    def __init__(self, root):
        self.root = root
        self.root.title(" CSC/CYEN 131 Card Game")
        self.game = Game()
        self.deck = Deck()
        self.canvas = tk.Canvas(self.root, width=1000, height=600, bg="lightgrey")
        self.canvas.pack()
        self.card_images = {}
        self.card_instances = []
        self.load_card_images()
        # self.play_game()
        
        self.default_image_path = "images\default.png"
        self.default_image = self.load_default_image()

        # Display default images for player and computer cards
        self.default_card(self.default_image, 60, 40)  #computer card
        self.default_card(self.default_image, 620, 40)  #player card


        self.play_button = tk.Button(root, text="Play", width=5, height=1, font=("Helvetica", 12),bg="lightblue",borderwidth=2, relief="raised",command=self.play_game)
        self.play_button.pack(side=tk.LEFT, padx=PADDING)

        self.restart_button = tk.Button(root, text="Restart", justify="left",width=5, height=1, font=("Helvetica", 12),bg="lightblue",borderwidth=2, relief="raised", command=self.restart)
        self.restart_button.pack(side=tk.LEFT, padx=PADDING)

        self.quit_button = tk.Button(root, text="Quit", justify="right",width=5, height=1, font=("Helvetica", 12),bg="lightblue",borderwidth=2, relief="raised", command=self.quit_game)
        self.quit_button.pack(side=tk.RIGHT, padx=PADDING)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

        self.player_card_label = tk.Label(root, text="You Picked")
        self.player_card_label.place(relx=0.99, rely=0.01, anchor=tk.NE, bordermode="outside")

        self.computer_card_label = tk.Label(root, text="Computer Picked")
        # self.player_card_label.pack(side=tk.TOP)
        self.computer_card_label.place(relx=0.01, rely=0.01, anchor=tk.NW, bordermode="outside")

       
        
    def load_card_images(self):
        for suit in Card.POSSIBLESUITS:
            for number in range(2, 11):
                card = PictureCard(number, suit)
                self.card_instances.append(card)
                imagefile = card._imagefile
                dir = "images"
                path = os.path.join(dir, imagefile)
                self.card_images[(number, suit)] = tk.PhotoImage(file=path)
        
    def load_default_image(self):
        try:
            default_image = Image.open(self.default_image_path)
            default_image = default_image.resize((min(default_image.width, MAX_WIDTH), min(default_image.height, MAX_HEIGHT)))
            return ImageTk.PhotoImage(default_image)
        except FileNotFoundError:
            return None
        
    def play_game(self):
        
        if self.game.deck.size() < 2:
            self.canvas.create_text(580, 790, text="Not enough cards to play.")
            self.root.update()
            return

        def play_round():
            playercard = self.game.deck.draw()
            computercard = self.game.deck.draw()

            self.canvas.delete("all")
            
            self.display_card(computercard, 60, 40)
            self.display_card(playercard, 620, 40)

            # I --> Computer and YOU ---> Player
            if playercard > computercard:
                self.canvas.create_text(580, 790, text="YOU WIN", font=("aerial", 14))
            elif playercard < computercard:
                self.canvas.create_text(580, 790, text="I WIN", font=("aerial", 14))
            else:
                self.canvas.create_text(580, 790, text="IT'S A DRAW", font=("aerial", 14))

            self.root.update()

        play_round()
                
    def display_card(self, card, x, y):
        number = card.number
        suit = card.suit
        image = self.card_images.get((number, suit))
        self.canvas.create_image(x, y, image=image, anchor=tk.NW)
        
    def default_card(self, image, x, y):
        if image:
            self.canvas.create_image(x, y, image=image, anchor=tk.NW)  

 
    def restart(self):
        self.play_button.config(command=lambda: None)
        self.game = Game()  
        self.canvas.delete("all")  

        self.load_card_images()
        # Load the default card image
        image_path = "images\default.png"
        image = Image.open(image_path)
        image = image.resize((min(image.width, MAX_WIDTH), min(image.height, MAX_HEIGHT)))
        self.default_image = ImageTk.PhotoImage(image)
        
        # Display the default card for both player and computer
        if self.default_image:
            self.canvas.create_image(60, 40, image=self.default_image, anchor=tk.NW)
            self.canvas.create_image(620, 40, image=self.default_image, anchor=tk.NW)
            self.canvas.create_text(580, 730, text="Who wins?", font=("aerial", 14))
            
        self.play_button.config(command=self.play_game)
        # Update the display
        self.root.update()
        
    def quit_game(self):
        self.root.destroy()


if __name__ == "__main__":
    # deck = Deck()
    root = tk.Tk()
    game = CardGameGUI(root)
    game.root.mainloop()

