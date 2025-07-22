import unittest
import os
from unittest.mock import patch, MagicMock
import youtube_downloader


class TestYoutubeDownloader(unittest.TestCase):

    def setUp(self):
        self.test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        self.test_info = {
            'title': 'Sample Video',
            'ext': 'mp4'
        }
        self.test_output_path = os.path.join(
            os.path.expanduser("~/Desktop"),
            f"{self.test_info['title']}.{self.test_info['ext']}"
        )

    @patch('yt_dlp.YoutubeDL')
    def test_download_successful(self, mock_yt_dlp):
        mock_ydl_instance = MagicMock()
        mock_ydl_instance.extract_info.return_value = self.test_info
        mock_yt_dlp.return_value.__enter__.return_value = mock_ydl_instance

        youtube_downloader.download_video(self.test_url)

        mock_ydl_instance.extract_info.assert_called_once_with(self.test_url, download=True)

    def test_output_path_exists(self):
        desktop_path = os.path.expanduser("~/Desktop")
        self.assertTrue(os.path.isdir(desktop_path), "Desktop path does not exist")

if __name__ == "__main__":
    unittest.main()
