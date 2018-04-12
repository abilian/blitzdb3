from __future__ import absolute_import, print_function, unicode_literals

from ..helpers.movie_data import Actor


def test_implicit_transaction(backend):

    backend.init_schema()
    backend.create_schema()

    al_pacino = Actor({'name' : 'Al Pacino','best_genre' : 'action'})
    #this will be automatically committed
    backend.save(al_pacino)
    assert backend.current_transaction is None
    assert backend._conn is None

def test_explicit_transaction(backend):

    backend.init_schema()
    backend.create_schema()

    al_pacino = Actor({'name' : 'Al Pacino','best_genre' : 'action'})
    #here we explicitly begin a transaction
    transaction = backend.begin()
    backend.save(al_pacino)
    #now the transaction object should be equal to the one we had before
    assert backend.current_transaction == transaction
    assert backend._conn is not None
    backend.commit()
    assert backend.current_transaction is None
    assert backend._conn is None
