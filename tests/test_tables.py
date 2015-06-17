""" run with

nosetests -v --nocapture

or

nosetests -v

"""

from cloudmesh_base.util import HEADING

from cloudmesh_common.tables import dict_printer

class Test_tables:

    """
    define tests for dict printer so you test

    yaml
    json
    table
    csv
    dict

    printing

    """
    def setup(self):
        self.d = {
            "a:" : {
                "id": "a",
                "x": 1,
                "y": 2,
                },
            "b:" : {
                "id": "b",
                "x": 3,
                "y": 4,
                },
            }

    def tearDown(self):
        pass

    def test_dummy(self):
        HEADING()
        assert True

    def test_001_yaml(self):
        HEADING()
        
        output = dict_printer(self.d, order=None, header=None, output="table", sort_keys=True)
        print (output)
        assert False

    def test_002_json(self):
        HEADING()
        assert False

    def test_003_table(self):
        HEADING()
        assert False

    def test_004_dict(self):
        HEADING()
        assert False

    def test_005_csv(self):
        HEADING()
        assert False


