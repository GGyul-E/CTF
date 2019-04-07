import os
import angr


project = angr.Project('./elementary', load_options={'auto_load_libs': False})
path_group = project.factory.path_group()

avoid_addr = 0x786
find_addr = 0x400773

path_group.explore(find=lambda path: 'Good job!' in path.state.posix.dumps(1))

print path_group.found[0].state.posix.dumps(0)
