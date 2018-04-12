from __future__ import absolute_import

import pytest

from .helpers.movie_data import Actor, Movie


def test_basic_delete(backend, small_test_data):

    backend.filter(Actor, {}).delete()
    backend.commit()

    assert len(backend.filter(Actor, {})) == 0


def test_basic_storage(backend, small_test_data):

    (movies, actors, directors) = small_test_data

    assert len(backend.filter(Movie, {})) == len(movies)
    assert len(backend.filter(Actor, {})) == len(actors)

def test_delete(backend):

    actor = Actor({'foo' : 'bar'})

    backend.save(actor)
    backend.commit()

    assert actor.foo == 'bar'

    assert backend.get(Actor,{'pk' : actor.pk}).foo == 'bar'

    del actor.foo

    with pytest.raises(AttributeError):
        actor.foo

    with pytest.raises(KeyError):
        actor['foo']

    backend.save(actor)
    backend.commit()

    with pytest.raises(AttributeError):
        backend.get(Actor,{'pk' : actor.pk}).foo

