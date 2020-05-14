from .helpers.movie_data import Actor


def test_delete(backend):

    stallone = Actor({"name": "ßílvöster Ställöne"})
    arnie = Actor({"name": "Arnöld Schwürzenöggär"})

    backend.save(stallone)
    backend.save(arnie)
    backend.commit()

    assert backend.get(Actor, {"name": stallone.name}) == stallone
    assert backend.get(Actor, {"name": arnie.name}) == arnie
