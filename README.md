# CS453 Assignment 3: Mutation Testing Tool  for Python

With this assignment, we will try implementing a basic mutation testing tool for Python that can mutate the source code, run given `pytest` test suites, report changed behaviour, and generate kill matrices. The skeleton code, called `pmut.py`, specifies the required functionalities. Assume that the project you want to apply mutation testing to is scored under directory `examples/example1`. When you invoke `pmut.py` as follows:

```bash
$ python3 pmut.py --action mutate --source examples/example1 --output ./mutation_diffs --km ./kill_matrix
```

it should apply mutation operators to all files under `examples/example1`, one mutation to one location in one file at a time, and generate mutants under `./mutated_versions`. You should generate each mutant as a diff against the original program, so that you can get the mutated version when you apply the patch from the root directory of the original project. Each diff file should be named using the following naming convention:

```
[mutation_operator]_[target_filename]_[line_number]_[index].diff
```
**If a mutation operator can generate multiple mutants from the same line in the same file**, sort the mutated line alphabetically and index them from 0 (use two digits, e.g., 00, 01, 02...). If there is only a single mutant, the index is naturally 0.

### Mutation Operators

You should implement the following mutation operators at the minimum:
- PITest

### Skeleton and Test Code

This repository includes a skeleton code named `pmut.py` for your profiler. Please keep the existing code and the command line interface provided, so that GitHub Classroom can run the automated grading scripts. 

The tool should operate in two different action modes, which is specified by the parameter `action`. It can be either `mutate`, or `execute`.

1. Mutation mode (`--action = mutate`)

```bash
$ python pmut.py --action mutate --source [source directory] --output [output directory]
```
The tool should mutate whatever it finds under the source directory, and create the resulting mutation diff patches under the output directory: follow the naming convention above.

2. Execution mode (`--action = execute`)
```
$ python pmut.py --action execute --source [source directory] --mutants [mutation diff directory] --kill [kill matrix directory]
```
The tool should read all diffs in mutation diff directory one by one, apply the mutation to the source directory, execute the `pytest` test cases in the source directory one by one, and write the output to the kill matrix directory. In the kill matrix directory, there should be three files:

- Test Case Index File (`test_index.json`): this file should contain the dictionary of test case name to kill matrix row index. Use `[test function name]@[pytest file name without .py]` naming convention for dictionary keys.
- Mutant Index File (`mutation_index.json`): this file should contain the dictionary of mutant name to kill matrix column Index. Use the same mutant naming sonvention for dictionary keys.
- Kill Matrix File (`kill_matrix.np`): this file should be a `numpy` array of type `int32`, whose size is [number of test cases] by [number of mutants]. The array should be saved using [`savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt) function in `numpy`: 1 corresponds to the corresponding mutant (column index) killed by the corresponding test case (row index), and 0 otherwise.

Note that a mutant is killed if 1) the test outcome is different, or 2) the `stdout` or the `stderr` output is different, between the original and the mutated version. **At the end of the execution, the source directory should be reverted back to the original state.**

### Libraries and Python Version

The template repository is configured with Python 3.9. We will use numpy to write the kill matrix.

### Submission Deadline

You need to submit this assignment before **18:00 on 26th of May, 2021.**
