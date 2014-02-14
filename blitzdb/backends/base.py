import abc

from blitzdb.object import Object
    
class Backend(object):

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.classes = {}
        self.collections = {}

    def register(self,cls,parameters):
        self.classes[cls] = parameters
        if 'collection' in parameters:
            self.collections[parameters['collection']] = cls
        else:
            self.collections[cls.__name__.lower()] = cls
            self.classes[cls]['collection'] = cls.__name__.lower()

    def serialize(self,obj):
        if isinstance(obj,dict):
            output_obj = {}
            for (key,value) in obj.items():
                output_obj[key] = self.serialize(value)
        elif isinstance(obj,list):
            output_obj = map(lambda x:self.serialize(x),obj)
        elif isinstance(obj,tuple):
            output_obj = tuple(map(lambda x:self.serialize(x),obj))
        elif isinstance(obj,Object):
            if not obj.__class__ in self.classes:
                raise AttributeError("Unknown object type: %s" % obj.__class__.__name__)
            collection = self.classes[obj.__class__]['collection']
            if obj.embed:
                output_obj = {'_collection':collection,'_attributes':self.serialize(obj.attributes)}
            else:
                if obj.pk == None:
                    raise AttributeError("Object not saved:"+str(obj))
                output_obj = {'_pk':obj.pk,'_collection':self.classes[obj.__class__]['collection']}
        else:
            output_obj = obj
        return output_obj


    def deserialize(self,obj):
        if isinstance(obj,dict):
            if '_collection' in obj and '_pk' in obj and obj['_collection'] in self.collections:
                output_obj = self.create_instance(obj['_collection'],{'pk' : obj['_pk']},lazy = True)
            else:
                output_obj = {}
                for (key,value) in obj.items():
                    output_obj[key] = self.deserialize(value)
        elif isinstance(obj,list) or isinstance(obj,tuple):
            output_obj = map(lambda x:self.deserialize(x),obj)
        else:
            output_obj = obj
        return output_obj

    def create_instance(self,collection_or_class,attributes,lazy = False):
        if collection_or_class in self.classes:
            cls = collection_or_class
        elif collection_or_class in self.collections:
            cls = self.collections[collection_or_class]
        else:
            raise AttributeError("Unknown collection or class: %s!" % str(collection) )

        if 'constructor' in self.classes[cls]:
            obj = self.classes[cls]['constructor'](attributes,lazy = lazy)
        else:
            obj = cls(attributes,lazy = lazy)
        if lazy:
            obj._lazy_backend = self

        return obj

    def get_collection_name_for_obj(self,obj):
        return self.get_collection_name_for_cls(obj.__class__)

    def get_collection_name_for_cls(self,cls):
        if not cls in self.classes:
            raise AttributeError("Unknown object type: %s" % cls.__name__)
        collection_name = self.classes[cls]['collection']
        return collection_name

    def compile_query(self,query_dict):

        def access_path(d,path):
            v = d
            for elem in path:
                if isinstance(v,list):
                    v = v[int(elem)]
                else:
                    v = v[elem]
            return v

        compiled_query = []
        for key,value in query_dict.items():
            splitted_key = key.split(".")
            accessor = lambda d,path = splitted_key : access_path(d,path = path)
            if isinstance(value,Object):
                value = {'_collection' : self.get_collection_name_for_obj(value),'_pk':value.pk}
            compiled_query.append((key,accessor,value))
        return compiled_query 

    @abc.abstractmethod
    def save(self,obj,cache = None):
        pass

    @abc.abstractmethod
    def get(self,cls,properties):
        pass

    @abc.abstractmethod
    def delete(self,obj):
        pass        

    @abc.abstractmethod
    def filter(self,cls,properties,sort_by = None,limit = None,offset = None):
        pass