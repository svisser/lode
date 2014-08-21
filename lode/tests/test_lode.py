import glob
import os

import lode

LODEFILE = 'lodefile'


def teardown_function(function):
    for lodefile in glob.glob('*lodefile'):
        os.remove(lodefile)


def test_log_function_exists():
    assert(lode.log('hello') is None)


def test_log_file_created():
    lode.log('created file')
    assert(os.path.isfile(LODEFILE))


def test_thing_is_logged():
    thing = 'thing with some different words'

    lode.log(thing)

    with open(LODEFILE) as f:
        thing_found = False
        for line in f:
            if thing in line:
                thing_found = True

    assert(thing_found)


def test_five_things_are_logged():
    things = ('one', 'two', 'three', 'four')
    things_str = ' '.join(things)

    lode.log(*things)

    with open(LODEFILE) as f:
        things_found = False
        for line in f:
            if things_str in line:
                things_found = True

    assert(things_found)


def test_setting_filename():
    name = 'different_lodefile'
    lode.log('hi there', name=name)
    with open(name) as f:
        assert('hi there' in f.read())


def test_find_caller_function():
    def dummy_function():
        return lode._get_caller_function()

    caller_function = dummy_function()
    assert(caller_function == 'test_find_caller_function')