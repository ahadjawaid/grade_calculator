from calculator import Grades
import argparse
import json
import os

def getConfig(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)

    return config

def preprocessConfig(config):
    for class_config in list(config["class"]):
        for grade_value in list(config["class"][class_config]["grading_scale"]):
            config["class"][class_config]["grading_scale"][float(grade_value)] = (
                config["class"][class_config]["grading_scale"][grade_value])
            del config["class"][class_config]["grading_scale"][grade_value]

    return config

def classInConfig(class_name, config):
    if not config["class"][class_name]:
        raise Exception(f"Class: '{class_name}' was not found in the config.")
    else:
        return True

def printScoreNeeded(item):
    scores_needed = user_grades.letterGradesPossibleForItem(*item)
    print(f"Grades needed for {item[0].capitalize()} {item[1] + 1}:")
    for letter in scores_needed:
        print(f"Score of {round(scores_needed[letter], 2)} to get a {letter}")

# Setup arg parser
parser = argparse.ArgumentParser(prog = 'Grade calculator')
parser.add_argument('-c', '--class_name')           # Class name defined in config
parser.add_argument('-l', '--get_letter_grade',     # Flag to print current letter grade
                    action="store_true")
parser.add_argument('-s', '--score_needed')         # Input item needed Ex: 'exam 3'
# Get arguments
args = parser.parse_args()
class_name = args.class_name
get_letter_grade_flag = args.get_letter_grade
score_needed_item = args.score_needed
print(type(get_letter_grade_flag))

# Import config
config_path = os.path.join(os.getcwd(), "config.json")
config = getConfig(config_path)

# Validate argument is in config
classInConfig(class_name, config)
config = preprocessConfig(config)

class_config = config["class"][class_name]
user_grades = Grades(class_config["grading_scale"], class_config["scores"], class_config["scores_weight"])

if get_letter_grade_flag:
    print(f"Current letter grade: {user_grades.letter_grade}")

if score_needed_item:
    item = score_needed_item.split(" ")
    item[1] = int(item[1]) - 1
    printScoreNeeded(item)
