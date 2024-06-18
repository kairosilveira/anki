import genanki
import random

def shuffle_list(input_list):
    shuffled_list = input_list[:]
    random.shuffle(shuffled_list)
    return shuffled_list

def correct_translation_order(phrases_list):
    corrected_phrases = []
    
    for phrase in phrases_list:
        corrected_phrase = {'front': '', 'back': ''}
        corrected_phrase['front'] = phrase['back']
        corrected_phrase['back'] = phrase['front']
        corrected_phrases.append(corrected_phrase)
    
    return corrected_phrases

class AnkiDeckCreator:
    def __init__(self, deck_name, deck_id, model_id):
        self.deck_id = deck_id
        self.deck_name = deck_name
        self.model_id = model_id
        self.deck = genanki.Deck(self.deck_id, self.deck_name)
        self.model = self.create_anki_model()

    def create_anki_model(self):
        return genanki.Model(
            self.model_id,  # A unique random number
            'Default',
            fields=[
                {'name': 'Front'},
                {'name': 'Back'},
            ],
            templates=[
                {
                    'name': 'Default Card',
                    'qfmt': '{{Front}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
                },
            ], css=".card { font-size: 24px; text-align: center; }")

    def add_card(self, front, back):
        anki_note = genanki.Note(
            model=self.model,
            fields=[front, back]
        )
        self.deck.add_note(anki_note)

    def create_package(self, filename):
        package = genanki.Package(self.deck)
        package.write_to_file(filename)

    def generate_deck(self, phrases_list):
        for phrase in phrases_list:
            self.add_card(phrase['front'], phrase['back'])
