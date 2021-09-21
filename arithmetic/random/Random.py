import ryvencore_qt as rc
import random


class RandFloatNode(rc.Node):
    """Generates random float"""

    title = 'Random float'
    init_inputs = [
        rc.NodeInputBP(label="Lower Bound",dtype=rc.dtypes.Integer(default=1)),
    ]
    init_outputs = [
        rc.NodeOutputBP()
    ]
    color = '#fcba03'

    def update_event(self, inp=-1):
        # random float between 0 and value at input
        val = random.random()

        # setting the value of the first output
        self.set_output_val(0, val)


class RandIntNode(rc.Node):
    """Generates random integer"""

    title = 'Random integer'
    init_inputs = [
        rc.NodeInputBP(label="Lower Bound",dtype=rc.dtypes.Integer(default=1)),
        rc.NodeInputBP(label="Upper Bound",dtype=rc.dtypes.Integer(default=1)),
    ]
    init_outputs = [
        rc.NodeOutputBP()
    ]
    color = '#fcba03'

    def update_event(self, inp=-1):
        # random float between 0 and value at input
        val = random.randint(self.input(0),self.input(1))

        # setting the value of the first output
        self.set_output_val(0, val)
