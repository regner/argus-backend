#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class BaseService(object):
    __model__ = None
    __db__ = None

    def _isinstance(self, model, raise_error=True):
        """Verify specified object matches the services defined model."""
        rv = isinstance(model, self.__model__)

        if not rv and raise_error:
            raise ValueError('{} is not of type {}'.format(model, self.__model__))

        return rv

    def save(self, model):
        """Save a given model to the database."""
        self._isinstance(model)
        self.__db__.session.add(model)
        self.__db__.session.commit()

    def get(self, model_id):
        """Get a model by a given ID."""
        return self.__model__.query.get(model_id)

    #
    # def all(self):
    #     """Returns a generator containing all instances of model."""
    #     return self.__model__.query.all()
    #
    # def get(self, id):
    #     """Returns an instance of the service's model with the specified id."""
    #     return self.__model__.query.get(id)
    #
    # def get_all(self, *ids):
    #     """Returns a list of instances of the service's model with the specified ids."""
    #     return self.__model__.query.filter(self.__model__.id.in_(ids)).all()
    #
    #
    #
    # def find(self, **kwargs):
    #     """Returns a list of instances of the service's model filtered by the specified key word arguments."""
    #     return self._find(**kwargs).all()
    #
    #
    #
    # def get_or_404(self, id):
    #     """Returns an instance of the service's model with the specified id or raises 404 it doesn't exist."""
    #     return self.__model__.query.get_or_404(id)
    #
    # def new(self, **kwargs):
    #     """Returns a new, unsaved instance of the service's model class."""
    #     return self.__model__(**kwargs)
    #
    # def update(self, model, **kwargs):
    #     """Returns an updated instance of the service's model class."""
    #     self._isinstance(model)
    #
    #     for k, v in kwargs.items():
    #         setattr(model, k, v)
    #
    #     self.save(model)
    #
    #     return model
    #
    # def delete(self, obj):
    #     """Immediately deletes the specified model instance."""
    #     self._isinstance(obj)
    #     self.__db__.session.delete(obj)
    #     self.__db__.session.commit()
    #
    # def paginate(self, page=1, per_page=10, order_by=None, desc=False, filter_by=None, error_out=True):
    #     """Returns a SQLAlchemy Pagination object of all results."""
    #     if filter_by is None:
    #         filter_by = {}
    #
    #     order_by = order_by or self.__model__.id
    #     order_by = order_by.desc() if desc else order_by.asc()
    #
    #     return self.__model__.query.filter_by(**filter_by).order_by(order_by).paginate(page, per_page, error_out)
