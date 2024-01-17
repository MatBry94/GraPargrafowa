import tkinter as tk
from PIL import Image, ImageTk


class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Cienie Yharnam')

        # Ekran startowy
        self.start_screen()

    def start_screen(self):
        # Wprowadzenie do świata gry
        intro_text = (
            "Witaj w Yharnam - ponurym, gotyckim mieście skąpanym w wiecznym zmierzchu. "
            "Miasto to, pełne wieżowców i wiktoriańskiej architektury, skrywa mroczne sekrety "
            "i jest opanowane przez tajemniczą zarazę. Twoim zadaniem jest odnalezienie lekarstwa "
            "i odkrycie prawdy, która kryje się w cieniach tego miejsca."
        )

        self.intro_label = tk.Label(self.root, text=intro_text, wraplength=400, justify="left")
        self.intro_label.pack()

        # Obraz miasta Yharnam
        self.city_image = Image.open(r'C:\Users\mateu\PycharmProjects\GraAi\images\miasto.jpg')  # Zmień na rzeczywistą ścieżkę do obrazu
        self.city_image = self.city_image.resize((800, 600), Image.Resampling.LANCZOS)
        self.city_image_tk = ImageTk.PhotoImage(self.city_image)
        self.image_label = tk.Label(self.root, image=self.city_image_tk)
        self.image_label.pack()

        # Przycisk do rozpoczęcia gry
        self.start_button = tk.Button(self.root, text="Rozpocznij grę", command=self.begin_game)
        self.start_button.pack()

        # Dowolny klawisz kontynuuje
        self.root.bind('<Any-KeyPress>', self.begin_game)

    def begin_game(self, event=None):
        # Usuń elementy ekranu startowego
        self.intro_label.destroy()
        self.image_label.destroy()
        self.start_button.destroy()

        # Przechodzimy do pierwszych wyborów w grze
        self.first_choices()



    def make_choice(self, scene_image_path, choice1_text, choice2_text, choice1_scene, choice2_scene):
        # Usuń poprzednie elementy
        for widget in self.root.winfo_children():
            widget.destroy()

        # Wyświetl obraz dla sceny
        scene_image = Image.open(scene_image_path)
        scene_image = scene_image.resize((800, 600), Image.Resampling.LANCZOS)
        scene_image_tk = ImageTk.PhotoImage(scene_image)
        image_label = tk.Label(self.root, image=scene_image_tk)
        image_label.image = scene_image_tk  # Trzymaj referencję
        image_label.pack()

        # Dodaj przyciski decyzyjne
        choice1_button = tk.Button(self.root, text=choice1_text, command=choice1_scene)
        choice1_button.pack()

        choice2_button = tk.Button(self.root, text=choice2_text, command=choice2_scene)
        choice2_button.pack()

    def scene2(self):
        self.make_choice(
            r'C:\Users\mateu\PycharmProjects\GraAi\images\mistrz.jpg',
            'Odkrycie Sekretu Mistrza Ludwiga: Ujawnić jego tajemnicę mieszkańcom',
            'Odkrycie Sekretu Mistrza Ludwiga: Zachować go dla siebie.',
            self.scene3,
            self.scene3
        )

    # Przykładowe metody dla kolejnych scen i wyborów
    def scene3(self):
        self.make_choice(
            r'C:\Users\mateu\PycharmProjects\GraAi\images\duch.jpg',
            'Spotkanie z Duchem Anny: Pomóc jej odnaleźć spokój ?',
            'Spotkanie z Duchem Anny: Ignorować jej prośbę ?',
            self.scene4,
            self.scene4
        )


    def scene4(self):
        self.make_choice(
            r'C:\Users\mateu\PycharmProjects\GraAi\images\walka.jpg',
            'Konfrontacja z Potworami: Stawić im czoła ',
            'Konfrontacja z Potworami: Stawić im czoła poszukać alternatywnej ścieżki ',
            self.scene5,
            self.scene5
        )

    def scene5(self):
        self.make_choice(
            r'C:\Users\mateu\PycharmProjects\GraAi\images\bohater.jpg',
            'Finałowa Decyzja: Zniszczyć źródło zarazy',
            'Finałowa Decyzja: opuścić miasto, ratując tylko siebie',
            self.scene5a,
            self.scene5b
        )

    def scene5a(self):
        # Usuń poprzednie elementy
        for widget in self.root.winfo_children():
            widget.destroy()

        # Tekst dla sceny 5a
        final_text_5a = "Po heroicznym starciu, Eliasz pokonuje źródło zarazy, przywracając Yharnam do stanu przed klęską. Jego nazwisko zostanie zapamiętane przez wieki."

        # Obraz dla sceny 5a
        final_image_path_5a = r'C:\Users\mateu\PycharmProjects\GraAi\images\boss.jpg'  # Zmień ścieżkę do odpowiedniego obrazu
        final_image_5a = Image.open(final_image_path_5a)
        final_image_5a = final_image_5a.resize((800, 600), Image.Resampling.LANCZOS)
        final_image_tk_5a = ImageTk.PhotoImage(final_image_5a)
        image_label_5a = tk.Label(self.root, image=final_image_tk_5a)
        image_label_5a.image = final_image_tk_5a  # Trzymaj referencję
        image_label_5a.pack()

        # Etykieta z tekstem końcowym
        label_5a = tk.Label(self.root, text=final_text_5a, wraplength=400, justify="center")
        label_5a.pack()
        close_button = tk.Button(self.root, text="Zakończ grę", command=self.root.destroy)
        close_button.pack()

        # Kontynuacja opowieści i kolejne decyzje
        # Ustaw self.current_scene na kolejną scenę

    def scene5b(self):
        # Usuń poprzednie elementy
        for widget in self.root.winfo_children():
            widget.destroy()

        # Tekst dla sceny 5a
        final_text_5a = "Eliasz, wybierając własne bezpieczeństwo, opuszcza Yharnam. Jego decyzja rzuca cień na los mieszkańców, którzy pozostają w mroku zarazy."

        # Obraz dla sceny 5a
        final_image_path_5a = r'C:\Users\mateu\PycharmProjects\GraAi\images\odejscie.jpg'  # Zmień ścieżkę do odpowiedniego obrazu
        final_image_5a = Image.open(final_image_path_5a)
        final_image_5a = final_image_5a.resize((800, 600), Image.Resampling.LANCZOS)
        final_image_tk_5a = ImageTk.PhotoImage(final_image_5a)
        image_label_5a = tk.Label(self.root, image=final_image_tk_5a)
        image_label_5a.image = final_image_tk_5a  # Trzymaj referencję
        image_label_5a.pack()

        # Etykieta z tekstem końcowym
        label_5a = tk.Label(self.root, text=final_text_5a, wraplength=400, justify="center")
        label_5a.pack()
        close_button = tk.Button(self.root, text="Zakończ grę", command=self.root.destroy)
        close_button.pack()





    def first_choices(self):
        self.make_choice(
            r'C:\Users\mateu\PycharmProjects\GraAi\images\Irina.jpg',
            'Irena – tajemnicza kobieta, która zna sekrety miasta.',
            'Ojciec Gascoigne – szalony kapłan, który stracił rodzinę przez zarazę.',
            self.scene2,
            self.scene2
        )
# Główna funkcja uruchamiająca aplikację
def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()


# Wywołanie głównej funkcji
if __name__ == "__main__":
    main()