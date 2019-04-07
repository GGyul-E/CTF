import angr
def main():
	project = angr.Project("angrme", auto_load_libs= False)
	ex = project.factory.path_group()
	ex.explore(find=lambda path: ':)' in path.state.posix.dumps(1), avoid=lambda path: ':(' in path.state.posix.dumps(1) )
	#ex.use_technique(angr.exploration_techniques.DFS())
	#avoid_addr = [0x2390]
	#find_addr = 0x238f
	#ex.explore(find=find_addr, avoid=avoid_addr)

	return ex.found[0].state.posix.dumps(3)

if __name__ == '__main__':
	print(repr(main()))