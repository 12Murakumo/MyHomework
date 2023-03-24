import os


def get_files_and_dirs(dirname):
    result = {
        'filenames': [],
        'dirnames': []
    }

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            result['filenames'].append(name)
        elif os.path.isdir(path):
            result['dirnames'].append(name)

    result['dirnames'] = sorted(result['dirnames'])
    result['filenames'] = sorted(result['filenames'])

    return result


def sort_files_and_dirs(data, reverse=False):
    data['dirnames'] = sorted(data['dirnames'], reverse=reverse)
    data['filenames'] = sorted(data['filenames'], reverse=reverse)

    return data


def add_file_or_dir(data, name):
    if os.path.isfile(name):
        data['filenames'].append(name)
    elif os.path.isdir(name):
        data['dirnames'].append(name)

    return data
