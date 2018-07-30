import subprocess

classifiers = {
    'svm-light': {
        'train': 'svm_learn',
        'classify': 'svm_classify'
    }
}

def train(classifier, feature_file, model_file):
    try:
        subprocess.run(
            [
                classifiers[classifier]['train'],
                feature_file,
                model_file
            ]
        )
    except KeyError:
        print("No such classifier: %s." % classifier)
    except FileNotFoundError:
        print("%s binary not found in $PATH." % classifiers[classifier]['train'])
        exit(1)


def classify(classifier, feature_file, model_file, output_file):
    try:
        subprocess.run(
            [
                classifiers[classifier]['classify'],
                feature_file,
                model_file,
                output_file
            ]
        )
    except KeyError:
        print("No such classifier: %s." % classifier)
    except FileNotFoundError:
        print("svm_classify binary not found in $PATH.")
        exit(1)

