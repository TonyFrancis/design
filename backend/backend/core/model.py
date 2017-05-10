

class LoadByIdMixin(object):
    """
    Load by id classmethod

    return None is not present.
    """
    @classmethod
    def load_by_id(cls, id):
        try:
            return cls.objects.get(pk=id)
        except cls.DoesNotExist as e:
            return None
