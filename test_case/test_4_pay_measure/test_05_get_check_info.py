import unittest
from testcase.api.login.login_all_api import LoginApi
from utils.config import NewConfig
# from testcase.api.studyCenter.report.get_measure_history_report import GetMeasureHistoryReport
from testcase.api.studyCenter.report.get_check_info import GetCheckInfo


class TestGetCheckInfo(unittest.TestCase):
    def setUp(self):
        cfg_info = NewConfig()
        self.common, self.headers = cfg_info.get_info()
        t = LoginApi()
        self.access_token = t.get_access_token(self.common, self.headers)
        self.sevicesID = t.get_user_study_center(self.common, self.headers, self.access_token)
        self.check_info = GetCheckInfo(self.common, self.headers, self.access_token)

    def tearDown(self):
        pass

    def test_get_check_info(self):
        code, datas = self.check_info.get_check_info(self.sevicesID)
        self.assertEqual(code, 0)
        self.assertEqual(int(datas.get('markWord')), 0)
        self.assertEqual(int(datas.get('knowledgePoint')), 0)
        self.assertEqual(int(datas.get('higherThan')), 0)
        self.assertEqual(int(datas.get('sortIdx')), 0)



if __name__ == '__main__':
    unittest.main()