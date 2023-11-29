import unittest
from src.loader import SlackDataLoader
import pandas as pd


class TestSlackDataLoader(unittest.TestCase):
    def setUp(self):
        self.base_path = "./src/anonymized/"
        self.loader = SlackDataLoader(self.base_path)
        self.channels = self.loader.get_channels()

    def test_dataframe_columns(self):
        all_data = []
        for channel in self.channels:
            data = self.loader.slack_parser(f"{self.base_path}/{channel['name']}/")
            all_data.append(data)
        df = pd.concat(all_data, ignore_index=True)

        expected_columns = ['msg_type', 'msg_content', 'sender_name', 'msg_sent_time',
                            'msg_dist_type', 'time_thread_start', 'reply_count',
                            'reply_users_count', 'reply_users',
                            'tm_thread_end', 'channel']
        self.assertTrue(set(expected_columns).issubset(df.columns))


if __name__ == '__main__':
    unittest.main()
