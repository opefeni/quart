import unittest
import json

from quart_basic import app as tested_app

class TestApp(unittest.IsolatedAsyncioTestCase):
    async def test_help(self):
        # create a Quart client instance
        app = tested_app.test_client()

        # calling the api endpoint
        hello = await app.get('/api')

        # assert the body
        data = await hello.get_data()
        body = json.loads(str(data, 'utf8'))
        self.assertEqual(body['Hello'], 'World')


if __name__ == '__main__':
    unittest.main()

