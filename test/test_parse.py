'''
test_parse.py: Test parse module
'''

import os
import os.path
import shutil
from nose.tools import with_setup
from utils import check_file
from circ.parse import parse


def setup_function():
    '''
    Enter data directory
    '''
    print('#%s: Moving to data directory' % __name__)
    os.chdir('data')


def teardown_function():
    '''
    Delete circ_out directory and leave data directory
    '''
    print('#%s: Remove test files' % __name__)
    shutil.rmtree('circ_out')
    os.chdir('..')


@with_setup(setup_function, teardown_function)
def test_star_parse():
    '''
    Test STAR parser
    '''
    print('#%s: Test parse STAR' % __name__)
    options = {'-t': 'STAR', '--output': 'circ_out',
               '<fusion>': 'Chimeric.out.junction'}
    parse(options, command='CIRCexplorer2 parse (STAR)', name='parse')
    assert os.path.isdir('circ_out'), 'No circ_out directory'
    check_file('fusion_junction.bed', 'circ_out', 'STAR_out')


@with_setup(setup_function, teardown_function)
def test_mapsplice_parse():
    '''
    Test MapSplice parser
    '''
    print('#%s: Test parse MapSplice' % __name__)
    options = {'-t': 'MapSplice', '--output': 'circ_out',
               '<fusion>': 'fusions_raw.txt'}
    parse(options, command='CIRCexplorer2 parse (Mapsplice)', name='parse')
    assert os.path.isdir('circ_out'), 'No circ_out directory'
    check_file('fusion_junction.bed', 'circ_out', 'MapSplice_out')


@with_setup(setup_function, teardown_function)
def test_segemehl_parse():
    '''
    Test segemehl parser
    '''
    print('#%s: Test parse segemehl' % __name__)
    options = {'-t': 'segemehl', '--output': 'circ_out',
               '<fusion>': 'splicesites.bed'}
    parse(options, command='CIRCexplorer2 parse (segemehl)', name='parse')
    assert os.path.isdir('circ_out'), 'No circ_out directory'
    check_file('fusion_junction.bed', 'circ_out', 'segemehl_out')