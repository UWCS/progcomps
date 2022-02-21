from sys import stdin

def remove_last_blank(arr):
    if arr[-1] == "":
        arr = arr[:-1]
    return arr

with open("output.txt") as file:
    test_lines = remove_last_blank(file.read().split("\n"))

submission_lines = remove_last_blank(stdin.read().split("\n"))

correct = sum([a == b for a, b in zip(test_lines, submission_lines)])
total = len(test_lines)
submitted = len(submission_lines)

if correct != total:
    for i, (test, submission) in enumerate(zip(test_lines, submission_lines)):
        i += 1
        if test != submission:
            print(f"! Test {i}: Expected {test} | Got {submission}")
        
print(f"{correct}/{total} (Submitted {submitted})")
