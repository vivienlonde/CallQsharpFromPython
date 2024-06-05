import qsharp

qsharp.init(project_root = '../CallQsharpFromPython')

result = qsharp.eval("Grover.Main()")

print(result)