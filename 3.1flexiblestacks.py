class flexibleStack:
    _list = None
    _maxlen = 0
    
    def __init__(self, len):
        self._list = [None] * len
        self._maxlen = len
    
    
    