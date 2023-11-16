import unittest
from app import make_questions

class TestQuiz(unittest.TestCase):

    def test_questions_contstructor(self):
        questions, _ = make_questions()
        self.assertTrue( isinstance(questions, list) )

    def test_question_attributes(self):
        # we will test that each question has a prompt and an answer
        questions, _ = make_questions()
        for entry in questions:
            self.assertIsNotNone(entry.prompt)
            self.assertIsNotNone(entry.answer)

if __name__ == '__main__':
    unittest.main()