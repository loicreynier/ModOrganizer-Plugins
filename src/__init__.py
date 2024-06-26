
try:
    from .rootbuilder_init import createPlugins as rbPlugins
except:
    def rbPlugins(): return []
try: 
    from .profilesync_init import createPlugins as psPlugins
except: 
    def psPlugins(): return []
try:
    from .pluginfinder_init import createPlugins as pfPlugins
except:
    def pfPlugins(): return []
try:
    from .openmwplayer_init import createPlugins as ompPlugins
except:
    def ompPlugins(): return []
try:
    from .shortcutter_init import createPlugins as scPlugins
except:
    def scPlugins(): return []

def createPlugins():
    plugins = []
    plugins.extend(rbPlugins())
    plugins.extend(psPlugins())
    plugins.extend(pfPlugins())
    plugins.extend(ompPlugins())
    plugins.extend(scPlugins())
    return plugins
