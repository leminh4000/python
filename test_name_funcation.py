import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    def test_first_name_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name=get_formatted_name('janis', 'joplin')
        if len(formatted_name) == 0:
            print('no names found')
        
        self.assertEqual(formatted_name, "Janis Joplin")
    def test_first_middle_last_name(self):
        """Do names like 'Wolgang Amadeus Mozart' work?
        """
        formatted_name=get_formatted_name('wolgang', 'mozart', 'amadeus')
        if len(formatted_name) == 0:
            print('no names found')
        
        self.assertEqual(formatted_name, "Wolgang Amadeus Mozart")    
unittest.main()        
