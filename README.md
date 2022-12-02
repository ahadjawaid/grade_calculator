# Grade Calculator
Grade calculator takes your grades from the config file and generate your current letter grade and can tell you what score you need to get on the assignments to get specific letter score


## Setup
Download the files 
```shell
git clone https://github.com/ahadjawaid/grade_calculator.git
```

### Config
Create config in the root directory
```shell
touch config.json
```

Open the config file or using the following command to open it
```shell
nano config.json
```

Copy the config template and paste into config.json
```json
{   
    "class": {
        "automata": {
            "grading_scale": {
                "90": "A+",
                "80": "A",
                "70": "A-",
                "65": "B+",
                "55": "B",
                "45": "B-",
                "35": "C+",
                "30": "C",
                "25": "C-",
                "20": "D+"
            },
            "scores": {
                "exam": [0, 0, 0],
                "hw": [0, 0, 0, 0, 0]
            },
            "scores_weight": {
                "exam": [0.25, 0.3, 0.35],
                "hw": [0.02, 0.02, 0.02, 0.02, 0.02]
            }
        }
    }
}
```
Change config data to fit your class's data

## Running program

| Flag        | Format   | Example  |What it does  |
| ------------- |:-------------:| -----:| -----:|
| '-c' or '--class_name'      | -c <class name from config> | -c "automata" | Select the class |
| '-l' or '--get_letter_grade'      | -l      |   -l | Will output current letter grade from config data | 
| '-s' or '--score_needed' | -s <item index>      |    -s "exam 3" | Output scores needed to get letter grades on and assignment |

Command for the program to get scores needed
```shell
python3 main.py -c automata -s "exam 3"
```
Output
```output
Grades needed for Exam 3:
Score of 98.49 to get a A
Score of 69.91 to get a A-
Score of 55.63 to get a B+
Score of 27.06 to get a B
```

Command to get current letter grade
```shell
python3 main.py -c automata -l
```
Output
```output
Current letter grade: B-
```
