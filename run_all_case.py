# coding:utf-8
import unittest
import os
from HTMLTestRunner import HTMLTestRunner
# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    #runner = unittest.TextTestRunner()
    #runner.run(all_case())

    runer = HTMLTestRunner(title="my test", description="netfyee's test", stream=open("sample.html", "wb"),
                           verbosity=2, retry=1, save_last_try=True)
    runer.run(all_case())