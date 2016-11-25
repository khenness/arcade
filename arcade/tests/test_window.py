from unittest import TestCase


class TestWindow(TestCase):

    def test_is_resizable(self):
        import arcade
        window = arcade.Window(200, 100, resizable=True)
        self.assertEqual(window.resizable, True)
        window.close()

    def test_is_not_resizable(self):
        import arcade
        window = arcade.Window(200, 100, resizable=False)
        self.assertEqual(window.resizable, False)
        window.close()

    def test_allows_minimum_size(self):
        import arcade
        window = arcade.Window(200, 100, resizable=True)
        window.set_minimum_size(200, 200)
        window.close()

    def test_disallows_minimum_size(self):
        import arcade
        window = arcade.Window(200, 100, resizable=False)
        self.assertRaises(ValueError, window.set_minimum_size, 200, 200)
        window.close()

    def test_allows_maximum_size(self):
        import arcade
        window = arcade.Window(200, 100, resizable=True)
        window.set_maximum_size(200, 200)
        window.close()

    def test_disallows_maximum_size(self):
        import arcade
        window = arcade.Window(200, 100, resizable=False)
        self.assertRaises(ValueError, window.set_maximum_size, 200, 200)
        window.close()

    def test_set_size_location(self):
        import arcade
        window = arcade.Window(200, 100)
        window.set_size(900, 800)
        self.assertEqual(window.width, 900)
        self.assertEqual(window.height, 800)
        window.close()
