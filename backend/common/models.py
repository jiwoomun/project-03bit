from dataclasses import dataclass


@dataclass
class DataTransferObject(object):

    context: str
    fname: str
    dframe: object


    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def dfname(self) -> str: return self._dfname

    @dfname.setter
    def dfname(self, dfname): self._dfname = dfname

