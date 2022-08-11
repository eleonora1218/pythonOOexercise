"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    {length of dictionary} words read.

    >>> wf.random() in ['Pacific', 'Atlantic', 'Indian']
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""
        dictionary = open(path)
        self.words = self.parse(dictionary)
        print(f"{len(self.words)} words read")

    def parse(self, dictionary):
        """Simplifies dictionary into an iterable list."""
        return [w.strip() for w in dictionary]

    def random(self):
        """Return random word."""
        return random.choice(self.words)



class SpecialWordFinder(WordFinder):
    """Subclass
    Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("words.txt")
    {length of dictionary} words read.

    >>> swf.random() in ['Pacific', 'Atlantic', 'Indian']
    True
    """

    def parse(self, dictionary):
        """Simplifies dictionary into an iterable list excluding blanks & comments."""
        return [w.strip() for w in dictionary
                if w.strip() and not w.startswith("#")]