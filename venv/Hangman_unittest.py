import unittest
import random
import string
from Hangman import hangman
from unittest.mock import patch, MagicMock

class MyTestCase(unittest.TestCase):
    # letter = chr(random.randint(ord('a'), ord('z')))
    # @patch("builtins.input", return_value=letter)
    # def test_play_game(self, mock_letter):
    #     hang = hangman()
    #     guess_letter = hang.play_game()
    #     print("random letter:", mock_letter)

    def test_create_mock_letter(self):
        get_letter = chr(random.randint(ord('a'), ord('z')))
        print("letter:", get_letter)
        return get_letter


    # @patch("builtins.input", return_value=self.create_mock_letter())
    # def test_play_game(self):
    #     hang = hangman()
    #     test = self.create_mock_letter()
    #     guess_letter = test
    #     guess_letter = hang.play_game()
        # print("random letter:", mock_letter)

    # def test_display_blank_word(self, mock_secret_word):
    #     hang = hangman()
    #     word = hang.secret_word
    #     print("WHAT IS THE SECRET WORD?:", word)
    #     n = ''
    #     for i in range(len(word)):  # Get length of the secret_word and loop over it, displaying _
    #         append '_'.join()
    #     self.assertEqual(hang.display_blank_word(), '_ _ _ _ _')

    @patch("builtins.input", return_value="a")
    def test_get_user_input(self, mock_get_user_input):
        hang = hangman()
        g_letter = hang.get_user_input()
        self.assertEqual(g_letter, 'a')

    @patch("builtins.input", return_value="z")
    def test_get_user_input2(self, mock_get_user_input):
        hang = hangman()
        g_letter = hang.get_user_input()
        self.assertEqual(g_letter, 'z')

    def test_find_letter(self):
        counter = 100

        while counter:
            hang = hangman()
            word = hang.secret_word  # Get secret word for this instance

            l = random.choice(word)  # Get random letter from the secret word to ensure letter is found in word since word is random
            assert hang.find_letter(l) == True
            counter -= 1

    def test_find_no_letter(self):
        counter = 100

        while counter:
            hang = hangman()
            word = hang.secret_word  # Get secret word for this instance

            p = list(set(string.ascii_letters + string.digits) - set(word))  # Create a list of random letters that do not contain the letters in the secret word
            c = random.choice(p)  # Choose a letter from the new list created to assert the letter is not in secret word
            assert hang.find_letter(c) == None
            counter -= 1

    def test_display_hangman_board(self):
        pass


    def test_win_hangman(self):
        pass

if __name__ == '__main__':
    unittest.main()
