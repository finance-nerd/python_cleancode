# def function(kwargs): ## error
# def function(*kwargs): ## error
def function(**kwargs):
    print(kwargs)


function(**{"key": "value", "key1": "value1"})
function(key="value", key1="value1")
