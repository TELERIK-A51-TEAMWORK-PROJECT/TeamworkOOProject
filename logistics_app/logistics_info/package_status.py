class PackageStatus:
    OPEN = 'OPEN'
    PROCESSING = 'PROCESSING'    

    STATUS = [OPEN,PROCESSING]

    @classmethod
    def advance_status(cls, current):
        current_index = cls.STATUS.index(current)
        next_index = current_index + 1
        return cls.STATUS[next_index]