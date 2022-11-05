from util import tah
from ai import tah_pocitace
from piskvorky import vyhodnot


def test_tah1():
    assert tah('-----o--------x-----', 10, 'x')


def test_tah2():
    assert tah('--------------------', 21, 'x')


def test_tah3():
    assert tah('--------------------', 10, 'y')


def test_tah_pocitace1():
    assert tah_pocitace('--------------')


def test_tah_pocitace2():
    assert tah_pocitace('--x--------o---')


def test_tah_pocitace3():
    assert tah_pocitace('xoxoxoxoxoxo')


def test_vyhodnot():
    assert vyhodnot('-----x-----')
    assert vyhodnot('---xxx-----')
    assert vyhodnot('xxooxxooxxoo')
