from filter_versions.filter4 import MyFilter

f = MyFilter()
f.train("./tests")
f.test("./tests")