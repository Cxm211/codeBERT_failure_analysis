from Simplifiedcodebert import myfunc
import csv
import os

ORIGINAL_INPUT_PATH = "OriginalClones/"
TOKEN_LABEL_INPUT_PATH = "TokenLabels/"
STATEMENT_LABEL_INPUT_PATH = "StatementLabels/"

def get_two_methods(filename):
    ori_file = open(filename, "r")
    list_lines = []
    line = ori_file.readline()
    while line:
        list_lines.append(line)
        line = ori_file.readline()
    for i in range(len(list_lines)):
        if list_lines[i] == "\n" and list_lines[i+1] == "\n":
            m1 = list_lines[:i]
            m2 = list_lines[i+2:]
            break
    if m1 and m2:
        return m1, m2
    else:
        print("Error occurs while detecting method 1 and method 2.")
        return None, None

def get_original_prediction(filename):
    m1, m2 = get_two_methods(ORIGINAL_INPUT_PATH+filename)
    if m1 and m2:
        #Get the prediction of original file
        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            mutation_file.write(line)
        mutation_file.close()
        #Get prediction result
        prediction_result, prediction_float = myfunc()
        return prediction_result, prediction_float

def get_statement_comment(filename):
    m1, m2 = get_two_methods(STATEMENT_LABEL_INPUT_PATH+filename)
    if m1 and m2:
        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            if "***" in line:
                line = line.replace('***','')
                line = "# " + line
            mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" in line:
                line = line.replace('***','')
                line = "# " + line
            mutation_file.write(line)
        mutation_file.close()
        # Get statement comment prediction result
        prediction_result, prediction_float = myfunc()

        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            if "***" not in line:
                line = "# " + line
            mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" not in line:
                line = "# " + line
            mutation_file.write(line)
        mutation_file.close()
        # Get statement comment prediction result
        prediction_prime_result, prediction_prime_float = myfunc()
        return prediction_result, prediction_float, prediction_prime_result, prediction_prime_float

def get_statement_removal(filename):
    m1, m2 = get_two_methods(STATEMENT_LABEL_INPUT_PATH+filename)
    if m1 and m2:
        # Get the prediction
        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            if "***" not in line:
                mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" not in line:
                mutation_file.write(line)
        mutation_file.close()
        # Get statement comment prediction result
        prediction_result, prediction_float = myfunc()

        mutation_file = open("pythontestfolder/mutation.py", "w")
        m1_has = 0
        m2_has = 0
        for line in m1:
            if "***" in line:
                m1_has = 1
                line = line.replace('***', '')
                mutation_file.write(line)
        if m1_has == 0:
            mutation_file.write(m1[0])
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" in line:
                m2_has = 1
                line = line.replace('***', '')
                mutation_file.write(line)
        if m2_has == 0:
            mutation_file.write(m2[0])
        mutation_file.close()
        # Get statement comment prediction result
        prediction_prime_result, prediction_prime_float = myfunc()
        return prediction_result, prediction_float, prediction_prime_result, prediction_prime_float

def get_token_replacement(filename):
    m1, m2 = get_two_methods(TOKEN_LABEL_INPUT_PATH+filename)
    if m1 and m2:
        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            if "***" in line:
                l = line.split("***")
                indexes = []
                for i in range(len(l)):
                    if i % 2 == 1:
                        indexes.append(l[i])
                for index in indexes:
                    l.remove(index)
                line = 'x'.join(l)
            mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" in line:
                l = line.split("***")
                indexes = []
                for i in range(len(l)):
                    if i % 2 == 1:
                        indexes.append(l[i])
                for index in indexes:
                    l.remove(index)
                line = 'y'.join(l)
            mutation_file.write(line)
        mutation_file.close()
        # Get statement comment prediction result
        prediction_result, prediction_float = myfunc()
        return prediction_result, prediction_float

def get_token_removal(filename):
    m1, m2 = get_two_methods(TOKEN_LABEL_INPUT_PATH + filename)
    if m1 and m2:
        mutation_file = open("pythontestfolder/mutation.py", "w")
        for line in m1:
            if "***" in line:
                l = line.split("***")
                indexes = []
                for i in range(len(l)):
                    if i % 2 == 1:
                        indexes.append(l[i])
                for index in indexes:
                    l.remove(index)
                line = ''.join(l)
            mutation_file.write(line)
        mutation_file.write('\n')
        mutation_file.write('\n')
        for line in m2:
            if "***" in line:
                l = line.split("***")
                indexes = []
                for i in range(len(l)):
                    if i % 2 == 1:
                        indexes.append(l[i])
                for index in indexes:
                    l.remove(index)
                line = ''.join(l)
            mutation_file.write(line)
        mutation_file.close()
        # Get statement comment prediction result
        prediction_result, prediction_float = myfunc()
        return prediction_result, prediction_float


def main():
    clone_files = os.listdir(ORIGINAL_INPUT_PATH)
    #a = 0
    for file in clone_files:
        #if a == 1:
            print("Running for " + file)
            original_result, original_float = get_original_prediction(file)
            stat_comment_result, stat_comment_float, stat_comment_prime_result, stat_comment_prime_float = get_statement_comment(file)
            stat_removal_result, stat_removal_float, stat_removal_prime_result, stat_removal_prime_float = get_statement_removal(file)
            token_replace_result, token_replace_float = get_token_replacement(file)
            token_removal_result, token_remove_float = get_token_removal(file)
            f = open("python_result.csv", "a")
            writer = csv.writer(f)
            row = [file, original_result, original_float, stat_comment_result, stat_comment_float, stat_comment_prime_result, stat_comment_prime_float,stat_removal_result, stat_removal_float, stat_removal_prime_result, stat_removal_prime_float,token_replace_result, token_replace_float,token_removal_result, token_remove_float]
            writer.writerow(row)

main()


