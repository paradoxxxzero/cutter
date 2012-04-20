from _ import cut, flatten


def test_cut_list_of_dict():
    list_of_dict = [
        {'a': 'a', 'b': 2, 0: 0},
        {'a': None, 'c': 4},
        {'z': 5, 'a': 0, 'b': 3, 5: 'foo'}
    ]
    assert cut(list_of_dict)['a'] == ['a', None, 0]
    assert cut(list_of_dict)['b'] == [2, 3]
    assert cut(list_of_dict)['j'] == []
    assert cut(list_of_dict)[5] == ['foo']
    assert cut(list_of_dict)[2] == []
    assert cut(list_of_dict)[0] == [0]


def test_cut_list_of_list():
    list_of_list = [
        list(range(4)),
        list(reversed(range(4))),
        list(range(12, 37, 3))
    ]
    assert cut(list_of_list)[3] == [3, 0, 21]
    assert cut(list_of_list)[1] == [1, 2, 15]
    assert cut(list_of_list)[5] == [27]
    assert cut(list_of_list)[50] == []
    assert cut(list_of_list)[0] == [0, 3, 12]


def test_cut_list_of_obj():

    class cls(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    list_of_obj = [
        cls(at1=1, at2=23, at3=None, at4='foo'),
        cls(at1=2, at2='bar', at4=cls()),
        cls(at1=[2., 4], at2=23, at3=None),
        cls(at2={})
    ]

    assert cut(list_of_obj)['at1'] == [1, 2, [2., 4]]
    assert cut(list_of_obj)['at2'] == [23, 'bar', 23, {}]
    assert cut(list_of_obj)['at3'] == [None, None]
    assert cut(list_of_obj)['at5'] == []


def test_flatten():
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[1], [2, 3]]) == [1, 2, 3]
    assert flatten([[[1, 2], [3]], [4, [5]]]) == [1, 2, 3, 4, 5]
    assert flatten([1]) == [1]
    assert flatten(['ab']) == ['ab']


def test_complex_cuts_list_of_dicts_of_dicts():
    list_complex = [
        {'A': {'b': 1, 'c': 2},
         'B': {'b': 12, 'd': 21}},
        {'C': {'a': 0, 'c': 2},
         'B': {'b': 'u', 'd': None, 'a': {'p': 2, 'T': 12}}},
        {'B': {'a': {'T': 4, 'a': 3}, 'b': 17},
         'A': {'p': 'a', 'e': '_', 'b': ''}},
        {'D': {'c': '0', 'z': 'w'},
         'C': {'c': 'u', 'p': 'u'}}
    ]
    assert cut(list_complex)['A', 'b'] == [1, '']
    assert cut(list_complex)['B', 'b'] == [12, 'u', 17]
    assert cut(list_complex)['B', 'a', 'T'] == [12, 4]


def test_complex_cuts_list_of_dicts_of_list_of_dicts():
    list_complex = [
        {'A': [
            {'b': 1, 'c': 2},
            {'b': 12, 'd': 21}
        ],
        'B': [
            {'a': 0, 'c': 2},
            {'b': 'u', 'd': None, 'a': {'p': 2, 'T': 12}}],
         },
        {'B': [
            {'p': 'a', 'e': '_', 'b': ''},
            {'a': {'T': 4, 'a': 3}, 'b': 17}
        ],
        'D': [
            {'c': '0', 'z': 'w'},
            {'c': 'u', 'p': 'u'}],
         }
    ]
    assert cut(list_complex)['A', ..., 'b'] == [1, 12]
    assert cut(list_complex)['B', ..., 'b'] == ['u', '', 17]
    assert cut(list_complex)['B', ..., 'a', 'T'] == [12, 4]
