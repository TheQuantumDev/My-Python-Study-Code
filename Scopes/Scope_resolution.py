# Variable scope is when a variable is visible and accessible
# Scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Scope resolution
def func1():
    x = 20
    print(x)

def func2():
    x = 30
    print(x)
func1()
func2()

# Enclosed Scope resolution
def func1():
    y = 911
    def func2():
        print(y)
    func2()
func1()

# Global Scope resolution
def func1():
    print(z)

def func2():
    print(z)
z = 112
func1()
func2()