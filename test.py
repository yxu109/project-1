import os
import subprocess
import sys

class TestResult:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.failures = []

    def add_failure(self, test_name, mode, expected, got):
        self.failed += 1
        self.failures.append((test_name, mode, expected, got))

    def add_pass(self):
        self.passed += 1

    def summary(self):
        summary = f"\nOK: {self.passed}\noutput mismatch: {self.failed}\ntotal: {self.passed + self.failed}\n"
        for fail in self.failures:
            test_name, mode, expected, got = fail
            summary += f"\nFAIL: {test_name} failed in {mode} mode (TestResult.OutputMismatch)\n      expected:\n{expected}\n\n           got:\n{got}\n"
        return summary

def run_test(prog, test_name, test_dir, results):
    input_file = os.path.join(test_dir, f'{prog}.{test_name}.in')
    expected_output_file = os.path.join(test_dir, f'{prog}.{test_name}.out')
    expected_arg_output_file = os.path.join(test_dir, f'{prog}.{test_name}.arg.out')

    # Run test with STDIN
    with open(input_file, 'r') as infile, open(expected_output_file, 'r') as exp_outfile:
        result = subprocess.run(['python', f'{prog}.py'], stdin=infile, text=True, capture_output=True)
        actual_output = result.stdout.strip()
        expected_output = exp_outfile.read().strip()

        if actual_output == expected_output:
            results.add_pass()
        else:
            results.add_failure(test_name, "STDIN", expected_output, actual_output)

    # Run test with command-line argument
    if os.path.exists(expected_arg_output_file):
        with open(expected_arg_output_file, 'r') as exp_arg_outfile:
            result = subprocess.run(['python', f'{prog}.py', input_file], text=True, capture_output=True)
            actual_arg_output = result.stdout.strip()
            expected_arg_output = exp_arg_outfile.read().strip()

            if actual_arg_output == expected_arg_output:
                results.add_pass()
            else:
                results.add_failure(test_name, "argument", expected_arg_output, actual_arg_output)

def find_and_run_tests(test_dir):
    results = TestResult()
    for filename in os.listdir(test_dir):
        if filename.endswith('.in'):
            prog, test_name = filename.split('.')[:2]
            run_test(prog, test_name, test_dir, results)
    return results

def main():
    test_dir = 'test/'
    results = find_and_run_tests(test_dir)
    print(results.summary())
    if results.failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
