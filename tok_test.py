import math as module

meth = type(str.count) 
for x in module.__dict__: 
    bltin = getattr(module, x) 
    if isinstance(bltin, meth): 
            print(\
f"{x}: {'{'}\n"
f"\t$meth: methods.{x},\n" 
f"\t$flags:{'{}'},\n"
f"\t$textsig: \"{ bltin.__text_signature__.__repr__()[1:-1] }\",\n"
f"\t$doc: \"{bltin.__doc__.__repr__()[1:-1]}\" {'}' },")