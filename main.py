import os
import subprocess

def run_tests():
    result = subprocess.run(['pytest', '--alluredir=allure-results', 'test_cnfin_page.py'], capture_output=True)
    print(result.stdout.decode('utf-8'))
    print(result.stderr.decode('utf-8'))

def serve_report():
    os.system('allure serve allure-results')

if __name__ == '__main__':
    run_tests()
    serve_report()