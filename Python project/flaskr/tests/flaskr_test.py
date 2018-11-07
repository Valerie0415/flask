-*- coding: utf-8 -*-
import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
	#测试用例执行初始化

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()
    #测试用例完成

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()