def introspection_info(obj):
    dict_info = {'type': type(obj),
                 'attributes': [attr for attr in dir(obj) if not attr.startswith('__')],
                 'methods': [method for method in dir(obj) if method.startswith('__')],
                 'module': obj.__class__.__module__}
    return dict_info


number_info = introspection_info(42)
print(number_info)
