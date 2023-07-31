import os
import subprocess


def run_tests(test_case_file, allure_results_dir):
    result = subprocess.run(['pytest', f'--alluredir={allure_results_dir}', test_case_file], capture_output=True)
    print(result.stdout.decode('utf-8'))
    print(result.stderr.decode('utf-8'))


def serve_report(allure_results_dir):
    os.system(f'allure serve {allure_results_dir}')


if __name__ == '__main__':
    test_case_file = 'pytests/test_cases'
    allure_results_dir = 'allure-results'
    run_tests(test_case_file, allure_results_dir)
    serve_report(allure_results_dir)
