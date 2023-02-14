#
from quart_error import app as tested_app, text_404
import unittest
import json

# declar test class
class TestApp(unittest.IsolatedAsyncioTestCase):
    # setup async method
    async def asyncSetUp(self):
        self.app = tested_app.test_client()

    async def test_raise(self):
        test = await self.app.get('/api')
        # this raise an error 500
        self.assertEqual(test.status_code, 500)

    async def test_proper_404(self):
        url = await self.app.get('/ddweewaa')
        # assert the error code
       

        # get your information
        url_body = json.loads(str(await url.get_data(), "utf8"))
        self.assertEqual(url.status_code, 404)
        self.assertEqual(url_body['Description'], text_404)

if __name__ == '__main__':
    unittest.main()
