from .script import outil
from .sousmodule.sousscript import sousoutil
from .autresousmodule.autresousscript import AutreSousModule

print("test outil",outil.moi,outil.path)
print("test sousoutil",sousoutil.moi,sousoutil.path)
print("test autresousoutil",AutreSousModule().moi,AutreSousModule().path)