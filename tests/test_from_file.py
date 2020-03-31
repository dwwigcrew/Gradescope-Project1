import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags, visibility
import subprocess32 as subprocess


class TestDiff(unittest.TestCase):
    def setUp(self):
        pass

    @weight(10.0)
    @visibility("hidden")
    @tags("Test1")
    def test_from_file1(self):
        # Test 1
        """Test 1"""
        with open('inputs/test1.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test1.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()

    @weight(10.0)
    @visibility("hidden")
    @tags("Test 2")
    def test_from_file2(self):
        # Test 2
        """Test 2"""
        with open('inputs/test2.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test2.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()

    @weight(10.0)
    @visibility("hidden")
    @tags("Test 3")
    def test_from_file3(self):
        # Test 3
        """Test 3"""
        with open('inputs/test3.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test3.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()

    @weight(10.0)
    @visibility("hidden")
    @tags("Test 4")
    def test_from_file4(self):
        # Test 4
        """Test 4"""
        with open('inputs/test4.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test4.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()

    @weight(10.0)
    @visibility("hidden")
    @tags("Test 5")
    def test_from_file5(self):
        # Test 5
        """Test 5"""
        with open('inputs/test5.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test5.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()

    @weight(10.0)
    @visibility("hidden")
    @tags("Test 6")
    def test_from_file6(self):
        # Test 6
        """Test 6"""
        with open('inputs/test6.in', 'r') as infile:
            enee140_gen_rnd = subprocess.Popen(['./enee140_gen_rnd'], stdin=infile, stdout=subprocess.PIPE)
            output = enee140_gen_rnd.stdout.read().strip()
        with open("expected_outputs/test6.out", "r") as outputFile:
            referenceOutput = outputFile.read()
        referenceOutput = "".join(referenceOutput.split())
        output = "".join(output.split())
        self.assertEqual(output, referenceOutput)
        enee140_gen_rnd.terminate()