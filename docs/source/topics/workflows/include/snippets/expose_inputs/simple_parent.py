from aiida.engine import ToContext, WorkChain
from child import ChildWorkChain


class SimpleParentWorkChain(WorkChain):
    @classmethod
    def define(cls, spec):
        super().define(spec)
        spec.expose_inputs(ChildWorkChain)
        spec.expose_outputs(ChildWorkChain)
        spec.outline(cls.run_child, cls.finalize)

    def run_child(self):
        child = self.submit(ChildWorkChain, **self.exposed_inputs(ChildWorkChain))
        return ToContext(child=child)

    def finalize(self):
        self.out_many(self.exposed_outputs(self.ctx.child, ChildWorkChain))
