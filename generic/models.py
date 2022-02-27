from django.db import models


class CustomModel(models.Model):
    def is_deletable(self):
        # get all the related objects
        for rel in self._meta.get_fields():
            try:
                # check if there is a relationship with at least one
                # related object
                related = rel.related_model.objects.filter(
                    **{rel.field.name: self}
                )
                if related.exists():
                    # if there is, return a tuple of flag = False and
                    # the related_model object
                    return False, related
            except AttributeError:
                # an attribute error for field occurs when checking for
                # AutoField. Just pass as we don't need to check for
                # AutoField
                pass
        return True, None

    class Meta:
        abstract = True
