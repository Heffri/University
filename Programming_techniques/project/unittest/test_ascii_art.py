import unittest
from unittest.mock import patch
from io import StringIO
from MAINMAIN import ASCIIArt, SessionManager, CommandHandler

class TestASCIIArtStudio(unittest.TestCase):

    def setUp(self):
        self.art = ASCIIArt()

    def test_load_image_success(self):
        with patch('builtins.print') as mocked_print:
            self.art.load_image('slalom.jpg', 'test_image')
            mocked_print.assert_called_with("Image 'test_image' loaded successfully and set as current.")
            self.assertIn('test_image', self.art.images)
            self.assertEqual(self.art.current, 'test_image')

    def test_load_image_file_not_found(self):
        with patch('builtins.print') as mocked_print:
            self.art.load_image('slalom.jpg', 'test_image')
            mocked_print.assert_called_with("File 'slalom.jpg' not found.")

    def test_info_specific_image(self):
        self.art.load_image('slalom.jpg', 'test_image')
        with patch('builtins.print') as mocked_print:
            self.art.info('test_image')
            mocked_print.assert_called_with("Alias: test_image")

    def test_info_no_image_found(self):
        with patch('builtins.print') as mocked_print:
            self.art.info('nonexistent_image')
            mocked_print.assert_called_with("No image found with alias 'nonexistent_image'.")




class TestSessionManager(unittest.TestCase):

    def setUp(self):
        self.art = ASCIIArt()
        self.session_manager = SessionManager(self.art)

    def test_save_session_success(self):
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file, \
             patch('json.dump') as mocked_json_dump:
            self.session_manager.save_session('session.json')
            mocked_file.assert_called_with('session.json', 'w')
            self.assertTrue(mocked_json_dump.called)

    def test_load_session_from_file_success(self):
        session_data = {'test_image': {'filepath': 'slalom.jpg', 'properties': {'width': 50, 'brightness': 1.0, 'contrast': 1.0}}}
        with patch('builtins.open', unittest.mock.mock_open(read_data=json.dumps(session_data))), \
             patch('json.load', return_value=session_data), \
             patch.object(ASCIIArt, 'load_image') as mocked_load_image:
            self.session_manager.load_session('session.json')
            mocked_load_image.assert_called_with('slalom.jpg', 'test_image')





class TestCommandHandler(unittest.TestCase):

    def setUp(self):
        self.art = ASCIIArt()
        self.session_manager = SessionManager(self.art)
        self.command_handler = CommandHandler(self.art, self.session_manager)

    def test_handle_load_command(self):
        with patch.object(ASCIIArt, 'load_image') as mocked_load_image:
            self.command_handler.handle_command('load slalom.jpg as test_image')
            mocked_load_image.assert_called_with('slalom.jpg', 'test_image')

    def test_handle_info_command(self):
        with patch.object(ASCIIArt, 'info') as mocked_info:
            self.command_handler.handle_command('info test_image')
            mocked_info.assert_called_with('test_image')

    def test_handle_render_command(self):
        with patch.object(ASCIIArt, 'render') as mocked_render:
            self.command_handler.handle_command('render test_image')
            mocked_render.assert_called_with('test_image')


if __name__ == '__main__':
    unittest.main()