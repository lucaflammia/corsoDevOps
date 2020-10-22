import unittest
import subprocess

class AutomatedAcceptanceTest(unittest.TestCase):
    def test_behave(self):
        proc = subprocess.Popen(["behave", "-k", "tests/acceptancetests/features/setup.feature"],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        (stdout, stderr) = proc.communicate()
        if "Failing scenarios:" in str(stdout):
            raise Exception(stdout)