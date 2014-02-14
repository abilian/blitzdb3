#Blitz-DB

Blitzdb (or simply blitz) is a document-oriented database toolkit for Python. It can be used either as a  **stand-alone, flat-file database** or in conjunction with another database backend such as **MongoDB** or **MySQL**.

Blitz supports document indexing and provides powerful query mechanism similar to MongoDB.

##Examples

To get an idea of what you can do with Blitz, here are some examples.

###Creating objects

    from blitzdb import Object
    
    class Movie(Object):
        pass
        
    class Actor(Object):
        pass
    
    the_godfather = Movie({'name': 'The Godfather','year':1972})
    
    marlon_brando = Actor({'name':'Marlon Brando'})
    al_pacino = Actor({'name' : 'Al Pacino'})
        
###Storing of objects in the database:

    from blitzdb import FileBackend
    
    backend = FileBackend("/path/to/my/db")
    
    backend.register(Movie,{'collection':'movies','pk':1L})
    backend.register(Actor,{'collection':'actors'})

    the_godfather.save(backend)
    marlon_brando.save(backend)
    al_pacino.save(backend)
    
###Retrieving objects from the database:

    the_godfather = backend.get(Movie,{'pk':1L})
    #or...
    the_godfather = backend.get(Movie,{'name' : 'The Godfather'})
    
###Filtering objects

    movies_from_1972 = backend.filter(Movie,{'year' : 1972})

###Creating nested object references
   
    the_godfather.cast = {'Don Vito Corleone' : marlon_brando, 'Michael Corleone' : al_pacino}
    
    #Objects stored within other objects will be automatically converted to database references.

    marlon_brando.performances = [the_godfather]
    al_pacino.performances = [the_godfather]
    
    marlon_brando.save(backend)
    al_pacino.save(backend)
    #Will store references to the movies within the documents in the DB
    
###Creation of database indexes and advanced querying

    backend.create_index(Actor,'performances')
    #Will create an index for fast querying
    
    godfather_cast = backend.filter(Actor,{'movies' : the_godfather})
    #Will return 'Al Pacino' and 'Marlon Brando'

###Arbitrary filter expressions

    star_wars_iv = Movie({'name' : 'Star Wars - Episode IV: A New Hope','year': 1977})
    star_wars_iv.save()

    movies_from_the_seventies = backend.filter(Movie,{'year': lambda year : True if year >= 1970 and year < 1980 else False})
    #Will return Star Wars & The Godfather (man, what a decade!)


#Blitz-DB

Blitzdb (or simply blitz) is a document-oriented database toolkit for Python. It can be used either as a  **stand-alone, flat-file database** or in conjunction with another database backend such as **MongoDB** or **MySQL**.

Blitz supports document indexing and provides powerful query mechanism similar to MongoDB.

##Examples

To get an idea of what you can do with Blitz, here are some examples.

###Creating objects

    from blitzdb import Object
    
    class Movie(Object):
        pass
        
    class Actor(Object):
        pass
    
    the_godfather = Movie({'name': 'The Godfather','year':1972})
    
    marlon_brando = Actor({'name':'Marlon Brando'})
    al_pacino = Actor({'name' : 'Al Pacino'})
        
###Storing of objects in the database:

    from blitzdb import FileBackend
    
    backend = FileBackend("/path/to/my/db")
    
    backend.register(Movie,{'collection':'movies','pk':1L})
    backend.register(Actor,{'collection':'actors'})

    the_godfather.save(backend)
    marlon_brando.save(backend)
    al_pacino.save(backend)
    
###Retrieving objects from the database:

    the_godfather = backend.get(Movie,{'pk':1L})
    #or...
    the_godfather = backend.get(Movie,{'name' : 'The Godfather'})
    
###Filtering objects

    movies_from_1972 = backend.filter(Movie,{'year' : 1972})

###Creating nested object references
   
    the_godfather.cast = {'Don Vito Corleone' : marlon_brando, 'Michael Corleone' : al_pacino}
    
    #Objects stored within other objects will be automatically converted to database references.

    marlon_brando.performances = [the_godfather]
    al_pacino.performances = [the_godfather]
    
    marlon_brando.save(backend)
    al_pacino.save(backend)
    #Will store references to the movies within the documents in the DB
    
###Creation of database indexes and advanced querying

    backend.create_index(Actor,'performances')
    #Will create an index for fast querying
    
    godfather_cast = backend.filter(Actor,{'movies' : the_godfather})
    #Will return 'Al Pacino' and 'Marlon Brando'

###Arbitrary filter expressions

    star_wars_iv = Movie({'name' : 'Star Wars - Episode IV: A New Hope','year': 1977})
    star_wars_iv.save()

    movies_from_the_seventies = backend.filter(Movie,{'year': lambda year : True if year >= 1970 and year < 1980 else False})
    #Will return Star Wars & The Godfather (man, what a decade!)

